#controlmouse.py

from tkinter import *
from tkinter import ttk
import pyautogui as pg
import webbrowser

GUI = Tk()
GUI.title('Clendar Checking Program')
GUI.geometry('500x300')

def Calendar():
    pg.click(1794, 1063)

def Google():
    webbrowser.open('https://www.google.com')

B1 = Button(GUI, text='Calendar', command=Calendar)
B1.pack(ipadx=20, ipady=10, pady=20)

B2 = ttk.Button(GUI,text='Google', command=Google)
B2.pack(ipadx=20, ipady=10, pady=20)

GUI.mainloop()