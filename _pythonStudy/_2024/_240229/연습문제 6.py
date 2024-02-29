"""
은행에 가서 계좌를 개설하면 
은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. 
Account 클래스를 생성한 후 생성자를 구현해보세요. 
생성자에서는 예금주와 초기 잔액만 입력 받습니다. 
은행이름은 SC은행으로 
계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
(hint. zfill 함수) => 파이썬 문자열 앞 0으로 채우기
"""
import random
class Account:
    def __init__(self,customerName,balance):
        self.bankName = 'SC은행'
        self.customerName = customerName
        self.balance = balance
        self.accountNumber = f'{str(random.randint(1,999)).zfill(3)}-{str(random.randint(1,99)).zfill(2)}-{str(random.randint(1,999999)).zfill(6)}'

       

customerName = input("이름을 입력하세요: ")
balance = int(input("초기 잔액을 입력하세요: "))
saram = Account(customerName,balance)
print(saram.bankName)
print(saram.accountNumber)
