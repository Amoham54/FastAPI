from BankAccount import BankAccount
from savingsaccount import SavingsAccount
from checkingaccount import checkingAccount

User = BankAccount("John Snow", 1200, 200, 1, 120)

print("\n")
User.print_customer_info()
print("\n")
User.deposit(100)
User.withdraw(200)
User.withdraw(1200) #insufficient funds
print("\n")
User.print_customer_info()
print("\n")

User2 = SavingsAccount("Cam Newton", 1111, 100, 2 , 121, .5)

print("\n")
User2.print_customer_info()
print("\n")
User2.withdraw(300)
User2.deposit(1000)
User2.withdraw(299)
User2.apply_interest()
print("\n")
User2.print_customer_info()
print("\n")

User3 = checkingAccount("Cristiano Ronaldo", 9000, 201, 3 , 122, 500)

print("\n")
User3.print_customer_info()
print("\n")
User3.withdraw(300)
User3.deposit(1000)
User3.withdraw(299)
User3.transfer(200)
User3.transfer(600)
print("\n")
User3.print_customer_info()
print("\n")







