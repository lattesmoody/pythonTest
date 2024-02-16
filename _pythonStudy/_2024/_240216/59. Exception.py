"""
try:
    # 수행 문장
except:
    # 에러 발생 시 수행 문장
else:
    # 정상 동작 시 수행 문장
finally:
    # 마지막으로 수행할 문장
"""
num1 = 3
num2 = 1
try:
    result = num1 / num2
    print(f'연산 결과는 {result}입니다')
except:
    print('에러가 발생했어요')
else:
    print('정상 동작했어요')
finally:
    print('수행 종료')
