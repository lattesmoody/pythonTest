# 클로저
def mul(m):
    def wrapper(n):
        return m * n
    return wrapper

mul3 = mul(3)
mul5 = mul(5)

print(mul3(10))
print(mul5(10))