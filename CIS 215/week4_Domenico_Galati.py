#Declaring and initializing variabls
names = ["Domenico Galati","Duane Marshall","Collin Duffy","Skylar Aguado",\
         "Collin Berney"]
Names = ["Jeff George","Howard Thomas","Betsy Randolf","Nancy Bloom",\
         "Doug Hammersmith", "Rebecca Smith"]
Year = ["Freshman","Sophomore","Senior","Freshman","Junior","Freshman"]
Age = [25,63,120,30,85,20]
GPA = [3.0,3.75,3.8,3.3,2.75,2.9]
numbers = [0,1,2,3,4]
Numbers = [0,1,2,3,4,5]
nameList = zip(names, numbers)
studentList = zip(Names, Year, Age, GPA, Numbers)
freshmanList = zip(Names, Year, Age, GPA, Numbers)

def listNames(nameList):
    '''Week 2 function (lists all names by first initial and first 3 chars\
       of last name'''
    for name, number in nameList:
        temp = name.split(" ")
        firstName = temp[0]
        lastName = temp[1]
        print(str(number) +": " + firstName[0] + " " + lastName[0:3])
    print()


def listStudents(studentList):
    '''Week 3 function (lists all students in a table'''
    print ("{:<18} {:<10} {:<4} {:<6}".format('Name', 'Year', 'Age', 'GPA'))
    print ("{:<18} {:<10} {:<4} {:<6}".format('====', '====', '===', '==='))
    for name, year, age, gpa, number in studentList:
        print ("{:<18} {:<10} {:<4} {:<6}".format(name, year, age,gpa))

    print("=======================================")
    print()

def listFreshman(freshmanList):
    '''Week 3 function (lists all Freshman in a table'''
    print ("{:<18} {:<10} {:<4} {:<6}".format('Name', 'Year', 'Age', 'GPA'))
    print ("{:<18} {:<10} {:<4} {:<6}".format('====', '====', '===', '==='))
    for name, year, age, gpa, number in freshmanList:
        if "Freshman" in str(year):
            print ("{:<18} {:<10} {:<4} {:<6}".format(name, year, age,gpa))
    print("=======================================")

#Calling the functions
listNames(nameList)
listStudents(studentList)
listFreshman(freshmanList)
    
