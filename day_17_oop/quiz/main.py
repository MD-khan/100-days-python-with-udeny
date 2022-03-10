#!/usr/bin/env python3
from question_model import Question
from data import general_data, science_questions, film_data

from quiz_brain import QuizBrain

# # Ask user to subject of the quiz
# quiz_subject = input(
#     f"Please type your interested subject: science/general/film: ").lower()
# if quiz_subject == "science":
#     quiz_subject = science_questions
# elif quiz_subject == "general":
#     quiz_subject = general_data
# elif quiz_subject == "film":
#     quiz_subject == film_data

question_bank = []
for question in science_questions:
    text = question['question']
    answer = question['correct_answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)
    #question_bank.append(Question(question['text'], question['answer']))

quiz = QuizBrain(question_bank)

while quiz.is_question_left():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
