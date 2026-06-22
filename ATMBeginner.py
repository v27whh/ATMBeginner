# =========================================================
# Project: Secure ATM Beginner-Friendly Simulator (ATMBeginner)
# Created by: Youssef Hassan Abdalla
# Description: A beginner-friendly, crash-proof Python script.
# =========================================================

balance = 2000
correct_pin = "1234" #Pin-code
pin_attempts = 3

print("Welcome to the Secure ATM System")
print("================================")

while pin_attempts > 0:
    entered_pin = input("Please enter your 4-digit PIN: ")
    
    if entered_pin == correct_pin:
        print("\nAccess Granted! Welcome back.")
        break  #if code is entered correctly let the user in!
    else:
        pin_attempts -= 1 #The attemppts decrease each time you enter a Pin-code!
        print(f"Incorrect PIN. Attempts remaining: {pin_attempts}")  #if not, LET HIM OUT! ( with attempts :) ) 
        print("--------------------------------")

if pin_attempts == 0:
    print("\nToo many incorrect PIN attempts. Your card has been blocked.")
    print("Please contact your bank. Goodbye.")
    exit()  #when the pin attempts get to zero, BLOCK THE CARD!!!


while True: #start of the loop!
    print("\n====== ATM MAIN MENU ======") 
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
#bank menu
    choice = input("Choose an option (1-4): ")
    print("--------------------------------")

    if choice == "1":
        print(f"Your current balance is: ${balance}")  #just to understand the f before the "" basically allows you to add variables to strings.
        
    elif choice == "2":
        try:
            deposit = int(input("How much would you like to deposit?: $"))
            
            if deposit > 0:
                balance += deposit #add the deposit ammount!
                print(f"Success! Your balance is now: ${balance}")
            else:
                print("Error: You must deposit an amount greater than $0.")
               
        except ValueError: #the try-expect basically says, "Instead of this exact error, do this instead"
            print("Error: Invalid input! Please enter a whole number using digits only.")
        
    elif choice == "3":
        try:
            withdraw = int(input("How much would you like to withdraw?: $"))
            
            if withdraw <= 0:
                print("Error: You must withdraw an amount greater than $0.")
            elif withdraw > balance:
                print(f"Insufficient funds! You cannot withdraw more than your balance (${balance}).")
            else:
                balance -= withdraw #subtract the withdrawl ammount!
                print(f"Success! Your balance is now: ${balance}")
                
        except ValueError:
            print("Error: Invalid input! Please enter a whole number using digits only.")
        
    elif choice == "4":
        print("Thank you for using this ATM. Have a wonderful day, farewell!")
        break  
        
    else:
        print("Invalid menu choice. Please select a number between 1 and 4.")