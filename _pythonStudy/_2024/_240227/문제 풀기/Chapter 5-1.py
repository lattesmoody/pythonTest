class Person:
    # 여기에 코드를 작성하세요
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        string = self.name + "님이 " + str(self.age) + "살입니다"
        return string

person1 = Person("홍길동", 30)
print(person1.greet())  # 출력: 홍길동님이 30살입니다.

