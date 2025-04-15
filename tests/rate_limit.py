import requests
import time

URL = "http://localhost/users/"
TOTAL_REQUESTS = 20
DELAY_BETWEEN_REQUESTS = 0.1  # 100ms

for i in range(TOTAL_REQUESTS):
    response = requests.get(URL)
    print(f"{i+1:02d}: Status {response.status_code}")
    time.sleep(DELAY_BETWEEN_REQUESTS)
