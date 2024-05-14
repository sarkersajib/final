import random
class Account:
    def __init__(self, name, email, address, account_type):
        self.account_no = str(random.randint(1000000000, 9999999999))
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.Total_balance = 0
        self.transaction_history = []
        self.Total_loan= 0

    def deposit(self, amount):
        self.Total_balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount > self.Total_balance:
            print("Withdrawal amount exceeded")
        else:
            self.Total_balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")

    def check_balance(self):
        return self.Total_balance

    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)

    def get_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.Total_loan >= 2:
            print("Error: Loan limit exceeded")
        else:
            self.Total_balance += amount
            self.Total_loan += 1
            self.transaction_history.append(f"Total Loan: {amount}")

class Bank:
    def __init__(self):
      
        
        self.total_loan = 0
        self.loan_status = True
        self.account_list = {}

    def create_account(self,name,email,address,account_type):
        account = Account(name,email,address,account_type) 
        self.account_list [account.account_no]  = account
        return account.account_no
    def delete_account(self, account_no):
        if account_no in self.account_list:
            del self.account_list[account_no]

    def transfer(self, from_acc, to_acc, amount):
        if from_acc not in self.accounts or to_acc not in self.accounts:
            print("Error: Account does not exist")
        elif self.account_list[from_acc].balance < amount:
            print("Error: Insufficient balance")
        else:
            self.account_list[from_acc].withdraw(amount)
            self.account_list[to_acc].deposit(amount)
            print(f"Transferred {amount} from {from_acc} to {to_acc}")

    def get_total_balance(self):
        return sum(account.Total_balance for account in self.account_list.values())

    def get_total_loan_amount(self):
        return self.get_total_loan_amount

    def toggle_loan_feature(self):
        self.loan_feature = not self.loan_status

class Admin:
    def __init__(self,bank):
        self.bank = bank

    def create_account(self,name,email,address,account_type):

        
        return self.bank.create_account(name, email, address, account_type)
        
        
        
    def delete_account(self,account_no):
        self.bank.delete_account(account_no)

    def get_account_list(self):
        return self.bank.account_list.keys()

    def get_total_balance(self):
        return self.bank.get_total_balance()

    def get_total_loan_amount(self):
        return self.bank.get_total_loan_amount()

    def toggle_loan_feature(self):
        self.bank.toggle_loan_feature()
       


bank = Bank()
admin = Admin(bank)   
while True:
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    ch = input("Enter input:")

    if ch == '1':
        
        while True:
            print("\nUser Menu")
            print("1. Create Account")
            print("2. Login")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Check Balance")
            print("6. Transaction History")
            print("7. Take Loan")
            print("8. Transfer")
            print("9. Logout")
            choice = input("Enter choice: ")

            if choice == '1':
                name = input("Enter name: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                account_type = input("Enter account type (Savings/Current): ")
                account_no = bank.create_account(name, email, address, account_type)
                print(f"Account created successfully! Your account number is {account_no}")

            elif choice == '2':
                account_no = input("Enter account number: ")
                if account_no in bank.account_list:
                    current_account = bank.account_list[account_no]
                    print("Login successful!")
                else:
                    print("Error: Account not found")

            elif choice == '3':
                if current_account:
                    amount = float(input("Enter amount to deposit: "))
                    current_account.deposit(amount)
                    print("Deposit successful!")
                else:
                    print("Error: Please login first")

            elif choice == '4':
                if current_account:
                    amount = float(input("Enter amount to withdraw: "))
                    current_account.withdraw(amount)
                    print("Withdraw successful")
                else:
                    print("Error: Please login first")

            elif choice == '5':
                if current_account:
                    print(f"Available balance: {current_account.check_balance()}")
                else:
                    print("Error: Please login first")

            elif choice == '6':
                if current_account:
                    print("Transaction History:")
                    for transaction in current_account.get_transaction_history():
                        print(transaction)
                else:
                    print("Error: Please login first")

            elif choice == '7':
                if current_account:
                    if bank.loan_feature:
                        amount = float(input("Enter loan amount: "))
                        current_account.Total_loan(amount)
                        bank.total_loan_amount += amount
                    else:
                        print("Error: Loan feature is currently disabled")
                else:
                    print("Error: Please login first")

            elif choice == '8':
                if current_account:
                    to_acc = input("Enter the account number to transfer to: ")
                    amount = float(input("Enter amount to transfer: "))
                    bank.transfer(current_account.account_number, to_acc, amount)
                else:
                    print("Error: Please login first")

            elif choice == '9':
                current_account = None
                print("Logged out successfully!")
                break

            else:
                print("Invalid choice! Try again.")
    elif ch == '2':
        
        while True:
            print("\nAdmin Menu")
            print("1. Create Account")
            print("2. Delete Account")
            print("3. View All Accounts")
            print("4. Check Total Balance")
            print("5. Check Total Loan Amount")
            print("6. Toggle Loan Feature")
            print("7. Logout")
            choice = input("Enter choice: ")

            if choice == '1':
                name = input("Enter name: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                account_type = input("Enter account type (Savings/Current): ")
                account_number = admin.create_account(name, email, address, account_type)
                print(f"Account created successfully! Account number is {account_number}")

            elif choice == '2':
                account_no = input("Enter account number to delete: ")
                admin.delete_account(account_no)
                print("Account deleted successfully!")

            elif choice == '3':
                account_list = admin.get_account_list()
                print("All Accounts:")
                for acc in account_list:
                    print(acc)

            elif choice == '4':
                Total_balance = admin.get_total_balance()
                print(f"Total available balance in the bank: {Total_balance}")

            elif choice == '5':
                total_loan_amount = admin.get_total_loan_amount()
                print(f"Total loan amount: {total_loan_amount}")

            elif choice == '6':
                admin.toggle_loan_feature()
                print("Loan feature toggled successfully!")

            elif choice == '7':
                break

            else:
                print("Invalid choice! Try again.")
    elif ch == '3':
        break
    else:
        print("Invalid choice! Try again.")




























        

