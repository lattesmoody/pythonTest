
class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class MailSender:
    def send(self):
        print('메일 발송')


class TravelBlackBox(BlackBox,VideoMaker,MailSender):
    def __init__(self, name, price,sd):
        super().__init__(name,price)
        # super() 부모 클래스 (객체는 아님) 부르고 초기화.
        # 다른 프레임워크 불러올 때 간간히 쓰인다.
        self.sd= sd
    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')

class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')
        self.make()  # 추억용 여행 영상 제작
        self.send()  # 메일 발송


b1 = BlackBox('까망이', 200000)
b2 = TravelBlackBox('하양이', 100000,'64GB')

print(b2.name)
print(b2.sd)

b3 = AdvancedTravelBlackBox('초록이', 120000, 64)
b3.set_travel_mode(15)

