from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('Calculator')
GUI.geometry('500x300')


bg = PhotoImage(file='guical01.png')
BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI, text='input amount of fish', font=(None, 20))
L.pack()

v_quantity = StringVar()				# เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None, 20))
E1.pack()

def Cal():
	try:
		quan = float(v_quantity.get())
		calc = quan * 50					#50 bath / kg
		messagebox.showinfo('total', 'total {} bath'.format(calc))
		E1.focus()
	except:
		messagebox.showwarning('wrong input', 'input integer only')
		v_quantity.set('1')

B = ttk.Button(GUI, text='calculate', command=Cal)
B.pack(ipadx=30, ipady=20)

GUI.mainloop()