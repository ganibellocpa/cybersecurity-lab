# This Python project calculates the American Cars Rental Payment
# Project Name: American Cars Rental Project
# Date: 10/15/2024
# Programmer: Ganiyu Bello    Instructor: Ogar Haji

# Constants
CHARGE_PER_DAY = 40.0  # $40 per day
CHARGE_PER_MILE = 0.30  # $0.30 per mile
DISCOUNT_RATE = 0.20    # 20% discount

# Function to validate days rented
def check_invalid_days(days):
    if days < 0 or days > 100:
        print('Invalid number of days. Please enter a value between 0 and 100.')
        return False
    return True

# Function to validate mileage input
def check_invalid_miles(beginning_miles, ending_miles):
    if beginning_miles < 0:
        print("Invalid beginning miles. Must be 0 or greater.")
        return False
    if ending_miles < 0 or ending_miles < beginning_miles:
        print("Invalid ending miles. Must be 0 or greater and not less than beginning miles.")
        return False
    return True

# Function to calculate rental charges
def calculate_rental_charges(days_rented, beginning_miles, ending_miles):
    charges_by_days = days_rented * CHARGE_PER_DAY
    miles_travelled = ending_miles - beginning_miles
    charges_by_miles = miles_travelled * CHARGE_PER_MILE
    total_charges = charges_by_days + charges_by_miles

    # Apply discount
    discount = total_charges * DISCOUNT_RATE
    amount_due = total_charges - discount

    return {
        "Days Charge": charges_by_days,
        "Miles Charge": charges_by_miles,
        "Total Charges": total_charges,
        "Discount": discount,
        "Amount Due": amount_due
    }

# Main Program
print("************ American Cars Rental ************")
print("******** Calculate Total Amount Due Program ********")

# Customer information
customer_name = input("Enter Customer Full Name: ")
days_input = int(input("Enter Number of Days Rented: "))
ending_miles = int(input("Enter Ending Miles: "))
beginning_miles = int(input("Enter Beginning Miles: "))


# Validation and calculations
if check_invalid_days(days_input) and check_invalid_miles(beginning_miles, ending_miles):
    result = calculate_rental_charges(days_input, beginning_miles, ending_miles)
   
    # Display the result
    print("\n***********************************************")
    print("The calculated output of the project looks like the following:")
    print(f"Charges By Days = ${result['Days Charge']:.2f}")
    print(f"Charges By Miles = ${result['Miles Charge']:.2f}")
    print(f"Total Charges = ${result['Total Charges']:.2f}")
    print(f"Discount (20%) = -${result['Discount']:.2f}")
    print(f"Total Amount Due = ${result['Amount Due']:.2f}")
    print("***********************************************")
    print("************ End of Program ************")
    print("***** Programmer: Ganiyu Bello    Instructor: Ogar Haji *****")
