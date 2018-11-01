from flask import Flask, render_template, request, jsonify, Response
import pickle
import pandas as pd

app = Flask(__name__)

# load in model
model = pickle.load(open('linreg.p', 'rb'))

# home route
@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

# mpg route
@app.route('/mpg', methods = ['GET'])
def mpg():
    return render_template('mpg.html')

# create inference route
@app.route('/inference', methods = ['POST'])
def inference():
    req = request.get_json()
    print(req)
    c,h,w = req['cylinders'],req['horsepower'],req['weight']
    prediction = float(model.predict([[c,h,w]]))
    print(prediction)
    return jsonify({'c':c,'h':h,'w':w,'prediction':prediction})

# create route for plotting
@app.route('/plot', methods = ['GET'])
def plot():
    df = pd.read_csv('cars.csv')
    data = list(zip(df.mpg, df.weight))
    return jsonify(data)

if __name__ == '__main__':
    app.run(app.run(host ='0.0.0.0', port = 3333, debug = True))