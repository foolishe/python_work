import tkinter

top = tkinter.Tk()
quit = tkinter.Button(top,text='QUIT',command=top.quit,bg='red',fg='white')
hello = tkinter.Label(top,text='Hello World')
hello.pack(),quit.pack(fill=tkinter.X,expand=1)

tkinter.mainloop()
