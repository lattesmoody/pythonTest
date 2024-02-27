numerator = 10
denominator = 0
try:
    result = numerator / denominator
    print("결과:", result)
except ZeroDivisionError as Error:
    print('0으로 나눌 수 없습니다!')


