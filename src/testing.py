import requests

BASE = "http://127.0.0.1:5000/"
response = requests.get(BASE + "api/routes/216.218.252.28")
print(response)