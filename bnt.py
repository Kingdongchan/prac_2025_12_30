import tkinter as tk

root = tk.Tk()

#버튼을 누르면 창에 들어가도록하는 함수 설정
def push():
    botton1 = btn1.get()
    botton2 = btn2.get()
    
    entry.insert(0, botton1)
    entry.insert(0, botton2)

#버튼 2개와 입력창 생성
entry = tk.Entry(root, state="readonly")
entry.grid(row=0, column=0, columnspan=2)

btn1 = tk.Button(root, text="1", padx= 10, pady=10)
btn1.grid(row=1, column=0)

btn2 = tk.Button(root, text="2", padx=10, pady=10)
btn2.grid(row=1, column=1)


root.mainloop()