def show_balance(balance):
    print("Current balance: $" + str(balance))


def deposit(balance):
    amount = int(input("Enter amount to deposit: "))
    return balance + amount


def withdraw(balance):
    amount = int(input("Enter amount to withdraw: "))
    if balance - amount < balance:
        print("Your withdrawal balance cannot exceed the current balance.")
        return balance
    return balance - amount


def logout(name):
    print("Goodbye", name + "!")
