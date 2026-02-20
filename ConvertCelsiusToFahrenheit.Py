# 1) Add Comments about the project on the top of the project

'''

*****************************************************************

    Purpose of the Project
    a)The Interactive Project will Convert Celsius
      Temperature to Fahrenheit.
          It prompts the userto enter the Celsius temperature
        And it will be converted into Fahrenheit temperature
            And print it to the console.
    b) Project Name: ConvertCelsiusTo Fahrenheit
    C) Date: Saturday, December 28, 2013
    d)Programmer: Ganiyu Bello Python Instructor + Ogar Haji

    *************************************************************

    '''
# 2) Prompt User to Enter Celsius Temperature, read it and store it

celsius = input ('Enter today temperature in Celsius: ')

# 3) Convert the string celsius to float using float() function

celsius = float (celsius)

# 4) Calculate the Formular to Convert Celsius to Fahrenheit

fahrenheit = (celsius * 9.0 / 5.0) + 32

# 5) Print Fahrenheit temperature to the output screen

print('Fahrenheit temperature = ', fahrenheit)

# 6) Print the format 100 Celsius is equal to 212.21 Fahrenheit. Use %.2f

print ('%.2f Celsius is equal to %.2f Fahrenheit.\n' %
       
                                       (celsius, fahrenheit) )

# or Use .format method with Place Holders {}

print ('{:.2f} Celsius is equal to {:.2f} Fahrenheit.'.format
               (celsius, fahrenheit) )


# 7) Check if Fahrenheit Temperature is Less or Equal to 32 then print the
#temperature and it is very cold message.
if fahrenheit <= 32:
    print(f'Today Fehrenheit temperature {fehrenheit} is very Cold,')

#8) Check if Fahrenheit Temperature is is Greater or Equal to 90 then print
#the temperature and it is very Hot message
if fahrenheit >= 90:
    print(f'Today Fehrenheit temperature {fahrenheit} is very Hot.')

























