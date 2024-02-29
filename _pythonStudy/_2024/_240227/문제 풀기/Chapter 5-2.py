class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(self.balance)

    def withdraw(self,amount):
        if self.balance - amount < 0:
            print("잔액이 부족합니다.")
        else :
            self.balance = self.balance -  amount
        print(self.balance)
        


account1 = BankAccount(12345, 1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)  # 출력: 잔액이 부족합니다