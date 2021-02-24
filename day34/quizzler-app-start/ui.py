from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)

        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0, padx=20, pady=20)

        self.canvas = Canvas(bg="white", width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Hi",
            font=FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        right_image = PhotoImage(file="images/true.png")
        wring_image = PhotoImage(file="images/false.png")
        self.right = Button(image=right_image, highlightthickness=0, bg=THEME_COLOR, command=self.correct_answer)
        self.wrong = Button(image=wring_image, highlightthickness=0, bg=THEME_COLOR, command=self.wrong_answer)
        self.right.grid(column=0, row=2, padx=20, pady=20)
        self.wrong.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Well done on completing the quiz!")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def correct_answer(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def wrong_answer(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


