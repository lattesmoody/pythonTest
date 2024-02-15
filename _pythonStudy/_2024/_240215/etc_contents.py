# kwargs (딕셔너리 전용)

# lambda 예약어 (리턴 값 없을 때 사용 (def 필요없을 때))

add = lambda x, y: x + y
result = add(3, 4)
print(result)

# readlines: 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴

# sys 모듈

import sys

args = sys.argv[1:]
for i in args:
    print(i)

#python etc_contents.py 1 2 3 4

"""
결과:

1
2
3
4
"""
