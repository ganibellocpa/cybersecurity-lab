
# ---------------------------------------------------------------------------------------
# This Python project prompt the user to input a text string 
# It will count number of Characters, digits, spaces, and the symbols
# Python Programmer: Ganiyu Bello
# Date: December 06, 2024
#-------------------------------------------------------------------------------------------

# 1) Declare global counter variables and Initialize them to 0
characters_count = 0
digits_count = 0
symbols_count = 0
spaces_count = 0

# 2) Declare a text string and initialize to empty string
text_string = ''

#---------------------------------------------------------------------------------------

# 3) Define and code the main() function which we call all other functions
def main():
    
    # 1) Call the following functions
    print_headers()
    prompt_user_for_input()
    process_string_and_count()
    print_footers()

#---------------------------------------------------------------------------------------

# 4) Define and code the print_headers() function
def print_headers():
    print ('****count letters digits space in a string *********')

#---------------------------------------------------------------------------------------
    
# 5) Define and code the prompt user for input() function
def prompt_user_for_input():
    
    # 1) Declare a global variable so it can be modified
    global text_string

    # 2) Prompt the user to enter a string text
    text_string = input ('Enter a String of Text and Numbers and Symbols: ')

#-----------------------------------------------------------------------------------------

# 5) Define and code the process_string_and_count() function
def process_string_and_count():
    
    # 1) Declare global variables so you can modify them
    global characters_count
    global digits_count
    global spaces_count
    global symbols_count

    # 2) use for in loop statement to loop inside the string
    for ch in text_string:
        
      # 3) Check if the character isalpha
      if ch.isalpha():
          characters_count += 1 # increment characters count by 1

      # 4) Check if the character (ch) is digit or number
      elif ch.isdigit():
          digits_count += 1 # increment digits counter by 1

      # 5) Check if the character isspace
      elif ch.isspace():
          spaces_count += 1
      else:
          symbols_count += 1
   # End of for loop statement

#------------------------------------------------------------------------------------------

# 6) Define and code print footers() function
def print_footers():
    
   # 4) Print the counters of the characters and the digits
   print ('\nTotal Number of Characters or Letters = ', characters_count)
   print ('Total Number of Digits or Numbers = ', digits_count)
   print ('Total Number of Spaces = ', spaces_count)
   print ('Total Number of Symbols = ', symbols_count)
   print ()
   print ('***** End of the Project +++ Ganiyu Bello *****')

#------------------------------------------------------------------------------------

# 7) Call the main() function which starts execution of project
main()
