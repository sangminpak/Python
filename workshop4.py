class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        for char in name:
            if char == " ":
                print("No space allowed in username.")
        if self.name == name:
            print("New username cannot be the same as previous one.")
        elif 2 <= len(name) <= 10:
            self.name = name
        else:
            print("Username cannot be less than 2 or more than 10 characters.")

    def change_pin(self, pin):
        if self.pin == pin:
            print("New PIN cannot be the same as previous one.")
        elif len(pin) == 4:
            self.pin = pin
        else:
            print("PIN has to be exactly 4 numbers")

    def change_password(self, password):
        if self.password == password:
            print("New password cannot be the same as previous one.")
        elif len(password) >= 5:
            self.password = password
        else:
            print("Password cannot be less than 5 characters.")


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    def toggle_on_hold(self):
        if self.on_hold == False:
            self.on_hold = True
        else:
            self.on_hold = False

    def show_balance(self):
        print(self.name, "has an account balance of:",
              "${:,.2f}".format(self.balance))

    def withdraw(self, amount):
        if (isinstance(amount, int) or isinstance(amount, float)) and amount < 0:
            print("The amount has to be a positive number.")
        elif isinstance(amount, str):
            print("You must put in a valid number.")
        elif self.on_hold == True:
            print("Transaction canceled. Your account is on hold.")
        else:
            if amount > self.balance:
                print("Amount to withdraw exceeds current balance.")
                return
            self.balance -= amount

    def deposit(self, amount):
        if (isinstance(amount, int) or isinstance(amount, float)) and amount < 0:
            print("The amount has to be a positive number.")
        elif isinstance(amount, str):
            print("You must put in a valid number.")
        elif self.on_hold == True:
            print("Transaction canceled. Your account is on hold.")
        else:
            self.balance += amount

    def transfer_money(self, amount, user):
        if (isinstance(amount, int) or isinstance(amount, float)) and amount < 0:
            print("The amount has to be a positive number.")
        elif isinstance(amount, str):
            print("You must put in a valid number.")
        elif amount > self.balance:
            print("Amount to transfer exceeds current balance.")
        elif self.on_hold == True:
            print("Transaction canceled. Your account is on hold.")
        else:
            print(f"\nYou are transferring ${amount} to {user.name}")
            print("Authentication required")

            pin = int(input("Enter your PIN: "))

            if pin == self.pin:
                self.balance -= amount
                user.balance += amount
                print("Transfer authorized")
                print(f"Transferring ${amount} to {user.name}")
                return True
            else:
                print("Invalid PIN. Transaction canceled.")
                return False

    def request_money(self, amount, user):
        if (isinstance(amount, int) or isinstance(amount, float)) and amount < 0:
            print("The amount has to be a positive number.")
        elif isinstance(amount, str):
            print("You must put in a valid number.")
        elif self.on_hold == True:
            print("Transaction canceled. Your account is on hold.")
        else:
            print(f"\nYou are requesting ${amount} from {user.name}")
            print("User authentication is required...")

            user_pin = int(input(f"Enter {user.name}'s PIN: "))
            my_pw = input("Enter your password: ")

            if user_pin == user.pin and my_pw == self.password:
                user.balance -= amount
                self.balance += amount
                print("Request authorized")
                print(f"{user.name} sent ${amount}")
            elif user_pin != user.pin and my_pw == self.password:
                print("Invalid PIN. Transaction canceled.")
            elif user_pin == user.pin and my_pw != self.password:
                print("Invalid password. Transaction canceled.")
            else:
                print("Invalid PIN and password. Transaction canceled.")


'''
""" Driver Code for Task 1 """
object = User("Bob", 1234, "password")
print(object.name, object.pin, object.password)
'''


'''""" Driver Code for Task 2 """
object = User("Bob", 1234, "password")
print(object.name, object.pin, object.password)
object.change_name("Bob hello")'''
'''
object.change_pin(4321)
object.change_password("newpassword")
print(object.name, object.pin, object.password)
'''

'''
""" Driver Code for Task 3"""
object = BankUser("Bob", 1234, "password")
print(object.name, object.pin, object.password, object.balance)
'''


""" Driver Code for Task 4"""
object = BankUser("Bob", 1234, "password")
object.toggle_on_hold()
# object.show_balance()
object.deposit(1000)
object.show_balance()
'''object.withdraw(1500)
object.show_balance()'''


'''""" Driver Code for Task 5"""
bob = BankUser("Bob", 1234, "bobpassword")
alice = BankUser("Alice", 5678, "alicepassword")

alice.deposit(100)
alice.show_balance()
bob.show_balance()

transfer = alice.transfer_money(500, bob)
'''
'''alice.show_balance()
bob.show_balance()
if transfer == True:
    alice.request_money(250, bob)
    alice.show_balance()
    bob.show_balance()'''
