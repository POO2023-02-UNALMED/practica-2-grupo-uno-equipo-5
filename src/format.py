from tkinter import Frame
from tkinter import Label, Entry
from tkinter import Tk

class FieldFrame(Frame):
    def __init__(self, title="",geo="300x300", **args):
        self.criterios=dict()
        self.window= Tk()
        self.window.title(title)
        self.window.geometry(geo)
        self.fr=Frame(self.window)
        count=0
        for i in args:
            a= Label(self.fr, text=i)
            b= Entry(self.fr)
            self.criterios[i]=b
            a.grid(row=count, column=0, padx=5, pady=5)
            b.grid(row=count, column=1, columnspan=2, padx=5, pady=5)
            count+=1

    def getValue(self, crit):
        print(self.criterios)
        print(self.criterios[crit])
        return self.criterios[crit].get()

    def show(self):
        self.window.mainloop()
