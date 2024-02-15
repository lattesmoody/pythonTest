result = 0

i = 1
while i <= 1000:
    if i % 3 == 0: # 나머지는 %
        result += i
    i += 1

print(result)