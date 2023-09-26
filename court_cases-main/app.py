# import streamlit as st
# import numpy as np
# import pickle
# import math

# def load_model():
#     with open('cases.sav','rb') as file:
#         model = pickle.load(file)
#     return model

# st.header('Court Hearing Prediction System')

# # Input features from the user
# num_advocates = st.slider('Number of Advocates',0, 50, 2)
# num_issues = st.slider('Number of Issues', 0, 50, 3)
# num_laws = st.slider('Number of Laws', 0, 50, 3)
# num_precedents = st.slider('Number of Precedents', 0, 50, 1)


# def classify_complexity(val):
#     st.write('Case Complexity',val)
#     if val > 6.0:
#         st.write('Case Classification: Hard')
#     elif val < 4.0 :
#         st.write('Case Classification: Standard')
#     else:
#         st.write('Case Classification: Intermediate')
    
# # Define the function to classify case complexity
# def classify_case_complexity(issues, precedents, laws): 
#     complexity = issues + precedents + laws
#     # std_dev = 1.005
#     # mean_val = 2.775
#     min_val  = 1
#     max_val = 73
#     # standardized_complexity = (complexity - mean_val) / std_dev
#     new_complexity = ((complexity - min_val)*6) / (max_val-min_val)
#     classify_complexity(new_complexity)
#     # classify_complexity(standardized_complexity)

# # Predict the case complexity based on the input
# model = load_model()
# input_data = np.array([num_advocates, num_issues, num_laws, num_precedents]).reshape(1, -1)
# prediction = model.predict(input_data)[0]

# if st.button('Predict'):
#     st.write('Predicted No. of Hearings:', math.ceil(prediction))
#     #case complexity
#     classify_case_complexity(num_issues,num_laws,num_precedents)
    
      
import streamlit as st
import numpy as np
import pickle
import math
import json

def load_model():
    with open('cases.sav','rb') as file:
        model = pickle.load(file)
    return model

st.header('Court Hearing Prediction System')

# Input features from the user
num_advocates = st.slider('Number of Advocates',0, 50, 2)
num_issues = st.slider('Number of Issues', 0, 50, 3)
num_laws = st.slider('Number of Laws', 0, 50, 3)
num_precedents = st.slider('Number of Precedents', 0, 50, 1)

# Create a dictionary to store input and output parameters
result = {
    'input': {
        'num_advocates': num_advocates,
        'num_issues': num_issues,
        'num_laws': num_laws,
        'num_precedents': num_precedents
    }
}

def classify_complexity(val):
    if val > 6.0:
        return 'Hard'
    elif val < 4.0 :
        return 'Standard'
    else:
        return 'Intermediate'

# Define the function to classify case complexity
def classify_case_complexity(issues, precedents, laws): 
    complexity = issues + precedents + laws
    min_val  = 1
    max_val = 73
    new_complexity = ((complexity - min_val) * 6) / (max_val - min_val)
    complexity_class = classify_complexity(new_complexity)
    return new_complexity, complexity_class

# Predict the case complexity based on the input
model = load_model()
input_data = np.array([num_advocates, num_issues, num_laws, num_precedents]).reshape(1, -1)
prediction = math.ceil(model.predict(input_data)[0])

if st.button('Predict'):
    st.write('Predicted No. of Hearings:', prediction)
    # Calculate case complexity
    complexity_value, complexity_class = classify_case_complexity(num_issues, num_laws, num_precedents)
    st.write('Case Complexity:', complexity_class)
    
    # Append output parameters to the result dictionary
    result['output'] = {
        'predicted_no_of_hearings': prediction,
        'case_complexity': complexity_class,
        'complexity_value': complexity_value
    }
    
    # Use st.json() to display the JSON data
    st.json(result)
