from tkinter import Button,END,Label,W,Tk
from Pmw import initialise,ComboBox,Counter

top = Tk()#initialise()

label = Label(top,text='Animals (in pairs;min:pair,max:dozen)')
label.pack()

ct = Counter(top,labelpos=W,label_text='Number:',datatype='integer',
    entryfield_value=2,
    increment=2,
    entryfield_validate={'validator':
    'integer','min':2,'max':12})
ct.pack()

cb = ComboBox(top,labelpos=W,label_text='type:')
for animal in ('dog','cat','hamster','python'):
    cb.insert(END,animal)
cb.pack()

qb = Button(top,text='QUIT',command=top.quit,bg='white',fg='red')
qb.pack()

top.mainloop()
