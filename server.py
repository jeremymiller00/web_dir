from flask import Flask, render_template, request, jsonify, Response
import pickle

app = Flask(__name__)

@app.route('/', methods = ['GET'])
@app.route('/index')

def home():
    return '<p> Hello you </p>'

if __name__ == '__main__':
    app.run(app.run(host ='0.0.0.0', port = 3333, debug = True))
