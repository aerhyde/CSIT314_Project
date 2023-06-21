import tkinter as tk
from tkinter import messagebox 
import time

class ExamApp:  
    def __init__(self):  
        self.window = tk.Tk()
        self.window.title("iLearn")
        self.window.geometry("1000x700")
        self.window.configure(bg="#F0F5F9")
        title_label = tk.Label(self.window, text="iLearn", 
                               font=("Arial", 36, "bold"), 
                               bg="#F0F5F9", 
                               fg="#1F2937")
        title_label.pack(pady=40)
        self.exams = {
            "Biology": [
                {
                    "question": "What is the powerhouse of the cell?",
                    "options": ["1. Nucleus", "2. Golgi Apparatus", "3. Mitochondria"],
                    "correct_answer": "Mitochondria"
                },
                {
                    "question": "What is the largest organ in the human body?",
                    "options": ["1. Brain", "2. Liver", "3. Skin"],
                    "correct_answer": "Skin"
                },
                {
                    "question": "A group of similar cells that come together to perform a specific function is a/an?",
                    "options": ["1. Tissue", "2. Organ", "3. Organism"],
                    "correct_answer": "Tissue"
                }
            ],
            "Physics": [
                {
                    "question": "What is the SI unit of force?",
                    "options": ["Joule", "Watt", "Newton"],
                    "correct_answer": "Newton"
                },
                {
                    "question": "What is the formula to calculate acceleration?",
                    "options": ["Force / Mass", "Mass / Distance", "Force / Time"],
                    "correct_answer": "Force / Mass"
                },
                {
                    "question": "Meters are used to describe?",
                    "options": ["Displacement", "Position", "Motion"],
                    "correct_answer": "Position"
                }
            ],
            "Math": [
                {
                    "question": "What is the value of π (pi) to two decimal places?",
                    "options": ["3.14", "2.71", "1.61"],
                    "correct_answer": "3.14"
                },
                {
                    "question": "What is the Pythagorean theorem?",
                    "options": [
                        "a^2 + b^2 = c^2",
                        "e = mc^2",
                        "F = ma"
                    ],
                    "correct_answer": "a^2 + b^2 = c^2"
                },
                {
                    "question": "Certain words in a story problem will give you clues on what operation to use. "
                                " What operation should you use when you see the word equal pieces ?",
                    "options": ["Addition", "Subtraction", "Division"],
                    "correct_answer": "Division"
                }
            ]
        }

        self.answers = []
        self.exam_history = []
        self.current_question = 0
        self.selected_exam = None
        self.start_time = None
        self.setup_widgets()

    def setup_widgets(self):
        self.exam_label = tk.Label(self.window, text="Select an Exam", font=("Times New Roman", 18, "bold"),
                                   bg="black",
                                   fg="white")
        
        self.exam_label.pack(pady=10)

        self.exam_var = tk.StringVar()
        self.exam_var.set("")
        self.exam_menu = tk.OptionMenu(self.window, self.exam_var, *self.exams.keys())
        self.exam_menu.config(font=("Arial", 12), bg="#F0F5F9")
        self.exam_menu.pack(pady=5)

        self.start_button = tk.Button(self.window, text="Start Exam", command=self.start_exam,
                                      font=("Arial", 14, "bold"), bg="#F0F5F9", fg="#000000")
        self.start_button.pack(pady=10)

        self.question_label = tk.Label(self.window, text="Question", font=("Times New Roman", 18, "bold"), 
                                       bg="black", fg="white")
        self.question_label.pack(pady=10)

        self.options_var = tk.StringVar()
        self.options_var.set("")
        
        self.options_label = tk.Label(self.window, textvariable=self.options_var, font=("Arial", 15,"bold"), 
                                      bg="#F0F5F9")
        self.options_label.pack()

        self.answer_entry = tk.Entry(self.window, font=("Arial", 12), bg="#ffffff")
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_answer,
                                       font=("Arial", 12, "bold"), bg="#F0F5F9", fg="#000000")
        self.submit_button.pack(pady=10)

        self.review_button = tk.Button(self.window, text="Review Exam", command=self.review_exam,
                                       state=tk.DISABLED, font=("Arial", 14, "bold"), bg="#F0F5F9", 
                                       fg="#000000")
        self.review_button.pack(pady=10)

        self.take_again_button = tk.Button(self.window, text="Take Another Exam", command=self.take_another_exam,
                                           state=tk.DISABLED, font=("Arial", 14, "bold"), bg="#F0F5F9", 
                                           fg="#000000")
        self.take_again_button.pack(pady=10)

        self.history_button = tk.Button(self.window, text="Review Exam History", command=self.review_exam_history,
                                        font=("Arial", 14, "bold"), bg="#F0F5F9", fg="#000000")
        self.history_button.pack(pady=10)


    def start_exam(self):
        self.selected_exam = self.exam_var.get()
        if self.selected_exam:
            self.exam_label.pack_forget()
            self.exam_menu.pack_forget()
            self.start_button.pack_forget()
            self.display_question()
            self.start_time = time.time()
        else:
            messagebox.showwarning("No Exam Selected", "Please select an exam to start.")

    def display_question(self):
        question = self.exams[self.selected_exam][self.current_question]
        self.question_label.config(text=question["question"])
        self.options_var.set("\n".join(question["options"]))


    def submit_answer(self):
        answer = self.answer_entry.get()
        self.answers.append(answer)

        if self.current_question < len(self.exams[self.selected_exam]) - 1:
            self.current_question += 1
            self.display_question()
            self.answer_entry.delete(0, tk.END)
        else:
            self.calculate_grade()
            self.review_button.config(state=tk.NORMAL)
            self.take_again_button.config(state=tk.NORMAL)

    def calculate_grade(self):
        total_questions = len(self.exams[self.selected_exam])
        correct_answers = 0

        for i, question in enumerate(self.exams[self.selected_exam]):
            if self.answers[i].lower() == question["correct_answer"].lower():
                correct_answers += 1

        percentage = (correct_answers / total_questions) * 100
        letter_grade = self.get_letter_grade(percentage)

        elapsed_time = time.time() - self.start_time

        self.exam_history.append({
            "exam": self.selected_exam,
            "grade": percentage,
            "letter_grade": letter_grade,
            "time_taken": elapsed_time,
            "answers": self.answers.copy()
        })

        messagebox.showinfo("Grade", f"You scored {percentage:.2f}% ({letter_grade})\n"
                                      f"Elapsed Time: {elapsed_time:.2f} seconds")

    def get_letter_grade(self, percentage):
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "F"

    def review_exam(self):
        review_text = ""

        for i, question in enumerate(self.exams[self.selected_exam]):
            user_answer = self.answers[i]
            correct_answer = question["correct_answer"]
            review_text += f"Q{i+1}: Your answer: {user_answer}, Correct answer: {correct_answer}\n"

        messagebox.showinfo("Exam Review", review_text)

    def take_another_exam(self):
        self.current_question = 0
        self.answers = []
        self.review_button.config(state=tk.DISABLED)
        self.take_again_button.config(state=tk.DISABLED)
        self.selected_exam = None
        self.exam_label.pack()
        self.exam_menu.pack()
        self.start_button.pack()

    def review_exam_history(self):
        if not self.exam_history:
            messagebox.showinfo("Exam History", "No exam history available.")
        else:
            review_text = ""
            for i, exam in enumerate(self.exam_history):
                exam_number = i + 1
                exam_name = exam["exam"]
                grade = exam["grade"]
                letter_grade = exam["letter_grade"]
                time_taken = exam["time_taken"]
                review_text += f"Exam {exam_number}: {exam_name}\n"
                review_text += f"Grade: {grade:.2f}% ({letter_grade})\n"
                review_text += f"Time Taken: {time_taken:.2f} seconds\n"
                review_text += f"Answers:\n"
                for j, answer in enumerate(exam["answers"]):
                    review_text += f"Q{j+1}: {answer}\n"
                review_text += "\n"

            messagebox.showinfo("Exam History", review_text)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ExamApp()
    app.run()



