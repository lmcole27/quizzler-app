from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(height=1200, width=1000, pady=50, padx=50, bg=THEME_COLOR)
        self.score = Label(text="Score: 0", background=THEME_COLOR, font=("Arial", 16, "normal"), foreground="white")
        self.score.grid(row=0, column=1, columnspan=1)
        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280, justify="center",
            text="question text goes here",
            font=("Arial", 20, "italic"), fill=THEME_COLOR,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.incorrect_image = PhotoImage(file="images/false.png")
        self.incorrect_button = Button(
            image=self.incorrect_image,
            highlightthickness=0, padx=100, pady=100,
            command=self.user_false)
        self.incorrect_button.grid(row=2, column=1)
        self.correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(
            image=self.correct_image,
            highlightthickness=0, padx=100, pady=100,
            command=self.user_true
        )
        self.correct_button.grid(row=2, column=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Thanks for playing!")
            self.incorrect_button.config(state="disabled")
            self.correct_button.config(state="disabled")

    def user_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def user_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, response):
        is_right = response[0]
        score = response[1]
        asked_questions = response[2]
        if is_right:
            self.canvas.config(bg="green")
            self.score.config(text=f"Score: {score} / {asked_questions}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, lambda: self.get_next_question())
