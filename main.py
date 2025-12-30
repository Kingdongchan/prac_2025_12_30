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
        self.name = tk.button(self.main, text=f"{self.text}").grid(row=self.row, column=self.column)



        