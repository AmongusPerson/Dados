from tkinter import *
import random
from PIL import ImageTk, Image
pg = Tk()
pg.geometry("500x500")
pg.title("Imagen")
pg.configure(bg="#264653")
img = ImageTk.PhotoImage(Image.open("imagen.jpg"))

var1 = 0
def fn1():
     global var1
     var2 = random.randint(1,6)
     lb1["text"] = "El jugador 1 saco: " + str(var2)
     var1 = var1+var2
     lb2["text"] = "Puntos: " + str(var1)
     
var3 = 0
def fn2():
        global var3
        var4 = random.randint(1,6)
        lb1["text"] = "El jugador 2 saco: " + str(var4)
        var3 = var3+var4
        lb3["text"] = "Puntos: " + str(var3) 
     
lb1 = Label(pg, text="Label")
lb1.place(relx=0.5, rely=0.5, anchor=CENTER)

lb2 = Label(pg, text="Label")
lb2.place(relx=0.2, rely=0.6, anchor=CENTER)

lb3 = Label(pg, text="Label")
lb3.place(relx=0.8, rely=0.6, anchor=CENTER)

lb4 = Label(pg, text="Jugador 1")
lb4.place(relx=0.2, rely=0.4, anchor=CENTER)

lb5 = Label(pg, text="Jugador 2")
lb5.place(relx=0.8, rely=0.4, anchor=CENTER)

bt1 = Button(pg, image=img, command=fn1)
bt1.place(relx=0.2, rely=0.5, anchor=CENTER)

bt2 = Button(pg, image=img, command=fn2)
bt2.place(relx=0.8, rely=0.5, anchor=CENTER)

pg.mainloop()