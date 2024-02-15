f = open('list.txt', 'r', encoding='utf8')
contents = f.read() # 파일 내용 다 읽어오기
print(contents)
f.close()

f = open('list.txt', 'r', encoding='utf8')
for line in f:
    print(line, end='') # (CRLF)없이 다음 라인으로 넘김.
f.close()
