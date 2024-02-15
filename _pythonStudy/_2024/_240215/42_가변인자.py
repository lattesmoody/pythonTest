# 가변인자: 개수가 바뀔 수 있는 인자, 
"""
전달값이 많으면 마지막에 한 번만
"""
def visit(today, *customers):
    print(today)
    for customer in customers:
        print(customer) # 고객 이름 출력

visit('2024', '사람1')
visit('2024', '사람2', '사람3')
visit('2024', '사람4','사람5')


