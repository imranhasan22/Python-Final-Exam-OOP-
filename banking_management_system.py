import random
class Account:
    accounts = []
    Total_balance = 0
    total_loan=0

    def __init__(self, name, email, address, account_Type):
        self.name = name
        self.account_num = self.generate_account_number() 
        self.balance = 0
        self.account_Type = account_Type
        self.loan_count=0
        self.loan_permission=True
        self.transfer_permission=True
        self.address=address
        self.bankrupt=False
        self.email=email
        Account.accounts.append(self)
        self.transaction_history= []

    def generate_account_number(self):
        return random.randint(100000000, 9999999999)
class User(Account):

    def deposit(self, amount):
        if 0 < amount:
            self.balance += amount
            Account.Total_balance+=amount
            self.add_transaction_history(f"Deposited ${amount}")
            print(f"\n--> Deposited ${amount} in account number :{self.account_num}. New balance: ${self.balance}  ")
        else:
            print("\n--> Invalid deposit amount")

    def withdraw(self, amount):
        if not self.bankrupt:
            if 0 < amount <= self.balance:
                self.balance -= amount
                Account.Total_balance-=amount
                self.add_transaction_history(f"Withdrew ${amount}")
                print(f"\n--> Withdrew ${amount} from account number :{self.account_num} New balance: ${self.balance} ")
            elif amount > self.balance:
                print("\n--> Withdrawal amount exceeded")
            else:
                print("\n--> Invalid withdrawal amount")
        else:
            print('\n\tBank is bankrupt')

    def check_balance(self):
        print(f"\n--> Available balance: ${self.balance}")

    def check_transaction_history(self):
        print(f"\n--> Transaction history for account number {self.account_num}:")
        for transaction in self.transaction_history:
            print(transaction)

    def add_transaction_history(self, transaction):
        self.transaction_history.append(transaction)
    def check_account_number(self):
        print(f"your account number is {self.account_num}")

    def take_loan(self,amount):
      if self.loan_permission:  
        if self.loan_count <= 2:
            if amount > 0:
                self.balance +=amount
                self.loan_count += 1
                Account.total_loan+=amount
                Account.Total_balance-=amount
                self.add_transaction_history(f"Loan received: ${amount}")
                print(f"\n--> Loan received: ${amount}. New balance: ${self.balance}")
            else:
                print("\n--> Invalid loan amount")
        else:
            print("\n--> Maximum loan limit reached")
      else:
          print('\n\tloan system is off!!') 

    def transfer(self, recipient_account_num, amount):
     
        recipient = None
        for acc in Account.accounts:
            if isinstance(acc,User) and acc.account_num == recipient_account_num:
                recipient = acc
                break
        if recipient:
            if amount > 0 and amount <= self.balance:
              if recipient_account_num != self.account_num: 
                self.balance -= amount
                recipient.balance += amount
                self.add_transaction_history(f"Transferred ${amount} to account number {recipient.account_num}\n new balance ${self.balance}")
                recipient.add_transaction_history(f"Received ${amount} from account number {self.account_num} \n new balance ${recipient.balance}")
                print("\n--> Transfer successful .new balance $",self.balance,"in account number",self.account_num)
              else:
                  print("can,t transfer to your own account")
            else:
                print("\n--> Invalid amount / insufficient balance")
        else: 
            print("\n--> Account does not exist")
     


   

class Admin(Account):
    def __init__(self, name, email, address):
        super().__init__(name, email, address, "Admin")

    
    def show_total_loan(self):
        print(f'\n\tBank total loan is: ${Account.total_loan}')

   
    def create_account(self,name, email, address, account_type):
        user = User(name,email,address,account_type)
        print(f"Account is created for {name} with email {email} and account number {user.account_num}")

   
    def delete_any_user(self,account_name):
        found=False
        for acc in Account.accounts:
            if isinstance(acc, User) and acc.name == account_name:
                found=True
                break
        if found is True:
            Account.accounts.remove(acc)
            print("\n\t user account deleted successfully")
        else:
         print("\n\tUser account not found!")

   
    def see_all_user_list(self):
        print("--------------------------------------------------User Account List--------------------------------------------------")
        print("\tuser name \t\temail \t\taddress \t\taccount Type\t\taccount Number ")
        print("-------------------------------------------------------------------------------------------------------------------------")

        user_accounts = [acc for acc in Account.accounts if isinstance(acc, User)]

        if user_accounts:
            for user in user_accounts:
                print(f'\t{user.name} \t\t {user.email} \t{user.address} \t\t {user.account_Type}   \t\t\t {user.account_num}')
        else:
            print('\tNo user accounts found.')

    
    def check_total_available_balance(self):
       
        print(f'\n\tBank total available balance is: ${Account.Total_balance}')

    
    def permission_loan_on_off(self,is_loan):
        for user in Account.accounts:
            if isinstance(user, User):
                user.loan_permission = is_loan
        print(f'\n\tLoan feature of the bank is now {"on" if is_loan else "off"}.')

  
    def bankrupt_on_off(is_bankrupt):
        for user in Account.accounts:
            if isinstance(user, User):
                user.bankrupt = is_bankrupt
        print(f'\n\tBank is {"bankrupt" if is_bankrupt else "Bank is no longer bankrupt"}')


