import requests

parameters = {
    "amount": 10,     # number of questions
    "type": "boolean" # True/False format
}

url = "https://opentdb.com/api.php"

try:
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    data = response.json()
    question_data = data["results"]
except requests.RequestException as e:
    print("Error fetching quiz data:", e)
    question_data = []
