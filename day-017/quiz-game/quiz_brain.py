class QuizBrain:

    def __init__(self, question_list):
        self.current_index = 0
        self.score = 0
        self.question_list = question_list

    def is_last_question(self):
        return self.current_index >= len(self.question_list)

    def next_question(self):
        if len(self.question_list) <= self.current_index:
            self.current_index = 0

        if len(self.question_list) > 0:
            question = self.question_list[self.current_index]
            self.current_index += 1
            return question, self.format_question(question)

    def format_question(self, q):
        return f"Q.{self.current_index}: {q.question} (True/False)? "

    def check_answer_score(self, question, answer):
        correct = question.is_correct(answer)
        if correct:
            self.score += 1
        return (f"'{answer}' answer is {"correct" if correct else "incorrect"}"
                f"\nThe correct answer is {self.get_answer(question)}"
                f"\nCurrent score: {self.score}/{self.current_index}"
                "\n")

    def get_score(self):
        return f"{self.score}/{self.current_index}"

    @staticmethod
    def get_answer(question):
        return question.answers[0]
