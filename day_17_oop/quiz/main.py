#!/usr/bin/env python3
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question['text']
    answer = question['answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)
    #question_bank.append(Question(question['text'], question['answer']))

quiz = QuizBrain(question_bank)

while quiz.is_question_left():
    quiz.next_question()
