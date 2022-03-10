class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def is_question_left(self):
        #   if len(self.question_list) > self.question_number:
        #         return True
        #     return False
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False)")
