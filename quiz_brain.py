import html

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0 
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        length_question_list = len(self.question_list)        
        return self.question_number < length_question_list
    
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {question_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
      