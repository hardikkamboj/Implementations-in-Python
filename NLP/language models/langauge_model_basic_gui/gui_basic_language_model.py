from basic_language_model import gen_sentence
import tkinter
from tkinter import Button,Label,messagebox,Entry

window = tkinter.Tk()

window.title('GUI')

def click_fn():
	sent = gen_sentence(txt.get())
	messagebox.showinfo('Generated sentence is',sent)

txt = Entry(window,text = 'Enter the first two words',width = 10)
txt.grid(column=0,row=0)


Button(window,text = 'Generate sentence',command = click_fn,bg = 'black',fg = 'white').grid(column = 1,row=0)


window.geometry('600x400')

window.mainloop()