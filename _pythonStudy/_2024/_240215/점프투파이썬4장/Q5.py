f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close() # 기존 코드에서 새로 추가.

f2 = open("test.txt", 'r')
print(f2.read())
f2.close() # 기존 코드에서 새로 추가.