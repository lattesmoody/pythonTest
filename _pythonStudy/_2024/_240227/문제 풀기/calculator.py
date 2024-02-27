def add(a, b):
    c = a + b
    return c

def subtract(a, b): 
    c = a - b
    return c


def multiply(a, b): 
    c = a * b
    return c

def divide(a, b):
    try:
        c = a / b 
        return c
    except ZeroDivisionError as Error:
        return "0으로 나눌 수 없습니다."
