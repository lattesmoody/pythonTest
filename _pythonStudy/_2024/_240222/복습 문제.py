# https://leelang7.github.io/python/ml/dl/python9-all/

print("\n# 변수와 문자열 출력\n")
a = 10
b = 20

print (a,'+', b, '=', a+b)

print("\n# 리스트 조작\n")
numbers = [5, 7, 2, 9, 1, 10, 4, 6, 8, 3]
numbers.sort()
print(numbers)

print("\n# 문자열 조작\n")
text = "Python is fun!"
convertText = text.replace(" ","")
sortTextResult = convertText[::-1]

print(sortTextResult)

print("\n# 함수\n")

def add_numbers():
    tmp1 = int(input("입력1 :"))
    tmp2 = int(input("입력2 :"))
    return tmp1+tmp2

resultAddNumbers = add_numbers()
print(resultAddNumbers)

print("\n# 조건문\n")
def oddOrEven():
    Copynumber = 5
    if Copynumber % 2 == 0:
        print("짝수")
    else:
        print("홀수")

oddOrEven()



print("\n# 반복문\n")
def repeatFN():
    list = [1,2,3,4,5,6,7,8,9,10]
    for i in list:
        if i % 2 == 1:
            print(i, end = ' ')
repeatFN()


print("\n# 자료형\n")
# 리스트와 튜플의 차이점을 설명하세요.
"""
정답: 
리스트: 값 수정 가능
튜플: 값 수정 불가
"""

print("\n# 딕셔너리\n")

Copysample_dict = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
for key, value in Copysample_dict.items(): 
    if value == 30:
        print(key)

print("# 리스트 내포")

파일 입출력

예외 처리

람다 함수

모듈

클래스

상속

정규 표현식

리스트 조작

문자열 조작

반복문과 조건문

함수와 리스트
