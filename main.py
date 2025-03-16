import tkinter as tkr
from tkinter import simpledialog
import FUNCIONESS as fun
from FUNCIONESS import mayoria_de_edad2, mayoria_de_edad

base = tkr.Tk()
base.title("djfngdher")

nom= simpledialog.askstring("nombre","Digite su nombre:")
ed= simpledialog.askinteger("edad","digite su edad:")
RR=fun.mayoria_de_edad(nom,ed)
usar_label = tkr.Label(base,text=RR,font=("arial",14))
usar_label.pack(pady=30)

base.mainloop()
print(fun.mayoria_de_edad(nom,ed))
