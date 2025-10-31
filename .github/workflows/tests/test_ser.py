import requests

url = "https://ser-mvp.replit.app/ser"
data = {"nodes": [{"energy": 1}, {"energy": 2}], "prob": [0.5, 0.5]}

r = requests.post(url, json=data)

print("Status Code:", r.status_code)
print("Raw Response:", r.text)