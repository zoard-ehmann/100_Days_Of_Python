import tkinter as tk
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 16, "italic")
PADDING = 30


class QuizInterface():
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=PADDING, pady=PADDING)
        
        self.scoreboard = tk.Label(bg=THEME_COLOR, fg="white")
        self.scoreboard.grid(row=0, column=1)
        
        self.question_box = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0, bd=0)
        self.question_text = self.question_box.create_text(150, 125, font=FONT, fill=THEME_COLOR, width=275)
        self.question_box.grid(row=1, column=0, columnspan=2, pady=PADDING)
        
        false_image = tk.PhotoImage(file="Day34/Quizzler/images/false.png")
        self.false_btn = tk.Button(image=false_image, highlightthickness=0, bd=0, command=self.is_false)
        self.false_btn.grid(row=2, column=0)
        
        true_image = tk.PhotoImage(file="Day34/Quizzler/images/true.png")
        self.true_btn = tk.Button(image=true_image, highlightthickness=0, bd=0, command=self.is_true)
        self.true_btn.grid(row=2, column=1)
        
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        self.set_qbox_color("white")
        if self.quiz.still_has_questions():
            self.false_btn.config(state="normal")
            self.true_btn.config(state="normal")
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_box.itemconfig(self.question_text, text=q_text)
        else:
            self.question_box.itemconfig(self.question_text, text="Well done! You've reached the end of the quiz.")
        
    def is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def give_feedback(self, is_correct):
        if is_correct:
            self.set_qbox_color("green")
        else:
            self.set_qbox_color("red")
        self.false_btn.config(state="disabled")
        self.true_btn.config(state="disabled")
        self.window.after(1000, self.get_next_question)
            
    def set_qbox_color(self, color: str):
        self.question_box.config(bg=color)