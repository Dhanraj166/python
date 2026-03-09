class ATMAccount:
    def __init__(self, account_name, account_number, balance, pin):
        self.account_name = account_name
        self.account_number = account_number
        self.balance  = balance
        self.pin = pin


    def deposit(self, amount):
        self.balance += amount
        print(amount, "Deposit successfully")

    def withdraw(self, amount):
        if(amount<=self.balance):
            self.balance -= amount
            print(amount, "Withdraw successfully")
        else:
            print("Invallid Balance")
    

    def check_balance(self):
        print("Account Holder :", self.account_name)
        print("balance :", self.balance)

user1 = ATMAccount("Dhanraj", 781004263, 8000, 5673)
user2 = ATMAccount("Vimal", 598376398, 12000, 8798)
user3 = ATMAccount("Arun", 498693755, 20000, 1050)
user3 = ATMAccount("Guru", 434857348, 20000, 2527)

user2.deposit(2000)
user2.check_balance()
user2.withdraw(15000)
user2.withdraw(14000)
user2.check_balance()


        




