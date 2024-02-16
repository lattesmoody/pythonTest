#init은 객체가 생성되면 자동으로 호출된다.
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

b1 = BlackBox('까망이', 200000)
print(b1.name, b1.price)
b2 = BlackBox('하양이', 100000)
print(b2.name, b2.price)

# 어떤 객체인지 구분하기 위해 self 사용 (객체를 가리킴)
