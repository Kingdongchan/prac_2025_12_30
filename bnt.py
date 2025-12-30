import tkinter as tk

root = tk.Tk()


#버튼 2개와 입력창 생성
entry = tk.Entry(root, state="readonly")
entry.grid(row=0, column=0, columnspan=2)

btn1 = tk.Button(root, text="1", padx= 10, pady=10)
btn1.grid(row=1, column=0)

btn2 = tk.Button(root, text="2", padx=10, pady=10)
btn2.grid(row=1, column=1)


root.mainloop()