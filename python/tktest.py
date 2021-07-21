from tkinter.ttk import *		#imports all objects from ttk library
from tkinter import *    #importing all objects in tkinter module
from tkinter import scrolledtext		#import scrolled text library
from tkinter import messagebox			#imports message box library
from tkinter.ttk import Progressbar		#imports progressbar library

window = Tk()
window.title("Testing Gui Code") 	#sets window title
window.geometry('580x900')		#describes window's dimensions'
combo = Combobox(window)		#defines a combobox, like a select drop-down menu

lbl = Label(window, text="Hello World!", font=('times new roman', 14) )    	#declaring a label
lbl.grid(column=0, row=0)		#must set grid position to see object. !.Sequence starts from 0,0

txt = Entry (window, width = 20)			#accept user entry
txt.grid ( column = 1, row = 0)
txt.focus() #focuses on column to allow immediate typing

def clicked():
	'''it handles event when clicked'''
	res = txt.get()
	lbl.configure ( text = res )
	btn.configure ( text = 'Clicked', command = touch )
	#configure alters and updates settings of objects

btn = Button(window, text = 'Click Me!', bg= 'black', fg = 'white', command = clicked)		#creating a button
#command attribute accepts name of function that handles object events
#state = 'disabled' or 'enabled' used to handle widgets
btn.grid(column=0, row=1)

combo['values'] = ( 1, 2, 3, 4, 5, 'text' )		#initializing values
combo.current(5)		#sets selected item on display using Indexing
combo.grid( column = 0, row = 3)
#combo.get() ----> returns the selected item

chk_state = IntVar()
chk_state.set(0) #uncheck; 1 --> check
chk = Checkbutton( window, text = 'choice', var = chk_state )		#declares a checkbox
chk.grid( column = 0, row = 4)

#declaring radio buttons
selected = IntVar()
rad1 = Radiobutton( window, text = 'First', value = 1 , var = selected )
rad2 = Radiobutton( window, text = 'Second', value = 2, var = selected)
rad3 = Radiobutton( window, text = 'Third', value = 3, var = selected)
rad1.grid( column = 0, row = 5 )
rad2.grid( column = 0, row = 6 )
rad3.grid( column = 0, row = 7 )

#declaring a textarea
ter = scrolledtext.ScrolledText( window, width = 40, height = 10 )
ter.insert( INSERT, 'Your text goes here' )		#set textarea content like a placeholder in html
ter.grid( column = 3, row = 3 )

#showing a message box
# --> messagebox.showinfo( 'Title', 'content' )  --> displays info
# --> messagebox.showwarning( 'Title', 'content' )
# --> messagebox.showerror( 'Title', 'content' )
''' ok, yes and retry returns True.
   no and cancel returns False.
# --> messagebox.askquestion( 'Title', 'content' )
# --> messagebox.askyesno( 'Title', 'content' )
# --> messagebox.askyesnocancel( 'Title', 'content' )
# --> messagebox.askokcancel( 'Title', 'content' )
# --> messagebox.askretrycancel( 'Title', 'content' )
'''
def touch():
	messagebox.showwarning( 'Title', 'content' )

#declaring spinbox(number widget)
spin = Spinbox( window, from_ = 0, to = 100, width = 10 )
spin.grid( column = 0, row = 8 )
'''
values=(x, y, z) --> to specify range of values
To set the Spinbox default value, you can pass the value to the [ textvariable = var ] parameter
'''

#declaring a progress bar
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 85
bar.grid( column = 1, row = 8 )

#declaring a file dialog( file and directory chooser )


window.mainloop()		#this allows continues view of window