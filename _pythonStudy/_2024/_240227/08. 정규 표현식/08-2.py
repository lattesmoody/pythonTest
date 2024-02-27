# 파이썬 정규 표현식 지원하는 re 모듈

"""
match
search
findall
finditer
"""

import re
p = re.compile('[a-z]+')

m = p.match("3python00")  # None
n= p.match("python00") # python
print(m) 
print(n)


o = p.search("3python00")
print(o)


result = p.findall("life is too short")
print(result)



k = p.match("python")
print(k.group())
k.start()
k.end()
k.span()


"""
컴파일 옵션
re.DOTALL     # S
re.IGNORECASE # I
re.MULTILINE  # M
re.VERBOSE    # X

"""

"""
역슬래쉬 문제
"""
print('\\\\')
print(r'\\')