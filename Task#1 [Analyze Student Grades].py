import os
import pandas as pd

Student = {
    'Student Name': ['Robert','William','Rebecca','Shakespear','Evans','Johanna'],
    'Math' : [89,67,97,88.5,80,91.5],
    'English' : [77.5,95,90,99.5,92,87],
    'Science' : [90,78.5,85.5,68,79,82]
}
Student_Grade = pd.DataFrame(Student)                               # Creating Data Frame
Student_Grade.to_csv("Students_Grade.csv",index = False)            # Creating a .csv(Comma-Separated Value) file

#===========================================================================================================================================
#===========================================================================================================================================
#===========================================================================================================================================

Student_Grade = pd.read_csv('Students_Grade.csv')                                                          # Reading the file

Student_Grade["Average"] = Student_Grade[["Math", "English", "Science"]].mean(axis=1)                      # Calculate average score for each student
Student_Grade["Percentage"] = Student_Grade[["Math", "English", "Science"]].sum(axis=1) / (3 * 100) * 100  # Calculate percentage score for each student

top_student = Student_Grade.loc[[Student_Grade["Average"].idxmax()]]                                       # Find the student with the highest average
lowest_student = Student_Grade.loc[[Student_Grade["Average"].idxmin()]]                                    # Find the student with the lowest average


Math_top_index = Student_Grade["Math"].idxmax()
Math_top_student = Student_Grade.loc[Math_top_index,"Student Name"]
Math_top_marks = Student_Grade.loc[Math_top_index,"Math"]

Science_top_index = Student_Grade["Science"].idxmax()
Science_top_student = Student_Grade.loc[Science_top_index,"Student Name"]
Science_top_marks = Student_Grade.loc[Science_top_index,"Science"]

English_top_index = Student_Grade["English"].idxmax()
English_top_student = Student_Grade.loc[English_top_index,"Student Name"]
English_top_marks = Student_Grade.loc[English_top_index,"English"]

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

Student_Grade['Grade'] = Student_Grade["Percentage"].apply(grade)

print("All Students:\n", Student_Grade)
print("\nTop Average Marks Student:\n", top_student)                                        # Student with the highest average
print("\nLowest Average Marks Student:\n", lowest_student)                                  # Student with the lowest average

print(f"\n{Math_top_student} has highest marks in Math: {Math_top_marks}")                  # Student with highest marks in Math
print(f"\n{Science_top_student} has highest marks in Science: {Science_top_marks}")         # Student with highest marks in Science
print(f"\n{English_top_student} has highest marks in English: {English_top_marks}")         # Student with highest marks in English