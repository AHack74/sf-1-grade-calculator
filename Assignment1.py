num_of_labs = input("Enter the number of labs completed: ")
num_of_quiz = input("Enter the number of quizzes completed: ")
assignment_1 = input("Enter grade for Assignment 1: ")
assignment_2 = input("Enter grade for Assignment 2: ")
assignment_3 = input("Enter grade for Assignment 3: ")
assignment_4 = input("Enter grade for Assignemnt 4: ")
midterm_1 = input("Enter grade for Midterm 1: ")
midterm_2 = input("Enter grade for Midterm 2: ")
final_exam = input("Enter grade for Final Exam: ")
midterm_final_prep = input("Enter grade for Midterm and Final Preparation: ")

if (num_of_labs >= 6):
	labs = 100 * 0.2
else (num_of_labs < 6): 
	labs = (num_of_labs/6) * 0.2
if (num_of_quiz >= 6):
	quiz = 100 * 0.15
else (num_of_quiz < 6):
	quiz = (num_of_quiz/6) * 0.15
assignments = (assignment_1 + assignment_2 + assignment_3 + assignment_4) / 4 * 0.16
midterms = (midterm_1 + midterm_2) / 2 * 0.25 
final = final_exam * 0.18
mfp = midterm_final_prep * 0.06

grade = labs + quiz + assignments + midterms + final + mfp 
print("Your grade is: "grade) 
