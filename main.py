import tkinter as tk

#버튼 클래스 만들기
class button:
    def __init__(self, name, main, _text, row, column):
        self.name = name
        self.main = main
        self.text = _text
        self.row = row
        self.column = column

    def maker (self):
        tk.Button(self.main, text=self.text).grid(row=self.row, column=self.column)


root = tk.Tk()
root.title("class 연습")
root.geometry("600x400")

button1 = button("bt1", root, "버튼 1", 0, 0)
button1.maker()

root.mainloop()