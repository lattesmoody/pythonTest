result = 0
try:
    [1,2,3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError as Error:
    print(Error)
    result += 3
finally:
    print('finally 호출')
    result += 4

print(result)

"""
IndexError에서 먼저 Except 걸려서 3 더하고 finally 단 실행하여 4를 더했기 때문에 결과는 7이 나온다.
"""

