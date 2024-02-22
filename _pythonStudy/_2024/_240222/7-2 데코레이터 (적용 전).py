# 데코레이터: 기존 함수를 바꾸지 않고 기능을 추가할 수 있게 만드는 클로저
import time

def elapsed(original_func):   # 기존 함수를 인수로 받는다.
    def wrapper():
        start = time.time()
        result = original_func()    # 기존 함수를 수행한다.
        time.sleep(1)
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
        return result  # 기존 함수의 수행 결과를 리턴한다.
    return wrapper

def myfunc():
    print("함수가 실행됩니다.")

decorated_myfunc = elapsed(myfunc)
decorated_myfunc()

"""
함수가 실행됩니다.
함수 수행시간: 1.001043 초

Process finished with exit code 0
"""