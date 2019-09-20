import sys

students_list = []

def enterStudent():
    first_name = str(input("Enter the student's first name : "))
    last_name = str(input("Enter the student's last name :"))
    students_list.append({"first_name": first_name, "last_name": last_name, "grades": []})
    
    print(students_list)


def removeStudent():
    print(students_list)
    if len(students_list) != 0:
        remove_student = str(input("Enter the name to remove : "))
        for student in students_list:
            if student["first_name"] == remove_student or student["last_name"] == remove_student:
                for i in range(len(students_list)):
                    if students_list[i]["first_name"] == remove_student or students_list[i]["last_name"] == remove_student:
                        del students_list[i]
                        print('removed match')
                        print(students_list)
                        break

def addGrades(*grades):
    print(students_list)
    name_to_grade = str(input("Enter the student's name for grade input :"))
    for student in students_list:
         if student["first_name"] == name_to_grade or student["last_name"] == name_to_grade:
                for i in range(len(students_list)):
                    if students_list[i]["first_name"] == name_to_grade or students_list[i]["last_name"] == name_to_grade:
                        print(len(students_list[i]['grades']))
                        grade_input = int(input("Enter a grade for {} : ".format(name_to_grade)))
                        if len(students_list[i]['grades']) == 0:
                            students_list[i]["grades"] = [grade_input,]
                        elif len(students_list[i]['grades']) >= 1:
                            idx = len(students_list[i]['grades'])
                            print(idx)
                            print(students_list[i]['grades'][idx-1])
                            print(students_list[i]['grades'])
                            students_list[i]['grades'].append(grade_input)
                
                        print(students_list)

def studentReport():
    print(students_list)
    for i in range(len(students_list)):
        for j in range(0, len(students_list[i]['grades'])):
            print(students_list[i]['grades'][j])
    

def menu():
    print()
    print()
    print("*********************MAIN MENU*********************")
    print()
    print()

    choice = input("""
                      A: Enter Student 
                      B: Remove Student
                      C: Add Student Grades
                      D: Student Report Card
                      Q: Quit/Log Out

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        enterStudent()
    elif choice == "B" or choice =="b":
        removeStudent()
    elif choice == "C" or choice =="c":
        addGrades()
    elif choice=="D" or choice=="d":
        studentReport()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")

menu()