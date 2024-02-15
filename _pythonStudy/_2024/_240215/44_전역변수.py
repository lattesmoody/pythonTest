message = '나는야 전역 변수'
print(message,id(message))


def no_secret():
    global message
    message = '오 진짜 전역 변수!!'  # 전역 변수 값 변경

no_secret()
print(message,id(message))

try:
    print(id(message))
except NameError:
    print("메모리에 할당된 객체가 존재하지 않습니다.")

"""
나는야 전역 변수 2340279997568
오 진짜 전역 변수!! 2340279149328
2340279149328
"""