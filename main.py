import tkinter as tk
from tkinter import messagebox

#버튼 클래스 만들기
class button:
    def __init__(self, main, _text, row, column, msg="info"):
        self.main = main
        self.text = _text
        self.row = row
        self.column = column
        self.msg = msg

    def click_warn(self):
        if self.msg == "종료":
         messagebox.showwarning("경고", "누르지 말라 했잖아")
        else:
            messagebox.showinfo("알림", "다른 거 눌러")
    
    def maker (self):
        tk.Button(self.main, text=self.text, command=self.click_warn).grid(row=self.row, column=self.column)
#글자 클래스 라벨 만들기
class label_maker:
    def __init__(self, main, _text, row, column):
        self.main = main
        self.text = _text
        self.row = row
        self.column = column

    def maker (self):
        tk.Label(self.main, text=self.text).grid(row=self.row, column=self.column)


root = tk.Tk()
root.title("class 연습")
root.geometry("600x400")

labe1 = label_maker(root, "눌러", 0, 0)
labe1.maker()

button1 = button(root, "버튼 1", 0, 1)
button1.maker()


button3 = button(root, "버튼 3", 0, 2)
button3.maker()


labe2 = label_maker(root, "눌르지마", 1, 0)
labe2.maker()

button2 = button(root, "버튼 2", 1, 1, "종료")
button2.maker()


root.mainloop()