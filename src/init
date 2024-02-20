from tkinter import Tk, Label, Button, font

instructions = '''
Instructions: Click the cookie using your mouse cursor or press SPACE to increase score. 
Click the upgrade button using your mouse cursor or press the "U" key to upgrade clicking power.
Click the start button or press the "S" key to begin the cookie clicker game.
'''

def starting():
    # Destroy the current Tkinter window
    init.destroy()

def clicked(event):
    if event.keysym == 's':
        starting()

init = Tk()
init.title('Cookie Clicker')
init.geometry('500x500+10+10')

info = Label(init, text=instructions, justify='center', wraplength=490)
info.pack(fill='x', expand=True)

startfont = font.Font(family='Verdana', size=35, weight='bold')
start = Button(init, text="START", font=startfont, fg='red', command=starting) 
start.place(x=125, y=380)

init.bind("<KeyPress-s>", clicked)

init.mainloop()
