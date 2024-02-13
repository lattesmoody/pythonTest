input_lines = []  

while True:
    line = input()  
    if line.strip() == "":  
        break
    input_lines.append(line)  

multiline_input = '\n'.join(input_lines)

result = multiline_input.replace(
    '‘', "'"  
).replace(
    '’', "'"  
).replace(
    '>', ''  
)

print("변경된 문장:")
print(result)  
