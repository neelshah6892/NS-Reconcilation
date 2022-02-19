from tkinter import *
import tkinter.messagebox as tkMessageBox
from tkinter import filedialog
import tkinter.ttk as ttk
import pandas as pd
import tkintertable
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import xlrd

root = Tk()
root.title("Reconcilation")

width = 1200
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#99ff99")

def twoa():
	#global df1
	file1 = filedialog.askopenfilename()
	df1 = pd.read_excel(file1, sheet_name='Sheet1')
	df1.parse('Sheet1')
    #df1.head()
    #df1.shape()
	#df1 = pd.DataFrame(file1)

def inward():
	#global df2
	file2 = filedialog.askopenfilename()
	df2 = pd.read_excel(file2, sheet_name="Sheet1")
            
    
def merge():
    df = pd.concat([df1,df2])
	#print(df.shape())
    #df.tail()

def reset():
    df = pd.concat([df1,df2])
    #print(df.shape())
	#df.tail()

# def pan():



# ===Charts===# List Widget



#===Frames===#
Top = Frame(root, width=1200, height=100, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=790, height=550, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=390, height=550, relief="raise")
Right.pack(side=RIGHT)
Buttons = Buttons = Frame(Top, width=300, height=100, relief="raise")
Buttons.pack()

# ===Table===# Entry Widgets
'''nb = ttk.Notebook(Left)
nb.grid(row=1, column=0, colspan = 50, rowspan= 49, sticky="NESW")
tab1 = ttk.Frame(nb)
nb.add(tab1, text="Main")
tab2 = ttk.Frame(nb)
nb.add(tab2, text="GSTIN")
tab3 = ttk.Frame(nb)
nb.add(tab3, text="Pan")
tab4 = ttk.Frame(nb)
nb.add(tab4, text="Final")'''

#===Button Widgets===#
btn1 = Button(Buttons, width=30, text="DATABASE 1", command=twoa)
btn1.pack(side=LEFT)
btn2 = Button(Buttons, width=30, text="DATABASE 2", command=inward)
btn2.pack(side=LEFT)
btn3 = Button(Buttons, width=30, text="START", command=merge)
btn3.pack(side=LEFT)
btn4 = Button(Buttons, width=30, text="RESET", command=reset)
btn4.pack(side=LEFT,)

#===MENUBAR===#
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="DATABASE 1")
menubar.add_cascade(label="File")
menubar.add_cascade(label="Edit")
root.config(menu=menubar)

#===Main Screen Label===#
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

#===Initialization===#
if __name__ == '__main__':
    root.mainloop()
