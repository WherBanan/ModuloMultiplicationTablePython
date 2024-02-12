from tkinter import *
root = Tk( )
# Modulo
Z = 4

# Grid Size
S = 8

def GridMaker(x:str, r:int, c:int, colour:str): Button(root, text=str(x), fg='black', bg=colour, borderwidth=2, height= 3, width= 6 ).grid(row=r,column=c)


for r in range(S):
    for c in range(S):        
        if r == 0:
            if c == 0:
                GridMaker("", r, c, "grey50")
            else:
                GridMaker(c, r, c, "grey50")
        elif c == 0:
            GridMaker(r, r, c, "grey50")
        else:
            GridMaker((r*c) % Z, r, c, "white")
root.mainloop()
