import requests
import sys

url = "http://127.0.0.1:5000/predictdata"
data = {
    "step": "1",
    "type": "CASH_OUT",
    "amount": "1000",
    "oldbalanceOrg": "1000",
    "newbalanceOrig": "0",
    "oldbalanceDest": "0",
    "newbalanceDest": "1000"
}

try:
    print(f"Sending POST request to {url}...")
    response = requests.post(url, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text (first 500 chars): {response.text[:500]}")
except Exception as e:
    print(f"Request failed: {e}")
