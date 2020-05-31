from flask import Flask, render_template, request, jsonify, Response
import pickle
import pandas as pd
import random
import numpy as np
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# build in model
X_train = pd.read_csv('../data/processed/first_quarter/X_train.csv')
y_train = pd.read_csv('../data/processed/first_quarter/y_train.csv')
y_train = y_train['module_not_completed']
X_test = pd.read_csv('../data/processed/first_quarter/X_test.csv')
y_test = pd.read_csv('../data/processed/first_quarter/y_test.csv')
y_test = y_test['module_not_completed']
X_train.fillna(value = 0, inplace = True)
y_train.fillna(value = 0, inplace = True)
X_test.fillna(value = 0, inplace = True)
y_test.fillna(value = 0, inplace = True)
# best model as determined by grid search
rf_model = RandomForestClassifier(bootstrap=True, class_weight=None,criterion='gini', max_depth=50, max_features='auto',max_leaf_nodes=None,min_impurity_decrease=0.0,min_impurity_split=None, min_samples_leaf=5, min_samples_split=5,min_weight_fraction_leaf=0.0, n_estimators=1000, n_jobs=-1,oob_score=False, random_state=None, verbose=0, warm_start=False)
rf_model.fit(X_train, y_train)

# select base record
X_test = pd.read_csv('../data/processed/first_quarter/X_test.csv')
X_test.fillna(value=0, inplace=True)
# num = random.randint(0, X_test.shape[0])
num = 400

# home route
@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

# model route
@app.route('/model', methods = ['GET'])
def model():
    return render_template('model.html')

# create inference route
@app.route('/inference', methods = ['POST'])
def inference():
    req = request.get_json()
    # print(req)
    s, e, v = req['score'],req['early'],req['vle']
    student = X_test.iloc[num]
    student['avg_score'] = s
    student['avg_days_sub_early'] = e
    student['sum_days_vle_accessed'] = v
    student = np.array(student)
    student = student.reshape(1, -1)
    student = list(student)
    prediction = round(rf_model.predict_proba(student)[0][0], 4)
    # print(prediction)
    return jsonify({'s':s,'e':e,'v':v,'prediction':prediction})

# create route for plotting
@app.route('/plot', methods = ['GET'])
def plot():
    df = pd.read_csv('../data/processed/transformed_data_with_features_for_eda.csv')
    data = list(zip(df.avg_score, df.svg_days_sub_early, df.sum_days_vle_accessed))
    return jsonify(data)

if __name__ == '__main__':
    app.run(app.run(host ='0.0.0.0', port = 3333, debug = True))
    # app.run(app.run(host ='0.0.0.0', port = 3333)