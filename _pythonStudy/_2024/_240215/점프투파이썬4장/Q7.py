f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java','python')

f = open('test.txt', 'w', encoding = 'utf-8')
f.write(body)
f.close()