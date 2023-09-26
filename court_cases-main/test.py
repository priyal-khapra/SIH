import requests
import json

url = 'http://127.0.0.1:5000/predict'
data = {
    'num_advocates': 2,
    'num_issues': 3,
    'num_laws': 3,
    'num_precedents': 1
}

response = requests.post(url, json=data)
print(response.json())
