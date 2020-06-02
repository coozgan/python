from tkinter import *
from tkinter.ttk import Frame, Button, Entry, Style


class Calc(Frame):

    def __init__(self):
        super().__init__()

        self.entry = Entry(self)
        self.total = 0
        self.operation = ''
        self.initUI()

    def number_btn_click(self, number):
        current = self.entry.get()
        if number == '.' and '.' in current:
            current = current.replace('.', '')
            self.entry.delete(0, END)
            self.entry.insert(0, str(current) + str(number))
        else:
            self.entry.delete(0, END)
            self.entry.insert(0, str(current) + str(number))

    def divide_btn_click(self):
        self.total = int(self.entry.get())
        self.operation = 'divide'
        self.entry.delete(0, END)

    def plus_btn_click(self):
        self.total = int(self.entry.get())
        self.operation = 'plus'
        self.entry.delete(0, END)

    def multiply_btn_click(self):
        self.total = int(self.entry.get())
        self.operation = 'multiply'
        self.entry.delete(0, END)

    def minus_btn_click(self):
        self.total = int(self.entry.get())
        self.operation = 'minus'
        self.entry.delete(0, END)

    def clear_btn(self):
        self.entry.delete(0, END)

    def del_btn(self):
        current = self.entry.get()[:-1]
        self.entry.delete(0, END)
        self.entry.insert(0, current)

    def equals_btn(self):
        if self.operation == 'plus':
            self.total += int(self.entry.get())
        elif self.operation == 'minus':
            self.total -= int(self.entry.get())
        elif self.operation == 'divide':
            self.total /= int(self.entry.get())
        elif self.operation == 'multiply':
            self.total *= int(self.entry.get())
        self.entry.delete(0, END)
        self.entry.insert(0, str(self.total))

    def initUI(self):
        self.master.title("Calculator")

        Style().configure("TButton", padding=(0, 5, 0, 5),
                          font='sans-serif 12')
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        self.entry.grid(row=0, columnspan=4, sticky=W + E)
        cls = Button(self, text="Cls", command= self.clear_btn)
        cls.grid(row=1, column=0)
        bck = Button(self, text="Back", command=self.del_btn)
        bck.grid(row=1, column=1)
        lbl = Button(self)
        lbl.grid(row=1, column=2)
        clo = Button(self, text="Close", command = self.quit)
        clo.grid(row=1, column=3)
        sev = Button(self, text="7", command=lambda: self.number_btn_click(7))
        sev.grid(row=2, column=0)
        eig = Button(self, text="8", command=lambda: self.number_btn_click(8))
        eig.grid(row=2, column=1)
        nin = Button(self, text="9", command=lambda: self.number_btn_click(9))
        nin.grid(row=2, column=2)
        div = Button(self, text="/", command= self.divide_btn_click)
        div.grid(row=2, column=3)

        fou = Button(self, text="4", command=lambda: self.number_btn_click(4))
        fou.grid(row=3, column=0)
        fiv = Button(self, text="5", command=lambda: self.number_btn_click(5))
        fiv.grid(row=3, column=1)
        six = Button(self, text="6", command=lambda: self.number_btn_click(6))
        six.grid(row=3, column=2)
        mul = Button(self, text="*", command= self.multiply_btn_click)
        mul.grid(row=3, column=3)

        one = Button(self, text="1", command=lambda: self.number_btn_click(1))
        one.grid(row=4, column=0)
        two = Button(self, text="2", command=lambda: self.number_btn_click(2))
        two.grid(row=4, column=1)
        thr = Button(self, text="3", command=lambda: self.number_btn_click(3))
        thr.grid(row=4, column=2)
        mns = Button(self, text="-", command= self.minus_btn_click)
        mns.grid(row=4, column=3)

        zer = Button(self, text="0", command=lambda: self.number_btn_click(0))
        zer.grid(row=5, column=0)
        dot = Button(self, text=".", command=lambda: self.number_btn_click('.'))
        dot.grid(row=5, column=1)
        equ = Button(self, text="=", command= self.equals_btn)
        equ.grid(row=5, column=2)
        pls = Button(self, text="+", command= self.plus_btn_click)
        pls.grid(row=5, column=3)

        self.pack()


def main():
    root = Tk()
    app = Calc()
    root.mainloop()


if __name__ == '__main__':
    main()