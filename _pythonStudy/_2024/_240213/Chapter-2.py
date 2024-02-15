my_list = [1,2,3]
for x in my_list:
    print(x)

person = {'이름': 'hello', '나이':7}
for k,v in person.items():
    print(k,v)

fruit = 'apple'
for x in fruit:
    print(x)


max = 25 # 최대 허용 무게
weight = 0 # 현재 캐리어 무게
item = 3 # 각 짐의 무게
while weight + item <= max: # 캐리어에 짐을 더 넣어도 되는지 확인
    weight += item
print('짐을 추가합니다')
print(f'총 무게는 {weight} 입니다')

my_list = [1, 2, 3, 4, 5]
new_list = [x for x in my_list if x > 3]
print(new_list)

my_list = [1, 2, 3, 4, 5]
new_list = [x+1 for x in my_list if x > 3]
print(new_list)

products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
recall = [p for p in products if p.startswith('SIRO')]
print(recall)