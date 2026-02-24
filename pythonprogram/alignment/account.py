class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance


accounts = []

def insert_account():
    acc_no = int(input("Enter Account Number: "))
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Balance: "))
    accounts.append(BankAccount(acc_no, name, balance))
    print("Account Created Successfully!\n")

def display_accounts():
    if not accounts:
        print("No Records Found!\n")
        return

    print("\n{:<12}{:<20}{:>15}".format("Acc No", "Name", "Balance"))
    print("-" * 47)
    for a in accounts:
        print("{:<12}{:<20}{:>15.2f}".format(a.acc_no, a.name, a.balance))
    print()

def update_account():
    acc_no = int(input("Enter Account Number to Update: "))
    for a in accounts:
        if a.acc_no == acc_no:
            a.name = input("Enter New Name: ")
            a.balance = float(input("Enter New Balance: "))
            print("Record Updated Successfully!\n")
            return
    print("Account Not Found!\n")

def delete_account():
    acc_no = int(input("Enter Account Number to Delete: "))
    for a in accounts:
        if a.acc_no == acc_no:
            accounts.remove(a)
            print("Record Deleted Successfully!\n")
            return
    print("Account Not Found!\n")

while True:
    print("====== Bank Menu ======")
    print("1. Insert")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        insert_account()
    elif choice == 2:
        display_accounts()
    elif choice == 3:
        update_account()
    elif choice == 4:
        delete_account()
    elif choice == 5:
        print("Program Ended!")
        break
    else:
        print("Invalid Choice!\n")