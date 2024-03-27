import requests

from question_model import Question

API_ENDPOINT = "https://opentdb.com/api.php"

params = {
    "amount": 10,
    "type": "boolean",
}
response = requests.get(API_ENDPOINT, params)
response.raise_for_status()
data = response.json()
question_data = data["results"]
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
