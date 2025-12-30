import tkinter as tk

root = tk.Tk()
root.title("뺄셈")
root.geometry("400x200")

#계산하기
#입력한 값을 먼저 가져오기
def minus():
    first = int(entry1.get())
    second = int(entry2.get())

    value = first - second

    result.delete(0, tk.END)
    result.insert(0, value)

#뺄셈을 위해 입력 칸 3개 만들기
entry1 =tk.Entry(root)
entry1.grid(row=0, column=0, padx=10)

entry2 = tk.Entry(root)
entry2.grid(row=0, column=1, padx=10)

#계산 버튼만들기
tk.Button(root, text="=", command=minus).grid(row=0, column=2, padx=10)

result = tk.Entry(root)
result.grid(row=0, column=3, padx=10)

root.mainloop()