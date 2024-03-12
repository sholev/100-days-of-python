class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answers = [answer]
        self.is_case_sensitive = False

    def add_answer(self, answer):
        self.answers.append(answer)

    def is_correct(self, answer):
        if self.is_case_sensitive:
            return answer in self.answers
        else:
            return answer.lower() in (a.lower() for a in self.answers)
