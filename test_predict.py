import requests

url = "http://15.236.208.93:5000/predict"

data = {
    "feature1": 0.5,
    "feature2": 1.2,
    "feature3": 3.8,
    "feature4": 0.7  # si ton modèle attend une 4e feature par exemple
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())
