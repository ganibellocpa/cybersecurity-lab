# #################################################################
# 1) Purpose of the Program: This Program will do different calculations on
# Two Numbers. It will call functions or modules to do calculations
# Programmer: Instructor: Ganiyu Bello
# Date: Thursday, October 24, 2024 (Type Today’s Date)
# Week 4: Calculating Two Numbers. File name calculating_two_numbers.py
# #################################################################
# 2) Declare the Variables to be used in the program.
# In Python language, you do Not have to explicitly declare variables
# just use them when needed
# 3) This is the main function that will call All the other functions
def main():
    # 4) Call print_headings function to display program info
    print_headings()

    # 5) Display the prompts and input (get, read) what user enters
    # Try to get valid integer inputs from the user
    number1 = get_integer_input('Enter the First Number: ')
    number2 = get_integer_input('Enter the Second Number: ')

    # 6) Call the functions or Modules to do the Calculations on the Two numbers
    add_numbers(number1, number2)
    subtract_numbers(number1, number2)
    print_footers()

# Function to get a valid integer input
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter an integer.")

# ---------------------------------------------------------------------------------------
# 7) Define the functions that are used in the program. The Definitions of
# functions must start at column 0, Not Indented with No Spaces before def
# a)The print_headings() function prints the headings of the program
def print_headings():
    print('*' * 70)
    print('***** Doing Calculations on Two Numbers *****')
    print('-' * 70)
    print('**** This program asks the user to enter 2 numbers ****')
    print('**** then it will call many modules to do \
different Calculations ****')
    print('*' * 70)
    print()

# -------------------------------------------------------------------------------------------------

# b) The add_numbers() function will accept 2 arguments, number1
# and number2 and then will add the Two numbers passed to it
def add_numbers(number1, number2):
    result = number1 + number2
    print('The Result of Adding the Two Numbers =', result)

# --------------------------------------------------------------------------------------------------
# c) The subtract_numbers() function will accept 2 arguments, number1
# and number2 and then will subtract the 2 numbers passed to it
def subtract_numbers(number1, number2):
    result = number1 - number2
    print('The Result of Subtracting the Two Numbers =', result)

# --------------------------------------------------------------------------------------------------
       
# d) The print_footers() function displays the End of Program message
def print_footers():
    print()
    print('*' * 70)
    print('*********** E n d o f P r o g r a m ************')
    print('-' * 70)
    print('******* Programmer: Instructor: Ganiyu Bello *******')
    print('*' * 70)

# -------------------------------------------------------------------------------------------------
# 8) Call the main () function or module to start the program
if __name__ == "__main__":
    main()

