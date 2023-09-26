from flask import Flask, request, jsonify
import pickle
import numpy as np
import math

app = Flask(__name__)

# Load your machine learning model
with open('cases.sav', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    num_advocates = data['num_advocates']
    num_issues = data['num_issues']
    num_laws = data['num_laws']
    num_precedents = data['num_precedents']

    # Perform any necessary data preprocessing
    # ...

    # Make predictions using your model
    input_data = np.array([num_advocates, num_issues, num_laws, num_precedents]).reshape(1, -1)
    prediction = math.ceil(model.predict(input_data)[0])

    response = {
        'predicted_no_of_hearings': prediction
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
