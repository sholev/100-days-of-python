from question_model import Question
from data import question_data, open_trivia_data
from quiz_brain import QuizBrain

question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     answer_text = question["answer"]
#     question_object = Question(question_text, answer_text)
#     question_object.add_answer(answer_text[0])
#     question_bank.append(question_object)

for question in open_trivia_data:
    question_text = question["question"]
    answer_text = question["correct_answer"]
    question_object = Question(question_text, answer_text)
    question_object.add_answer(answer_text[0])
    question_bank.append(question_object)

quiz_brain = QuizBrain(question_bank)


while not quiz_brain.is_last_question():
    question_data = quiz_brain.next_question()
    user_answer = input(question_data[1])
    print(quiz_brain.check_answer_score(question_data[0], user_answer))
    if user_answer.lower() == "quit" or user_answer.lower() == "q":
        break

print(f"Quiz completed. Final score: {quiz_brain.get_score()}")
