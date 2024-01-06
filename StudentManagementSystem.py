def highest_maths(student_list):
    highest_score_in_maths = 0
    Name_of_the_highest_score_maths = ''
    for student in student_list:
        if (student.get("Maths") > highest_score_in_maths):
            highest_score_in_maths = student.get("Maths")
            Name_of_the_highest_score_maths = student.get("student_name")
    print(f"The highest scorer in Maths is {Name_of_the_highest_score_maths} with the {highest_score_in_maths} marks ")

def highest_Science(student_list):
    highest_score_in_Science = 0
    Name_of_the_highest_score_Science = ''
    for student in student_list:
        if (student.get("Science") > highest_score_in_Science):
            highest_score_in_Science = student.get("Science")
            Name_of_the_highest_score_Science = student.get("student_name")
    print(f"The highest scorer in Science is {highest_score_in_Science} with the {Name_of_the_highest_score_Science} marks ")

def highest_Sost(student_list):
    highest_score_in_Sost = 0
    Name_of_the_highest_score_Sost = ''
    for student in student_list:
        if (student.get("Sost") > highest_score_in_Sost):
            highest_score_in_Sost = student.get("Sost")
            Name_of_the_highest_score_Sost = student.get("student_name")
    print(f"The highest scorer in Sost is {Name_of_the_highest_score_Sost} with the {highest_score_in_Sost} marks ")

Student_1 = {
    "Maths": 45,
    "Sost": 75,
    "Science": 96,
    "student_name": "Tanmay"
}
Student_2 = {
    "Maths": 74,
    "Sost": 83,
    "Science": 100,
    "student_name": "Dhiraj"
}
Student_3 = {
    "Maths": 98,
    "Sost": 92,
    "Science": 23,
    "student_name": "Suraj"
}

student_list = [Student_1, Student_2, Student_3]

highest_maths(student_list)
highest_Science(student_list)
highest_Sost(student_list)

