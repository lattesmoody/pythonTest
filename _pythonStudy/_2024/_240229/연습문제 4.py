"""
문자열로 표현된 PER 값을 
실수로 변환한 후 
이를 새로운 리스트에 
저장해보세요.
"""

per = ["10.31", "", "8.00"]


newList = []
for i in per:
    try:
        newList.append(float(i))
    except Exception as Error:
        print(Error)
        pass

print(newList)
    