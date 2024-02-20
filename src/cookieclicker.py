from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

instructions = '''
Instructions: Click the cookie using your mouse cursor or press SPACE to increase score. 
Click the upgrade button using your mouse cursor or press the "U" key to upgrade clicking power.
Click the second upgrade button using your mouse cursor or press the "I" key to upgrade idle cookie production.
Click the start button or press the "S" key to begin the cookie clicker game.
'''

def clicked(event):
    if event.keysym == 's':
        starting()

init = Tk()
init.config(bg='gray')
init.title('Cookie Clicker')
init.geometry('600x600+10+10')

info = Label(init, bg='gray',text=instructions, justify='center', wraplength=490)
info.pack(fill='x', expand=True)

def starting():
    init.quit()
    # Destroy the current Tkinter window
    init.destroy() 

startfont = font.Font(family='Verdana', size=35, weight='bold')
start = Button(init, bg='gray', text="START", font=startfont, fg='red', command=starting) 
start.place(x=175, y=380)

init.bind("<KeyPress-s>", clicked)

init.mainloop()

#new window
import requests
from io import BytesIO
 
window = Tk()
window.config(bg = "yellow")
# Assign Tk class (the main window of GUI) to variable window
window.title('Cookie Clicker')
window.geometry("640x600+10+10")
# window is 600*600 pixels and situated 10 pixels from top of screen and 10 pixels from left of screen
gold_frame = Frame(window, width=630, height=590, bg="gold")
gold_frame.pack(padx=30, pady=30) 
# If I ever make a tkinter gui lets stick to pack

image_url = "https://assets.stickpng.com/images/580b57fbd9996e24bc43c0fc.png"
response = requests.get(image_url)
window.image_cookie = Image.open(BytesIO(response.content))
# OLD CODE: window.image_cookie = Image.open("/Users/ahmed/OneDrive/Documents/cookiepng.png")
# opens image in PIL... from here a person could use .show() method from Image module

window.resized = window.image_cookie.resize([200, 200])
# resizes image in PIL

window.photoimg = ImageTk.PhotoImage(window.resized)
# convert resized image into PhotoImage class for use in Tkinter

window.clicks = 0

# When you use window.clicks, you are accessing the clicks variable as an attribute of the window object.
# The window object is an instance of the Tk class provided by Tkinter.
# On the other hand a variable named clicks would directly reference the global variable. I could use this but 
# ... using window.clicks can be beneficial in more complex situationswhen you have multiple instances of classes
# ... with similar variable names, as it helps avoid naming conflicts.

window.multiple = 1
window.click_power = 1
window.offer = 2
window.price = 21
window.idle_offer = 2
window.idle_price = 12
window.fullsize = True
window.rotations = 1

import time

window.auto_power = 1
window.auto_increment = 1 * window.auto_power
window.autoscore = 0

def shrink():
    window.resized = window.image_cookie.resize([180, 180])
    window.rotated = window.resized.rotate(20 * window.rotations)
    window.rotations += 1
    window.photoimg = ImageTk.PhotoImage(window.rotated)
    window.cookie_button.config(image = window.photoimg)
    window.cookie_button.place(x=225, y=130)
    window.fullsize = False

def unshrink():
    window.resized = window.image_cookie.resize([200, 200])
    window.rotated = window.resized.rotate(20 * window.rotations)
    window.rotations += 1
    window.photoimg = ImageTk.PhotoImage(window.rotated)
    window.cookie_button.config(image = window.photoimg)
    window.cookie_button.place(x=215, y=125)
    window.fullsize = True
   

def clicked():
    window.clicks += 1 * window.click_power
    window.L.config(text=f'''
Cookies: {window.clicks}
Clicking Power: {window.click_power} Cookies per Click
Idle Cookie Rate: +{window.auto_increment} cookie every 10 seconds ({window.autoscore} cookies from idle production)
''')
    if window.clicks == 10*window.multiple:
        window.multiple += 1
        window.L['text'] += f'''--> Congrats on {window.clicks} clicks'''
    if window.fullsize:
        shrink()
    else:
        unshrink()
    
def upgraded():
    if window.clicks >= window.price:
        window.clicks -= window.price
        window.offer += 1
        window.price *= 3
        window.click_power += 1
        window.upgrade['text'] = f'Buy x{window.offer} click speed for {window.price} points?'
        window.L['text'] = f'''
Cookies: {window.clicks}
Clicking Power: {window.click_power} Cookies per Click
Idle Cookie Rate: +{window.auto_increment} cookie every 10 seconds ({window.autoscore} cookies from idle production)
        '''

def idle_upgraded():
    if window.clicks >= window.idle_price:
        window.clicks -= window.idle_price
        window.idle_offer += 1
        window.idle_price *= 3
        window.auto_power += 1
        window.auto_increment = 1 * window.auto_power
        window.idle_upgrade['text'] = f'Buy x{window.idle_offer} idle cookies per second for {window.idle_price} cookies?'
        window.L['text'] = f'''
Cookies: {window.clicks} 
Clicking Power: {window.click_power} Cookies per Click
Idle Cookie Rate: +{window.auto_increment} cookie every 10 seconds ({window.autoscore} cookies from idle production)
        '''

import subprocess

def onKeyPress(event): # event parameter is essential because it allows your onKeyPress function to access information about the key press event such as which key was pressed, the state of modifier keys (Shift, Control, etc.), ...
    if event.keysym == 'space': # event.keysym to obtain the symbolic name of the key.
        clicked()
    if event.keysym == 'u':
        upgraded()
    if event.keysym == 'i':
        idle_upgraded()
    if event.keysym == 'm':
        subprocess.run(['python', '/code/cookieclickergame/1gameinit.pyt'])

window.cookie_button=Button(window, image=window.photoimg, bg = "yellow", command=clicked,)
window.cookie_button.place(x=215, y=125)

window.upgrade = Button(window, bg = "yellow", text=f'Buy x{window.offer} click speed for {window.price} cookies?', command=upgraded)
window.upgrade.place(x=220, y=450)

window.idle_upgrade = Button(window, bg = "yellow", text=f'Buy x{window.idle_offer} idle cookies per second for {window.idle_price} cookies?', command=idle_upgraded)
window.idle_upgrade.place(x=220-33  , y=490)

window.L = Label(window, bg = "yellow", text=f'''
Cookies: {window.clicks}
Clicking Power: {window.click_power} Cookies per Click
Idle Cookie Rate: +{window.auto_increment} cookie every 10 seconds ({window.autoscore} cookies from idle production)
''')
window.L.place(x=110, y=50)

window.help_label = Label(window, bg = 'yellow', text='Need help? Press "M" on your keyboard.')
window.help_label.place(x=30,y=555)

window.bind('<KeyPress-space>', onKeyPress)
window.bind('<KeyPress-u>', onKeyPress)
window.bind('<KeyPress-i>', onKeyPress)
window.bind('<KeyPress-m>', onKeyPress)

def auto_increment():
    window.clicks += window.auto_increment
    window.autoscore += window.auto_increment
    window.L.config(text=f'''
Cookies: {window.clicks}
Clicking Power: {window.click_power} Cookies per Click
Idle Cookie Rate: +{window.auto_increment} cookie every 10 seconds ({window.autoscore} cookies from idle production)
''')
    window.after(10000, auto_increment)  # Schedule the function to run again after 1000 milliseconds (1 second)

window.after(10000, auto_increment)  # Start the auto_increment function after 1000 milliseconds

window.mainloop()
