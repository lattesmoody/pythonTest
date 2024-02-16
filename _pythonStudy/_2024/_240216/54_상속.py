"""
class TravelBlackBox는 부모의 BlackBox를 물려받음.
"""


class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TravelBlackBox(BlackBox):
    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')


b1 = BlackBox('까망이', 200000)
b2 = TravelBlackBox('하양이', 100000)

print(b2.name)
