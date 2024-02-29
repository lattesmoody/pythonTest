"""
글자 하나를 입력하면 
2, 8, 10, 16진수인지 아닌지를 구분하는 
코드를 작성해 보세요.
"""





import re
p = re.compile('[0-F]+')

inputText = input("입력: ")

result = p.match(inputText)

# if inputChr.search([0-1]) is : 
# elif :
# else :