import random

class BankingSystem:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}  

    def create_account(self):
        account_owner = input("Enter account owner name: ")
        account_number = random.randint(0, 9999999999999999)  
        self.accounts[account_number] = {"owner": account_owner, "balance": 0}
        print("Account created with account number: ",account_number)

    def deposit(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter the amount to deposit: "))
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            print("Deposited: ", amount," successfully. New balance: ",self.accounts[account_number]["balance"])
        else:
            print("Account not found!")

    def withdraw(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter the amount to withdraw: "))
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                print("Withdrew ", amount," successfully. New balance:", self.accounts[account_number]['balance'])
            else:
                print("Insufficient balance!")
        else:
            print("Account not found!")

    def account_summary(self):
        account_number = int(input("Enter account number: "))
        if account_number in self.accounts:
            print("Account Owner: ",self.accounts[account_number]['owner'])
            print("Balance: ",self.accounts[account_number]['balance'])
        else:
            print("Account not found!")

    def run(self):
        while True:
            print("Options:")
            print("a) Create account")
            print("b) Deposit")
            print("c) Withdraw")
            print("d) Account Summary")
            print("e) Exit")
            option = input("Select an option: ").lower()

            if (option == 'a'):
                self.create_account()
            elif (option == 'b'):
                self.deposit()
            elif (option == 'c'):
                self.withdraw()
            elif (option == 'd'):
                self.account_summary()
            elif (option == 'e'):
                break
            else:
                print("Invalid option. Please select a valid option.")


bank = BankingSystem("MyBank")
bank.run()
