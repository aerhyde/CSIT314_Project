import tkinter as tk
from tkinter import filedialog 

class LearningPortal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("iLearn")
        self.root.geometry("1000x400")
        self.root.configure(bg="#F0F5F9") 

        self.userPermission = "Student"
        self.levelPermission = "Beginner"
        self.subjectPermission = ["Math", "English"]

        self.message = None
        self.submitted_assignments = {}  

        self.allSubjects = ["Math", "English", "Science"]

        self.show_main_window()

    def show_main_window(self):
        self.clear_window()
        self.root.title("iLearn")
        self.message = None

        title_label = tk.Label(self.root, text="iLearn", font=("Arial", 36, "bold"), 
                               bg="#F0F5F9", fg="#1F2937")  
        title_label.pack(pady=40)

        for subject in self.allSubjects:
            subject_button = tk.Button(self.root, text=subject, font=("Arial", 14), width=20, height=2,
                                       command=lambda s=subject: self.check_subject_permission(s))  
            subject_button.pack(pady=10)

    def check_subject_permission(self, subject):
        if self.userPermission == "Student" and subject in self.subjectPermission:
            self.show_assignment_window(subject)
        else:
            self.show_error_message("You are not enrolled in this subject!")

    def show_assignment_window(self, subject):
        self.clear_window()
        self.root.title(subject)

        title_label = tk.Label(self.root, text=subject, font=("Arial", 36, "bold"), bg="#F0F5F9", fg="#1F2937")  

        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), width=10, command=self.show_main_window)  
        back_button.pack()

        assignment_button1 = tk.Button(self.root, text="Assignment 1: Beginner", font=("Arial", 14), width=25, height=2,
                                       command=lambda: self.check_level_permission(subject, "Beginner"))  
        assignment_button1.pack(pady=10)

        assignment_button2 = tk.Button(self.root, text="Assignment 2: Advanced", font=("Arial", 14), width=25, height=2,
                                       command=lambda: self.check_level_permission(subject, "Advanced"))  
        assignment_button2.pack()

    def check_level_permission(self, subject, level):
        if self.levelPermission == level:
            self.show_upload_window(subject)
        else:
            self.show_error_message("You do not have access to this assignment")

    def show_upload_window(self, subject):
        self.clear_window()
        self.root.title(subject)

        title_label = tk.Label(self.root, text=subject, font=("Arial", 36, "bold"), bg="#F0F5F9", fg="#1F2937") 
        title_label.pack(pady=40)

        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), width=10,
                                command=lambda: self.show_assignment_window(subject)) 
        back_button.pack()

        upload_button = tk.Button(self.root, text="Upload Assignment", font=("Arial", 14), width=25, height=2,
                                  command=lambda: self.upload_assignment(subject))  
        upload_button.pack()

        if self.submitted_assignments.get(subject):
            message_label = tk.Label(self.root, text="Assignment already submitted!", font=("Arial", 14), fg="green", bg="#F0F5F9")  
            message_label.pack()

    def upload_assignment(self, subject):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.submitted_assignments[subject] = True
            self.show_success_message("Assignment uploaded!")

    def show_error_message(self, message):
        self.clear_window()
        self.root.title("Error")

        message_label = tk.Label(self.root, text=message, font=("Arial", 14), fg="red", bg="#F0F5F9")  
        message_label.pack(pady=40)

        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), width=10, command=self.show_main_window) 
        back_button.pack()

    def show_success_message(self, message):
        self.clear_window()
        self.root.title("Success")

        message_label = tk.Label(self.root, text=message, font=("Arial", 14), fg="green", bg="#F0F5F9")  
        message_label.pack(pady=40)

        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), width=10, command=self.show_main_window) 
        back_button.pack()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    portal = LearningPortal()
    portal.run()
