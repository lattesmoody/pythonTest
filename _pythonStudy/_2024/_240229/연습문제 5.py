data = {
    '011' : 'SKT',
    '016' : 'KT',
    '019' : 'LGU',
    '010' : '알수없음'
}

phoneNumber = input("휴대전화 번호 입력: ")

if phoneNumber[0:3] == '011':
    print(f'당신은 {data['011']} 사용자입니다.')
elif phoneNumber[0:3] == '016':
    print(f'당신은 {data['016']} 사용자입니다.')
elif phoneNumber[0:3] == '019':
    print(f'당신은 {data['019']} 사용자입니다.')
else:
    print("사용자의 통신사를 알 수 없습니다.")