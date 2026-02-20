'''
This python program will read data from an input file
Open the File for read and calculate the average of 2 tests
Python Programmer: Oluwatosin Bello
Date: 11/15/2025
'''

# 1) Open the file to read using open function and infile object
infile = open('students.txt', 'r')

# 2) print the message Reading Data from student file
print('**** Reading Data from an Input File Students.txt *****\n')

# 3) Initial or Prime reading before entering while loop
first_name = infile.readline()
last_name = infile.readline()
first_test = infile.readline()
second_test = infile.readline()

# 4) Use 'while' statement to loop until no line found to read
while first_name != '':

    # 5) Strip data from new line \n using rstrip()
    first_name = first_name.rstrip('\n')
    last_name = last_name.rstrip('\n')

    # 6) Print firstName, lastName, firstTest and secondTest
    print('First Name:', first_name)
    print('Last Name: ', last_name)
    print('First Test: ', first_test, end='')
    print('Second Test: ', second_test, end='')

    # 7) Convert the string test values into int
    first_test = int(first_test)
    second_test = int(second_test)

    # 8) Calculate the Average of the 2 tests
    average = (first_test + second_test) / 2.0
    print('Average: {:.2f}'.format(average))

    # 9) Check if the student is Passing or Failing
    if average >= 70:
        status = 'Passing'
    else:
        status = 'Failing'

    # 10) Print out the Student Name and the Status
    print('The Student: {0} {1} is {2}'.format(first_name, last_name, status))

    # 11) Print a separator line
    print('---------------------------------------------------------')

    # 12) Second reading
    first_name = infile.readline()
    last_name = infile.readline()
    first_test = infile.readline()
    second_test = infile.readline()

# 13) End message
print('******* End of the project ********')

# 14) Close the file
infile.close()
