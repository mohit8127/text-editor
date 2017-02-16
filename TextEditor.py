import Tkinter
from Tkinter import *
#import Scrolled because tk has not this scrolling.
from ScrolledText import *
import tkFileDialog
import tkMessageBox

root = Tkinter.Tk(className="Text Editor")
textPad = ScrolledText(root, width=100, height=80)
# we adding fundamental feature in text editor
# create a menu & define functions for each menu item

# define open command in menu
def open_command():
    file = tkFileDialog.askopenfile(parent=root, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        textPad.insert('1.0', contents)
        file.close()

# define save command in menu
def save_command(self):
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        # slice off the last character from get, as an save to return
        data = self.textPad.get('1.0', END + '-1c')
        file.write(data)
        file.close()

# define exit command in menu
def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

# define about command in menu
def about_command():
    label = tkMessageBox.showinfo("About", "Rahul Chauhan")


def dummy():
    print " Hello World "


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=dummy)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)

#
textPad.pack()
root.mainloop()
