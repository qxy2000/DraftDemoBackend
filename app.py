import json
import os
from flask import Flask
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)

CORS(app, resources=r'/*')


@app.route('/',methods=['GET'])
def hello_world():
    #return 'Hello World! test successfully'
    return jsonify({'msg': 'Try POSTing to the /predict endpoint with an RGB image attachment'})

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file is not None:
            return jsonify({'class_id': "test", 'class_name': "test111"})


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0')
