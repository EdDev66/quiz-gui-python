from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = 'Quizzler'
        self.score = 0
        self.create_ui()
        self.get_next_question()

        self.window.mainloop()

    def check_answer(self, answer):
        correct_answer = self.quiz.check_answer(answer)

        if correct_answer == True:
            self.score += 1
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, lambda: self.canvas.config(bg='white'))

        # next_question = self.quiz.next_question()
        # self.window.after(1000, lambda: self.canvas.itemconfig(self.question_text, text=next_question))
        self.window.after(1000, lambda: self.get_next_question)

    def create_ui(self):
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lbl = Label(text=f'Score: {self.score}', fg='white', bg=THEME_COLOR)
        self.score_lbl.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question text!", fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_img = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=lambda: self.check_answer('True'))
        self.true_btn.grid(column=0, row=2)

        self.false_img = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=lambda: self.check_answer('False'))
        self.false_btn.grid(column=1, row=2)

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_lbl.config(text=f'Score: {self.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz!')
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')