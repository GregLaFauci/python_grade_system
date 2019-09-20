import sys 

# to do list: 
    # what if multiple students have the same first or last name?
    # add validations to inputs
    # if first_name match: addGrade() loops through 4 times FIX


students_list = []

def enterStudent():
    first_name = str(input("Enter the student's first name : "))
    last_name = str(input("Enter the student's last name :"))
    students_list.append({"first_name": first_name, "last_name": last_name, "grades": [], "average": 0 })

    # use Regex to validate first_name and last_name
    # either try to create a match pattern, or a list of excluded chars
    

def printStudentList():
    print(students_list)


# def searchStudentList():
    '''def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return None'''

    
def removeStudent():
    if len(students_list) != 0:
        print("This action cannot be undone.")
        remove_student = str(input("Enter the name to remove : "))
        
        for student in students_list:
            if student["first_name"] == remove_student or student["last_name"] == remove_student:
                for i in range(len(students_list)):
                    if students_list[i]["first_name"] == remove_student or students_list[i]["last_name"] == remove_student:
                        del students_list[i]
                        print('removed match')
                        break
                    else:
                        print('no match found')

                        
def addGrades():
    name_to_grade = str(input("Enter the student's name for grade input :"))
    for student in students_list:
         if student["first_name"] == name_to_grade or student["last_name"] == name_to_grade:
                for i in range(len(students_list)):
                    if students_list[i]["first_name"] == name_to_grade or students_list[i]["last_name"] == name_to_grade:
                        grade_input = int(input("Enter a grade for {} : ".format(name_to_grade)))
                        if grade_input < 0:
                            print("Please reenter a positive number: ")
                            addGrades()
                        if grade_input > 100:
                            print("Please reenter a number in the range 1 - 100 : ")
                            addGrades()
                        else:
                            if len(students_list[i]['grades']) == 0:
                                students_list[i]["grades"] = [grade_input,]
                                Sum = sum(students_list[i]['grades'])
                                students_list[i]['average'] = Sum
                                break
                            elif len(students_list[i]['grades']) >= 1:
                                students_list[i]['grades'].append(grade_input)
                                Sum = sum(students_list[i]['grades'])
                                avg = Sum / len(students_list[i]['grades'])
                                students_list[i]['average'] = avg
                                break
                

def studentReport():
    for student in students_list:
        print(" {} {} grades: {} final average: {}".format(student["first_name"], student["last_name"], ', '.join(map(str, student["grades"])), student["average"]))        
        
            
def print_menu():
    print()
    print()
    print("                        ********MAIN MENU**********                 ")
    print("""
                      1: Enter Student        
                      2: Remove Student       
                      3: Add Student Grades   
                      4: Student Report Card
                      5: Print Student List 
                      6: Exit

                      Please enter your choice: \n\n """)
    


# start it up:    
print_menu()
# keep it going:
menu_choice = 0
while menu_choice != 6:
    print()
    menu_choice = int(input("Menu Choice (1-6): "))
    if menu_choice == 1:
        enterStudent()
        print_menu()
    elif menu_choice == 2:
        removeStudent()
        print_menu()
    elif menu_choice == 3:
        addGrades()
        print_menu()
    elif menu_choice == 4:
        studentReport()
        print_menu()
    elif menu_choice == 5:
        printStudentList()
        print_menu()


# need to protect menu_choice BETTER or at all.... accidently entered e3 at menu screen and crashed system