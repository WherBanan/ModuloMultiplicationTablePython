import random
from tkinter import *

root = Tk( )
# Modulo
Z = 6

# Grid Size
S = 12
height = 1
widht = 2

def GridMaker(x:str, r:int, c:int, colour): Button(root, text=str(x), fg='black', bg=colour, borderwidth=2, height=height, width=widht).grid(row=r,column=c)
def RandomColor(): return '#{0:02x}{1:02x}{2:02x}'.format(*[random.randint(150, 255) for _ in range(3)])


colors = [RandomColor() for _ in range(Z)]

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
            GridMaker((r*c) % Z, r, c, str(colors[((r*c)%Z)]))
root.mainloop()
