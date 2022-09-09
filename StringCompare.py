from tkinter import font
from tokenize import String
from turtle import bgcolor
from FunctionStringCompare import stringCompare
from tkinter import *

def affiche():
 
  str = stringCompare(saisie.get(), saisie2.get())
  if str:
  
    label1.config(fg="green")
    label1.pack()
    text.set("Compare pass ! ")
    
  else:
    text.set("Compare not good !!!")
    label1.config(fg="red")
    label1.pack()

window = Tk()
window.title("String Compare")


label = Label(text="Input both string to compare : ")
label.pack()
text=StringVar()
text.set("test")


saisie = Entry()
saisie.pack()
saisie2 = Entry()
saisie2.pack()


label1 = Label(window, textvariable=text)


button = Button(text="Compare!", command=affiche)
button.pack()



window.mainloop()

