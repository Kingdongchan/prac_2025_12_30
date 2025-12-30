import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

entry = tk.Entry(root, state="disabled")
entry.pack()

entry2 = tk.Entry(root, state="readonly")
entry2.pack()

root.mainloop()