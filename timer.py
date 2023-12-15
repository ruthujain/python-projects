from tkinter import Tk
from tkinter import Label#label is a function where we can write ont he tk window
import time
root=Tk()
root.title("CLOCK")
def present_time():
    display_time=time.strftime("%I:%M:%S %p")#%I is used if we want the time to be displayef in 1,2,3.. %H for 13,14,..and %M is for mins and %p is for pm or am
    digi_clock.config(text=display_time)
    digi_clock.after(200,present_time)#200milliseconds 
digi_clock= Label(root,font=("arial",200),bg="lightpink",fg="black")#font,forntsize,fg-fontcolor
digi_clock.pack()
present_time()#calling of a function
root.mainloop()