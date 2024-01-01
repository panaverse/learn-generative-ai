import requests

r = requests.get("localhost:8000/agent")
print(r.status_code, r.headers)