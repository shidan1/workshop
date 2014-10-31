import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Menu
import tkinter.scrolledtext as tkst
from tkinter.constants import END
from Project.Evaluate import evaluate

root = tkinter.Tk(className=" Workshop: Compile-time techniques for detecting JavaScript exploits")
textPad = tkst.ScrolledText(root, width=100, height=40, padx=5, pady = 5, highlightthickness=3, bg = "LightSteelBlue1")
global currentFile

# create a menu & define functions for each menu item
 
# NEW FILE 
def new_command():
    root.title(" Workshop: Compile-time techniques for detecting JavaScript exploits")
    textPad.delete("1.0",END)
 
# OPEN FILE
def open_command():
    file = filedialog.askopenfile(parent=root,mode='rb',title='Select a file')
    global currentFile 
    currentFile = file.name
    if file != None:
        root.title(file.name)
        contents = file.read()
        textPad.insert('1.0',contents)
        file.close()

# SAVE CURRENT FILE
def save_command():
    file = open(currentFile, "w")
    data = textPad.get("1.0",END+'-1c')
    file.write(data)
    file.close()

# SAVE TO FILE
def save_as_command():
    file = filedialog.asksaveasfile(mode='w')
    global currentFile 
    currentFile = file.name
    if file != None:
        root.title(file.name)
        data = textPad.get("1.0",END+'-1c')
        file.write(data)
        file.close()

# DETECT MALICIOUS CODE   
def detect_command():
        script = textPad.get("1.0",END+'-1c')
        result = evaluate(script)
        if result[0] == 1.0:
            message = "This script is clean of malicious activity"
        if result[0] == -1.0:
            message = "This script has some sort of maliciousness"
        else:
            message = "Error"
        messagebox.showinfo("Results", message)  

# EXIT THE PROGRAM
def exit_command():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

# CUT TEXT
def cut():        
    try:
        selection = textPad.get(*textPad.tag_ranges('sel'))
        textPad.clipboard_clear()
        textPad.clipboard_append(selection)
        textPad.delete(*textPad.tag_ranges('sel'))
    except TypeError:
        pass

# COPY TEXT 
def copy():
    try:
        selection = textPad.get(*textPad.tag_ranges('sel'))
        textPad.clipboard_clear()
        textPad.clipboard_append(selection)
    except TypeError:
        pass

# PASTE TEXT  
def paste():  
    textPad.insert('insert', textPad.selection_get(selection='CLIPBOARD'))

# SELECT ALL 
def select_all():
    textPad.tag_add('sel', '1.0', 'end-1c')

# CLEAR ALL
def clear_all():
    if messagebox.askokcancel("Clear All", "Do you want to erase all text?"):
        textPad.delete('1.0', 'end')

# ABOUT US
def about_command():
    messagebox.showinfo("About", " Copyright \N{COPYRIGHT SIGN} \n All Rights Reserved to: \n Daniel Strokovsky \n Idan Sharon")  
 
# create menus
menu = Menu(root)
root.config(menu=menu)

# Adding FILE menu with options: New, Open, Save, Save As, Exit, and the main option: Detect Malicious Code
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_command)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_command(label="Save As...", command=save_as_command)
filemenu.add_separator()
filemenu.add_command(label="Detect Malicious Code", command=detect_command, background="blue")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command, accelerator="Command-Q")

# Adding EDIT menu with option: Cut, Copy, Paste, Select All
editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label='Cut', command=cut, accelerator="Command-X")
editmenu.add_command(label='Copy', command=copy, accelerator="Command-C")
editmenu.add_command(label='Paste', command=paste, accelerator="Command-V")
editmenu.add_separator()
editmenu.add_command(label='Select All', command=select_all, accelerator="Command-A")
editmenu.add_command(label='Clear All', command=clear_all, accelerator="Command-W")

# Adding HELP menu with About option
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)
 
textPad.pack()
root.mainloop()