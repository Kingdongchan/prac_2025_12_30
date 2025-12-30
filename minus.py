import tkinter as tk

root = tk.Tk()
root.title("뺄셈")
root.geometry("400x200")

#뺄셈을 위해 입력 칸 3개 만들기
tk.Entry(root).grid(row=0, column=0, padx=10)

tk.Entry(root).grid(row=0, column=1, padx=10)

#계산 버튼만들기
tk.Button(root, text="=", command=equl).grid(row=0, column=2, padx=10)

tk.Enry(root).grid(row=0, column=3, padx=10)

root.mainloop()