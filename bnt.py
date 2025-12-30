import tkinter as tk

root = tk.Tk()

#버튼을 누르면 창에 들어가도록하는 함수 설정
def push(num):
    #입력창을 작성을 할 수 있게 기본 상태로 바꿈
    entry.config(state="normal")
    #누르는 버튼에 있는 값을 입력창에 넣음
    entry.insert(tk.END, num)
    #입력창을 작성하지 못하게 원상태로 복귀
    entry.config(state="readonly")

#버튼 2개와 입력창 생성
entry = tk.Entry(root, state="readonly")
entry.grid(row=0, column=0, columnspan=2)
# 람다 -> 이름없는 일회용 함수
btn1 = tk.Button(root, text="1", padx= 10, pady=10, command=lambda: push(1))
btn1.grid(row=1, column=0)

btn2 = tk.Button(root, text="2", padx=10, pady=10, command=lambda: push(2))
btn2.grid(row=1, column=1)


root.mainloop()