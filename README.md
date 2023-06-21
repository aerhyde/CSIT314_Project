# CSIT314_Project
CSIT 314 Spring 2023 - Riya, Salma, Mishka, Sherif, Laith - Repository for our CSIT314 Final Project testing codes.

The following codes were written using Python, and CODE1 and CODE2 utilize pythons TKinter library to display a GUI. 

314_CODE1 :

defines the assessment functionality of iLearn, where students are given three subjects to choose from to take an exam. Once they've chosen a subject, they can choose to start their exam (where a timer also starts to record how long the student has taken) Each subject has its own respective set of questions and right answers. Based on the students entered answers and the right answer, a mark is assigned to them as they are taking the test. Once they are done answering all the questions, they get assigned a letter grade from A to F, which is displayed in a message box. Their performance and answers of past exams are recorded so students can view them within each console session. 


314_CODE2 : 

defines the subject assignment submission section access and permission control functionalities of the application. The student can select only the subjects they have access to, for this code the subject permissions for the current student is set to math and english, they will be shown an error if they try to access science. Once the access a subject, they can click on an assignment from beginner or advanced. The current student in this code is defined as a beginner, and thus cannot access the advanced assignment. Once they access an assignment, they can upload a file by browsing their pc, however they are restricted to only submitting txt files. After they choose a file, the assignment is set as submitted. The student can return and upload another file. 


314_CODE3: 

defines the login, sign up, send message and create/edit/view file functionalities of the application. A user can register themselves by simply creating a username and password, and this is stored such that when they log in, they are given access to the send message and file functionalities. Send message works by allowing the user to enter an existing user name apart from theirs (for that session) and entering a message that is sent to them. The file functionalities allow the user to enter a file name, enter file content and create a txt file on the local system. This replicates the creation of a post or similar on our application. This file can be opened and its contents can be viewed using this code, and its content can be changed using the edit functionality. 


314_CODE4: 

defines a way for parent users to view their childs information provided that this student is on the list of students that are subscribed to our applications extra perks. This gives the parent access to their information, and is a simple test of how access can be restricted by using a list that records students that have subscription add ons. 