currentUser = None

while True:
  
   if currentUser is None:

        print("\n--> Welcome to the Banking System!")
        print("1. Login/register as User")
        print("2. Login as Admin")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
        # User part
          choice = input("\n--> Register/Login (R/L) : ").upper()
          if choice == "R":        
            name = input("\nName :")
            email= input("\nEmail :")
            address= input("\nAddress :")
            account_type = input(
                "\n\tAccount type: Savings or Current? : ")
            currentUser = User(name, email, address, account_type)
          elif choice == "L":

            account_number = int(input("Enter your account number: "))
            for account in Account.accounts:
              if  isinstance(account, User) and account.account_num==account_number:
                currentUser = account
                break
            else:
              print("\n--> User account not found!")
          else:
              print("\n\tInvalid option")

        elif choice == "2":
            # admin part
            admin_username = input("Enter admin username: ")
            admin_password = int(input("Enter admin password: "))
   
            if admin_username == "Admin" and admin_password == 123:
               currentUser = Admin("Admin", "admin@gmail.com", "Admin Address")
            else:
              print(f"\n--> Invalid admin credentials!")
        elif choice =="3": 
          print(f"\n--> Exiting the Banking System. Goodbye!")
          break

        else:
          print(f"\n--> Invalid choice.")

     
   else:
     
      if isinstance(currentUser, User):
        
            print("\nWelcome ",currentUser.name ,"!\n")
       
            print(f"1. Withdraw")
            print(f"2. Deposit")
            print(f"3. Check Balance")
            print(f"4. Transaction History")
            print(f"5. Take Loan")
            print(f"6. Transfer Money")
            print(f"7.check account number")
            print(f"8. Logout\n")

            option = int(input("Choose option: "))

            if option == 1:
              amount = int(input("Enter withdrawal amount: $"))
              currentUser.withdraw(amount)
            elif option == 2:
              amount = int(input("Enter deposit amount: $"))
              currentUser.deposit(amount)
            elif option == 3:
              currentUser.check_balance()
            elif option == 4:
              currentUser.check_transaction_history()
            elif option == 5:
              amount=int(input("Enter loan amount : $"))
              currentUser.take_loan(amount)
            elif option == 6:
              recipient_account_num = int(input("Enter recipient's account number: "))
              amount = int(input("Enter transfer amount: $"))
              currentUser.transfer(recipient_account_num, amount)
            elif option == 7:
                currentUser.check_account_number()
            elif option == 8:
              currentUser = None
            else:
              print("Invalid option")

      elif isinstance(currentUser, Admin):
            
            print("\nWelcome ",currentUser.name,"\n")
            print(f'\n\t...........Displayed Admin Menu options ...............\n')
            print(f"\t1. Create account ")
            print(f"\t2. Delete user")
            print(f"\t3. See all user account list ")
            print(f"\t4. Available total balance")
            print(f"\t5. See total loan")
            print(f"\t6. Turn off loan feature")
            print(f"\t7. Bankrupt ")
            print(f"\t8. Logout")
            option = int(input("\n\tChoose an option : "))
            if option == 1:
                name = input("\n\tName : ")
                email = input("\n\tEmail : ")
                address = input("\n\tAddress : ")
                account_type = input(
                    "\n\tAccount type: User or Admin?  : ")
                currentUser.create_account(name, email, address, account_type)
            elif option == 2:
                name = input("\n\tEnter the account name  to delete : ")
                currentUser.delete_any_user(name)
            elif option == 3:
                currentUser.see_all_user_list()
            elif option == 4:
                currentUser.check_total_available_balance()
            elif option == 5:
                currentUser.show_total_loan()

            elif option == 6:
                xd = input(
                    "\n\t Turn off loan feature? (YES or NO)  : ").upper()
                if xd == "YES":
                    currentUser.permission_loan_on_off(False)

            elif option == 7:
                xd = input("\n\t(Do you want to Bankrupt the bank?(YES or NO)  : ")
                if xd == "YES":
                    Admin.bankrupt_on_off(True)
            elif option == 8:
                currentUser = None
            else:
                print("\nt\tInvlid option!")

  


