
class ATMUser:
    def __init__(self, pin_number, balance=1000):
        self.pin_number = pin_number
        self.balance = balance
class ATM(ATMUser):
    def verify_pin(self, entered_pin):
        return self.pin_number == entered_pin

    def check_balance(self):
        print("Current Balance: ₹", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited ₹", amount)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrawn ₹", amount)
        else:
            print("Insufficient balance.")
user = ATM("1234") 
entered_pin = input("Enter your PIN: ")
if user.verify_pin(entered_pin):
    print("PIN is verified")
    user.check_balance()
    try:
        deposit_amount = float(input("Enter amount to deposit: ₹"))
        user.deposit(deposit_amount)
    except ValueError:
        print("Please enter a valid number for deposit.")
    try:
        withdraw_amount = float(input("Enter amount to withdraw: ₹"))
        user.withdraw(withdraw_amount)
    except ValueError:
        print("Please enter a valid number for withdrawal.")
    user.check_balance()

else:
    print("Invalid PIN. Access denied.")


