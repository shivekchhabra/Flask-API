from flask import Flask, request
import pandas as pd
import pickle
from flasgger import Swagger

## Overview:
# This code uses flasgger to render a web UI
# checkout the URL + /apidocs

app = Flask(__name__)
Swagger(app)
pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)


@app.route('/')
def welcome_msg():
    return "Welcome"


@app.route('/predict')
def predict_note_authentication():
    # There are 4 features.

    """
    Testing Notes...
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true

    responses:
        200:
            description: The output value
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = model.predict([[variance, skewness, curtosis, entropy]])

    # It will render results on:  http://127.0.0.1:5000/predict?variance=2&skewness=3&curtosis=2&entropy=1
    return 'The predicted value is {}'.format(prediction)


@app.route('/predict_file', methods=['POST'])
def predict_file():
    """
        Testing Notes...
        ---
        parameters:
          - name: file
            in: formData
            type: file
            required: true

        responses:
            200:
                description: The output values

    """
    df = pd.read_csv(request.files.get('file'))
    pred = model.predict(df)
    return 'The predicted values are {}'.format(list(pred))


if __name__ == '__main__':
    app.run()
