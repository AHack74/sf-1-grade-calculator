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

if int(num_of_labs) >= 6:
	labs = 100 * 0.2
else: 
	labs = int(num_of_labs)/6 * 100 * 0.2
if int(num_of_quiz) >= 6:
	quiz = 100 * 0.15
else:
	quiz = int(num_of_quiz)/6 * 100 * 0.15

assignments = (int(assignment_1) +int(assignment_2) + int(assignment_3) + int(assignment_4)) / 4 * 0.16
midterms = (int(midterm_1) + int(midterm_2)) / 2 * 0.25 
final = int(final_exam) * 0.18
mfp = int(midterm_final_prep) * 0.06

grade = labs + quiz + assignments + midterms + final + mfp 
print("Your grade is: " + str(round(grade, 0))) 
