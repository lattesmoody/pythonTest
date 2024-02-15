a = b = [1, 2, 3]
a[1] = 4
print(b)

# 같은 주소 참조.
print(id(b))
print(id(a))