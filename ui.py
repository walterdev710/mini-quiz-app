from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=30, pady=30)
        
        self.score_label = Label(text="Score:0",font=("Arial", 15, "bold"), bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.score_label.grid(row=0, column=1, pady=20)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text =self.canvas.create_text(
            150, 
            125, 
            text='Some text here bro', 
            width=280, 
            font=("Arial", 15, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2)
        
        self.true_btn_img = PhotoImage(file="./imgs/true.png")
        self.true_btn = Button(image=self.true_btn_img, highlightthickness=0, command=self.answer_true)
        self.true_btn.grid(row=2, column=0, pady=50)
        
        self.false_btn_img = PhotoImage(file="./imgs/false.png")
        self.false_btn = Button(image=self.false_btn_img, highlightthickness=0, command=self.answer_false)
        self.false_btn.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfigure(self.question_text, fill=THEME_COLOR)
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz",fill=THEME_COLOR )
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
        
    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green", highlightthickness=0)
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.configure(bg="red", highlightthickness=0)
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)