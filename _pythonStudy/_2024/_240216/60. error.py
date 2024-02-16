num1 = 3
num2 = 0
try:
    result = num1 / num2
    print(f'연산 결과는 {result}입니다')
except ZeroDivisionError:
    print('0 으로 나눌 수 없어요')
except TypeError:
    print('값의 형태가 이상해요')
except Exception as err:
    print('에러가 발생했어요 : ', err)
else:
    print('정상 동작했어요')
finally:
    print('수행 종료')