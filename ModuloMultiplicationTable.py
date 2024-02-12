from tkinter import *
root = Tk( )
# Modulo
Z = 4

def GridMaker(x:str, r:int, c:int, colour:str): Button(root, text=str(x), fg='black', bg=colour, borderwidth=2, height= 3, width= 6 ).grid(row=r,column=c)


for r in range(1, Z+1):
    for c in range(1, Z+1):        
        if r == 1:
            if c == 1:
                GridMaker("", r, c, "grey50")
            else:
                GridMaker(c-1, r, c, "grey50")
        elif c == 1:
            GridMaker(r-1, r, c, "grey50")
        else:
            GridMaker(((r-1)*(c-1)) % Z, r, c, "grey50")
root.mainloop()