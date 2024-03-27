from ui import QuizUi
from quiz_brain import QuizBrain
from data import question_bank

quiz = QuizBrain(question_bank)
quiz_ui = QuizUi(quiz)
