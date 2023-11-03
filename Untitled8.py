#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.question_index = 0
        self.score = 0

        self.questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
            {"question": "What is 2 + 2?", "answer": "4"},
        ]

        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(root, font=("Arial", 12))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 12))
        self.submit_button.pack()

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.question_index]["question"])
            self.answer_entry.delete(0, tk.END)
            self.feedback_label.config(text="")
        else:
            self.question_label.config(text="Quiz Over!")
            self.answer_entry.config(state=tk.DISABLED)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        correct_answer = self.questions[self.question_index]["answer"]

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.feedback_label.config(text="Correct!")
        else:
            self.feedback_label.config(text=f"Wrong! The correct answer is {correct_answer}")

        self.question_index += 1
        self.next_question()


root = tk.Tk()
app = QuizApp(root)
root.mainloop()


# In[ ]:




