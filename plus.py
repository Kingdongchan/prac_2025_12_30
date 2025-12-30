import tkinter as tk

root = tk.Tk()
root.title("더하기")
root.geometry("600x400")

def plus():
    first = entry1.get()
    second = entry2.get()

    value = first + second 

    result.delete(0, tk.END)
    result.insert(0, value)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, padx=10)

entry2 = tk.Entry(root)
entry2.grid(row=0, column=1, padx=10)

result_bt = tk.Button(root, text="=", command=plus).grid(row=0, column=2, padx=10)

result = tk.Entry(root)
result.grid(row=0, column=3, padx=10)

root.mainloop()
