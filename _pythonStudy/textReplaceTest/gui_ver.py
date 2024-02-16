import tkinter as tk

def process_input():
    input_text = input_text_widget.get("1.0", "end-1c")  # 입력된 텍스트 가져오기
    processed_text = input_text.replace('“', "'").replace('”', "'")  # 처리된 텍스트
    output_text_widget.delete("1.0", "end")  # 이전 결과 지우기
    lines = processed_text.split('\n')  # 개행을 기준으로 문장 분할
    
    processed_lines = []  # 처리된 텍스트를 저장할 리스트
    skip_next = False  # 다음 문장을 건너뛸지 여부를 나타내는 변수
    for line in lines:
        if (('def' in line) or ('with' in line)):  # 'def' 키워드를 포함하고 있는 경우
            processed_lines.append(line)  # 'def' 포함된 줄은 들여쓰기 없이 추가
            skip_next = True  # 다음 문장을 건너뛰도록 설정
        elif skip_next:
            processed_lines.append('    ' + line)  # 다음 문장은 4칸 들여쓰기하여 추가
        else:
            processed_lines.append(line)  # 그 외의 경우에는 그대로 추가
            
    processed_text = '\n'.join(processed_lines)  # 처리된 텍스트를 개행문자로 연결하여 문자열로 변환
    
    output_text_widget.delete("1.0", "end")  # 이전 결과 지우기
    output_text_widget.insert("1.0", processed_text)  # 처리된 텍스트 출력

# 메인 윈도우 생성
root = tk.Tk()
root.title("Text Processing Tool")

# 입력 텍스트
input_label = tk.Label(root, text="Enter your text:")
input_label.pack()
input_text_widget = tk.Text(root, height=10, width=50)
input_text_widget.pack()

# 처리 버튼
process_button = tk.Button(root, text="Process", command=process_input)
process_button.pack()

# 출력 텍스트
output_label = tk.Label(root, text="Processed text:")
output_label.pack()
output_text_widget = tk.Text(root, height=10, width=50)
output_text_widget.pack()

# GUI 실행
root.mainloop()
