from tkinter import Frame
from tkinter import Label, Entry
from tkinter import Tk

class FieldFrame(Frame):
    def __init__(self, **kw):
        self.criterios={}
        self.window= Tk()
        self.fr=Frame(self.window)
        count=0
        for i in kw:
            a= Label(self.fr, str(i))
            b= Entry(self.fr)
            self.criterios[str(i)]=b
            a.grid(row=count, column=0, relx=5, rely=5)
            b.grid(row=count, column=1, columnspan=2)
            count+=1

    def getValue(self, crit):
        return self.criterios[crit].get()

    def show(self):
        self.window.mainloop()
