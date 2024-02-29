try:
    number = input("숫자를 입력하세요: ")
    squared_number = int(number) ** 2
    print("입력한 숫자의 제곱:", squared_number)
except ValueError as Error:
    print(f'숫자만 입력해주세요 {Error}')
