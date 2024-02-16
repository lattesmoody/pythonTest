# method: 기능 구현
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def set_travel_mode(self):
        print(f'{self.name}는 여행 모드 ON')

    def set_travel_mode2(self, min):  # 여행 모드 시간 (분)
        print(str(min) + '분 동안 여행 모드 ON')


b1 = BlackBox('까망이', 200000)
b2 = BlackBox('하양이', 200000)
b1.set_travel_mode()
b2.set_travel_mode()
b1.set_travel_mode2(20)