from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    usr_question = Question(question_text, question_answer)
    question_bank.append(usr_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

