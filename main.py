#Digital Clock

from tkinter import *
from tkinter import messagebox
from time import strftime


if __name__ == '__main__':
    # FUNCTIONS >>>

    # Clock Function
    def clock():
        # Time
        hr = strftime('%H')
        if int(hr) > 12:
            hr = int(hr)-12
        time_line = strftime(f'{hr}:%M:%S %p')
        time.config(text=time_line)
        time.after(200,clock)

        # Date
        year = str(20)
        date_line = strftime(f'%d/%m/{year}%y %a')
        date.config(text=date_line)
        date.after(50000,clock)

    # Functions for buttons >>>
    def lightMode():
        root.config(bg='white')
        title.config(bg='white', fg='black')
        time.config(bg='white', fg='black')
        date.config(bg='white', fg='black')
        r1.config(bg='white', fg='black')
        r2.config(bg='white', fg='black')
        b1.config(bg='white', fg='black')
        b2.config(bg='white', fg='black')
        
    
    def darkMode():
        root.config(bg='black')
        title.config(bg='black', fg='cyan')
        time.config(bg='black', fg='cyan')
        date.config(bg='black', fg='cyan')
        r1.config(bg='black', fg='white')
        r2.config(bg='black', fg='white')
        b1.config(bg='black', fg='white')
        b2.config(bg='black', fg='white')

    
    def about():
        return messagebox.showinfo('About', 'Digital Clock by Hassan Khan.')
    
    def close():
        choice = messagebox.askquestion('Digital Clock', 'Are you sure you want to close?')
        if choice == 'Yes' or choice == 'yes':
            root.destroy()
        else:
            return
    
    # Tkinter GUI code>>>
    root = Tk()
    root.title("Digital Clock")
    image_icon = PhotoImage(file='logo.png')
    root.iconphoto(False, image_icon)
    root.geometry('700x380')
    root.resizable(False,False)
    root.config(bg="white")
    title = Label(root,text="Digital Clock",font="Forte 70", bg="white")
    title.pack(side=TOP)

    timeFrame = Frame(root).pack(pady=10)
    # Time_line
    time = Label(timeFrame, text="12" ,font="digital-7 70 bold", bg="white", fg='black')
    time.pack()

    # Date_line
    date = Label(timeFrame, text="12" ,font="digital-7 70 bold", bg="white", fg='black')
    date.pack()

    # Bottom Menu
    bottomWindow = Frame(root).pack(pady=10,side=BOTTOM)
    var = IntVar()

    r1 = Radiobutton(bottomWindow,text="Light Mode", variable=var, value=0, command=lightMode,bg="white", fg='black')
    r1.pack(padx=10,side=LEFT)

    r2 = Radiobutton(bottomWindow,text="Dark Mode", variable=var, value=1, command=darkMode, bg="white", fg='black')
    r2.pack(padx=10,side=LEFT)

    b1 = Button(bottomWindow,text="About", command=about, bg="white", fg='black')
    b1.pack(padx=10,side=LEFT)

    b2 = Button(bottomWindow,text="Close", command=close, bg="white", fg='black')
    b2.pack(padx=10,side=LEFT)


    # running clock function and GUI graphics...
    clock()
    root.mainloop()