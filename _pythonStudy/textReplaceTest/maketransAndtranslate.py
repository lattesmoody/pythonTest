input_lines = []  

while True:
    line = input()  
    if line.strip() == "":  
        break
    input_lines.append(line)  

multiline_input = '\n'.join(input_lines)

translation_table = str.maketrans("‘’", "''")
translation_table[ord(">")] = None
result = multiline_input.translate(translation_table)

print("변경된 문장:")
print(result)
