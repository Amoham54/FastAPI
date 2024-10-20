#A function that adds two numbers
def add(a , b):
  return a + b

#A function that subtracts two numbers
def subtract(a , b):
    return a - b

#A function that multiplies two numbers
def multiply(a , b):
    return a * b

#A function that adds two numbers
def divide(a , b):
    return a / b

#Main function that handles user input and performs calculation
def calculate():
    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("Enter the number of the operation you wish to execute:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        user_choice = int(input("Enter your choice (1/2/3/4): "))

        if user_choice == 1:
            print(f"Answer: {add(num1,num2)}")
        elif user_choice == 2:
            print(f"Answer: {subtract(num1,num2)}")
        elif user_choice == 3:
            print(f"Answer: {multiply(num1,num2)}")
        elif user_choice == 4:
            print(f"Answer: {divide(num1,num2)}")
        else:
            print("Invalid choice")

        exit_choice = input("Are you finished using the calculator? (Y/N): ").lower()
        if exit_choice == "y":
            print("Thank you for using the calculator!. Bye!")
            break

calculate()
