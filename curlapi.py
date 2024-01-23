import requests

base_url = "http://api.cpdevsecops.net/api"

def call_get_api(endpoint, params=None):
    url = f"{base_url}{endpoint}"
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(f"GET {url} - Success")
    else:
        print(f"GET {url} - Error: Status code {response.status_code}")

def call_post_api(endpoint, body):
    url = f"{base_url}{endpoint}"
    response = requests.post(url, data=body)
    if response.status_code == 200:
        print(f"POST {url} - Success")
    else:
        print(f"POST {url} - Error: Status code {response.status_code}")

endpoints = [
    ("/sessions", None),
    ("/session/{id}", {"id": 123}),
    ("/session/{id}/topics", {"id": 123}),
    ("/speakers", None),
    ("/speaker/{id}", {"id": 456}),
    ("/speaker/{id}/sessions", {"id": 456}),
    ("/speaker/{id}/topics", {"id": 456}),
    ("/topics", None),
    ("/topic/{id}", {"id": 789}),
    ("/topic/{id}/speakers", {"id": 789}),
    ("/topic/{id}/sessions", {"id": 789}),
]

number_of_executions = 2500

for _ in range(number_of_executions):
    for endpoint, params in endpoints:
        call_get_api(endpoint, params)

    call_post_api('/session/{id}/feedback', {"id": 123, "body": "Your feedback here"})
