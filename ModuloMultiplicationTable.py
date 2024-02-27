import random
from tkinter import *

root = Tk( )
# Modulo
Z = 2


# Grid Size
startFromZero = True
S = 2 #Size
height = 1
widht = 2



def GridMaker(x:str, r:int, c:int, colour): Button(root, text=str(x), fg='black', bg=colour, borderwidth=2, height=height, width=widht).grid(row=r,column=c)
def random_color(): return '#{0:02x}{1:02x}{2:02x}'.format(*[random.randint(150, 255) for _ in range(3)])


colors = [random_color() for _ in range(Z)]

if startFromZero == True:
    S += 1
    startFromZero = -1
else:
    startFromZero = 0
for r in range(S):
    for c in range(S):        
        if r == 0:
            if c == 0:
                GridMaker("*", r, c, "grey50")
            else:
                GridMaker((c+startFromZero), r, c, "grey50")
        elif c == 0:
            GridMaker(r+startFromZero, r, c, "grey50")
        else:
            GridMaker(((r-startFromZero)*(c-startFromZero)) % Z, r, c, str(colors[(((r-startFromZero)*(c-startFromZero))%Z)])) 
root.mainloop()
