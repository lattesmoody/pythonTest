import tkinter as tk

def process_input():
    input_text = input_text_widget.get("1.0", "end-1c")  # 입력된 텍스트 가져오기
    processed_text = input_text.replace('“', "'").replace('”', "'").replace('>', '')  # 처리된 텍스트
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
