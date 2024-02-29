f = open('C:/Users/latte/PycharmProjects/pythonProject/pythonTest/_pythonStudy/_2024/_240229/abc.txt', 'r')
lines = f.readlines()
f.close()
lines.reverse()

print(lines)