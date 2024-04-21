class Account:
    def __init__(self,first_name,last_name, balance=0):
        self.name = first_name
        self.last_name = last_name
        #self.account = account
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("You have a withdraw,your new balance is", customer1.balance)
        else:
            print("There is not enough balance in this account")
            user = input("Please select s for your account information or x for exit:  ")
            if user == "s":
                self.ac_information()
            else:
               print("Select the right operation")


    def ac_information(self):
        print("Your balance is", self.balance)




accounts = {}
while True:
    your_name = input("Enter your first name: ")
    your_last_name = input("Enter your last name: ")
    account_number = input("Enter your account number: ")
    customer1 = Account(your_name, your_last_name)
    accounts[account_number] = customer1
    operation = input("Please select from the menu. \n 1 Deposit! \n 2 Withdraw! ")
    if operation == "1":
        amount = float(input("Enter your amount:  "))
        customer1.deposit(amount)
        print("You have a deposit,your new balance is", customer1.balance)
    elif operation == "2":
        amount = float(input("enter your amount:  "))
        customer1.withdraw(amount)

    elif operation == "3":
        print("Your are exiting from the program!")
        break
    else:
        print("Invalid input. Please selece 1 for deposit, 2 for wothdraw and 3 for exit")


















