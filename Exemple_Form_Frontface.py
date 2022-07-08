from tkinter import *

window = Tk()

window.title('User Form')
window.geometry('500x350+500+200')
window.resizable(height=False, width=False)
window.iconbitmap('forms.ico')
window.configure(bg='#D7C6EE')

frame1 = Frame(window, bg='#D7C6EE')
frame1.grid(row=0, column=0)
frame2 = Frame(window, bg='#D7C6EE')
frame2.grid(row=0, column=1)
frame3 = Frame(window, bg='#D7C6EE')
frame3.grid(row=0, column=2)
frame4 = Frame(window, bg='#D7C6EE')
frame4.grid(row=1, column=2)
frame5 = Frame(window, bg='#D7C6EE')
frame5.place(x=0, y=240)

Label(frame1, text='Name', font=('Arial 12 bold'), bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame1, text='Surname', font=('Arial 12 bold'), bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame1, text='Age', font=('Arial 12 bold'), bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame1, text='Birth', font=('Arial 12 bold'), bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame1, text='Gender', font=('Arial 12 bold'), bg='#D7C6EE', padx=5, pady=5).pack()

Label(frame2, text=':', font=('Arial 12 bold'), bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame2, text=':', font=('Arial 12 bold'), bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame2, text=':', font=('Arial 12 bold'), bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame2, text=':', font=('Arial 12 bold'), bg='#D7C6EE', padx=5, pady=5).pack()
Label(frame2, text=':', font=('Arial 12 bold'), bg='#D7C6EE', padx=5, pady=5).pack()

Entry(frame3, font=('Arial 12 bold'), bg='#ECE8F0', justify='center').pack(padx=5, pady=5)
Entry(frame3, font=('Arial 12 bold'), bg='#ECE8F0', justify='center').pack(padx=5, pady=5)

Button(window, text='Save', font=('Arial 13 bold'), bg='green', width=12).place(x=100, y=270)
Button(window, text='Clean', font=('Arial 13 bold'), bg='yellow', width=12).place(x=260, y=270)

photo=PhotoImage(file='user.png')
photoResized=photo.subsample(4, 4)
Button(window, text='Upload', image=photoResized, compound=TOP).place(x=325, y=11)

Spinbox(frame3, from_=18, to=60, font=('Arial 12 bold'), bg='#ECE8F0', justify='center', width=19).pack(padx=5, pady=5)

optionList=[
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'Oktober',
    'November',
    'December',
]
sval = StringVar(frame3)
sval.set(optionList[0])
opm1 = OptionMenu(frame3, sval, *optionList)
opm1.config(width=18, font=('Arial 11 bold'), bg='#ECE8F0', justify='center')
opm1.pack(padx=5, pady=5)

ivar = IntVar()
def sel():
    selection = 'Selected radiobutton val = ' + str(ivar.get())
    print(selection)

rdb1 = Radiobutton(frame3, text='Male', variable=ivar, value=1, command=sel, font=('Arial 11 bold'), bg='#ECE8F0')
rdb2 = Radiobutton(frame3, text='Female', variable=ivar, value=2, command=sel, font=('Arial 11 bold'), bg='#ECE8F0')
rdb1.pack(side='left', padx=5, pady=5)
rdb2.pack(side='right', padx=5, pady=5)

cb1 = Checkbutton(frame4, text='I have read the form. I Approve', font=('Arial 10 bold'), bg='#ECE8F0')
cb1.pack(padx=5, pady=10)

cv1= Canvas(frame5, width=400, height=3, bg='#D7C6EE', highlightthickness=0)
cv1.create_line(100,2,390,2)
cv1.pack()

menubar = Menu(window)
filemenu= Menu(menubar, tearoff=0, font=('Arial 10 bold'))
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save As')
filemenu.add_separator()
filemenu.add_command(label='Close')
menubar.add_cascade(label='File', menu=filemenu)

helpmenu= Menu(menubar, tearoff=0, font=('Arial 10 bold'))
helpmenu.add_command(label='About')
menubar.add_cascade(label='Help', menu=helpmenu)


window.config(menu=menubar)
window.mainloop()