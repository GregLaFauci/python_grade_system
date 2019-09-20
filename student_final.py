import sys

students_list = []

def enterStudent():
    first_name = str(input("Enter the student's first name : "))
    last_name = str(input("Enter the student's last name :"))
    students_list.append({"first_name": first_name, "last_name": last_name, "grades": [], "average": 0 })
    

def printStudentList():
    print(students_list)
    
def removeStudent():
    if len(students_list) != 0:
        remove_student = str(input("Enter the name to remove : "))
        for student in students_list:
            if student["first_name"] == remove_student or student["last_name"] == remove_student:
                for i in range(len(students_list)):
                    if students_list[i]["first_name"] == remove_student or students_list[i]["last_name"] == remove_student:
                        del students_list[i]
                        print('removed match')
                        break

def addGrades(*grades):
    name_to_grade = str(input("Enter the student's name for grade input :"))
    for student in students_list:
         if student["first_name"] == name_to_grade or student["last_name"] == name_to_grade:
                for i in range(len(students_list)):
                    if students_list[i]["first_name"] == name_to_grade or students_list[i]["last_name"] == name_to_grade:
                        grade_input = int(input("Enter a grade for {} : ".format(name_to_grade)))
                        if len(students_list[i]['grades']) == 0:
                            students_list[i]["grades"] = [grade_input,]
                            Sum = sum(students_list[i]['grades'])
                            students_list[i]['average'] = Sum
                        elif len(students_list[i]['grades']) >= 1:
                            # idx = len(students_list[i]['grades'])
                            students_list[i]['grades'].append(grade_input)
                            Sum = sum(students_list[i]['grades'])
                            avg = Sum / len(students_list[i]['grades'])
                            students_list[i]['average'] = avg
                

def avgGrade():
    for student in students_lists: 
        for i in range(len(students_list)):
            Sum = sum(students_list[i]['grades'])
        if len(students_list[i]['grades']) > 0:
            avg = Sum / len(students_list[i]['grades'])
        students_list[i]['average'].append(avg)
        

                    
                    
def studentReport():
    for student in students_list:
        for i in range(len(students_list)):
            print(" {} {} grades: {} final average: {}".format(student["first_name"], student["last_name"], student["grades"], student["average"]))
        
            
    

def menu():
    print()
    print()
    print("        *********************MAIN MENU*********************         ")
    print()
    print()

    choice = input("""
                      1: Enter Student        
                      2: Remove Student       
                      3: Add Student Grades   
                      4: Student Report Card
                      5: Print Student List 
                      Q: Quit/Log Out

                      Please enter your choice: \n\n """)

    if choice == "1":
        enterStudent()
    elif choice == "2":
        removeStudent()
    elif choice == "3":
        addGrades()
    elif choice=="4":
        studentReport()
    elif choice=="5":
        printStudentList()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select 1,2,3,4,5 or Q")
        print("Please try again")

menu()