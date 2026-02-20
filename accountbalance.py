# account_test.py - A test program for the BankAccount class

# 1) Import the module 'bank_account' created in the previous program
import bank_account

def main():
    try:
        # 1) Prompt the user to enter the starting balance and get it.
        start_balance = float(input('Enter your Starting Balance in the Bank: '))
        
        # 2) Create an object called `savings` from the BankAccount class.
        savings = bank_account.BankAccount(start_balance)
        
        print(f'Your Starting Balance in the bank is: ${savings.get_balance():.2f}')
        print()
        
        # 3) Deposit the user's paycheck.
        deposit = float(input('Enter the amount to Deposit: '))
        savings.deposit(deposit)
        print(f'Deposited ${deposit:.2f}. Updated balance: ${savings.get_balance():.2f}')
        print()
        
        # 4) Get the amount to withdraw.
        withdraw = float(input('Enter the amount to Withdraw from the Bank: '))
        if withdraw > savings.get_balance():
            print("Error: Insufficient funds.")
        else:
            savings.withdraw(withdraw)
            print(f'Withdrew ${withdraw:.2f}. Updated balance: ${savings.get_balance():.2f}')
        
        print()
    
    except ValueError:
        print("Error: Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# 9) Call the main function to start the program
if __name__ == "__main__":
    main()
