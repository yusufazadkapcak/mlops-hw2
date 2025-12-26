import requests
import time
import sys

url = "http://localhost:5000/health"

print("Smoke test is starting...")

for i in range(10):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Smoke Test PASSED! Service is healthy.")
            sys.exit(0)
    except requests.exceptions.ConnectionError:
        print(f"Connection is trying... ({i+1}/10)")
        time.sleep(2)

print("Smoke Test FAILED! Service unreachable.")
sys.exit(1)