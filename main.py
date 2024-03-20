# ------------- Import ----------------
import random
import tkinter.messagebox
from tkinter import *

# ------------- Variable ----------------
MoveGame = ['rock', 'paper', 'sicssor']
P1W = 0
P2W = 0
Win = 4

# ------------- Function ----------------
def Game(Moveuser):
    global Win, P1W, P2W, MovePcM, MoveUserM
    MoveM.config(text="...")
    PC = random.choice(MoveGame)
    USER = Moveuser
    if USER == PC:
        MoveM.config(text="Equal")
        if USER == 'rock':
            MovePcM.config(image=RockL)
            MoveUserM.config(image=RockR)
        elif USER == 'paper':
            MovePcM.config(image=PaperL)
            MoveUserM.config(image=PaperR)
        elif USER == 'sicssor':
            MovePcM.config(image=ScissorL)
            MoveUserM.config(image=ScissorR)
    elif USER == 'rock':
        MoveUserM.config(image=RockR)
        if PC == 'sicssor':
            MovePcM.config(image=ScissorL)
            MoveM.config(text="Win")
            P1W += 1
        elif PC == 'paper':
            MovePcM.config(image=PaperL)
            MoveM.config(text="Loss")
            P2W += 1
    elif USER == 'paper':
        MoveUserM.config(image=PaperR)
        if PC == 'rock':
            MovePcM.config(image=RockL)
            MoveM.config(text="Win")
            P1W += 1
        elif PC == 'sicssor':
            MovePcM.config(image=ScissorL)
            MoveM.config(text="Loss")
            P2W += 1
    elif USER == 'sicssor':
        MoveUserM.config(image=ScissorR)
        if PC == 'paper':
            MovePcM.config(image=PaperL)
            MoveM.config(text="Win")
            P1W += 1
        elif PC == 'rock':
            MovePcM.config(image=RockL)
            MoveM.config(text="Loss")
            P2W += 1
    PWLable.config(text=f"User: {P1W}          Pc: {P2W}")
    if int(P1W) == int(Win) or int(P2W) == int(Win):
        if int(P1W) == int(Win):
            tkinter.messagebox.showinfo(title="Final result", message="You Won")
            MoveM.config(text="")
            P1W = 0
            P2W = 0
            PWLable.config(text=f"User: {P1W}          Pc: {P2W}")
            MovePcM.config(image=NULLP)
            MoveUserM.config(image=NULLP)
            return
        elif int(P2W) == int(Win):
            tkinter.messagebox.showerror(title="Final result", message="You Lost")
            MoveM.config(text="")
            P1W = 0
            P2W = 0
            PWLable.config(text=f"User: {P1W}          Pc: {P2W}")
            MovePcM.config(image=NULLP)
            MoveUserM.config(image=NULLP)
            return

# ------------- Setting ----------------
Windows = Tk()
Windows.resizable(False, False)
Windows.title("Rock - Paper - Scissor")

# ------------- Photo ----------------
RockR = PhotoImage(file=r"Photo\RockR.png").subsample(10, 10)
RockL = PhotoImage(file=r"Photo\RockL.png").subsample(10, 10)
PaperR = PhotoImage(file=r"Photo\PaperR.png").subsample(10, 10)
PaperL = PhotoImage(file=r"Photo\PaperL.png").subsample(10, 10)
ScissorR = PhotoImage(file=r"Photo\ScissorR.png").subsample(10, 10)
ScissorL = PhotoImage(file=r"Photo\ScissorL.png").subsample(10, 10)
NULLP = PhotoImage(file=r"Photo\NULL.png").subsample(10, 10)

# ------------- Label ----------------
PWLable = Label(Windows, font=('arial', 15, 'bold'), text=f"User: {P1W}          Pc: {P2W}")
PWLable.grid(columnspan=4)
MoveUserM = Label(Windows, font=('arial', 15, 'bold'),image= NULLP, compound=LEFT)
MoveUserM.grid(row=2, column=0)
MovePcM = Label(Windows, font=('arial', 15, 'bold'),image= NULLP, compound=RIGHT)
MovePcM.grid(row=2, column=2)
MoveM = Label(Windows, font=('arial', 15, 'bold'), text="")
MoveM.grid(columnspan=4)

# ------------- Button ----------------
btn1 = Button(Windows, bd=5, command=lambda: Game('rock'), image=RockR, compound=CENTER)
btn1.grid(row=4, column=0, )
btn2 = Button(Windows, bd=5, command=lambda: Game('paper'),image=PaperR, compound=CENTER)
btn2.grid(row=4, column=1)
btn3 = Button(Windows, bd=5, command=lambda: Game('sicssor'), image=ScissorR, compound=CENTER)
btn3.grid(row=4, column=2)

# ------------- Run ----------------
Windows.mainloop()