import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import colors

class Notepad:
    __root = Tk()
    __thisWidth = 300
    __thisHeigth = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar.config(background=colors.DARK_GREY), tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    
    
    # Add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    # Set icon
    def __init__(self, **kwargs):
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set window size (default 300x300)        
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass
        try:
            self.__thisHeigth = kwargs['heigth']
        except KeyError:
            pass
        # Set window text   
        self.__root.title("Untitled - Notepad")

        # Center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeigth = self.__root.winfo_screenheight()

        # Left-rigth align
        left = (screenWidth / 2) - (self.__thisWidth / 2)
        # Top and Bottom align
        top = (screenHeigth / 2) - (self.__thisWidth / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeigth, left, top))

        # Make trextArea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        
        # Add controls(widget)
        self.__thisTextArea.grid(sticky=N + E + S + W)


        # To open new file
        self.__thisFileMenu.add_command(label="New", command=self.__newFile)
        # To open an existing file
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)
        # To save current file
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)

        # To create a line in the dialog
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit", command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu, activeforeground=colors.LIGHT_BLUE, activebackground=colors.GREY, foreground=colors.BLUE, background=colors.GREY)

        # To give a feature of cut
        self.__thisEditMenu.add_command(label="Cut", command=self.__cut)
        # To give a feature of copy
        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)
        # To give a feature of paste
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)
        # To give a feature of editing
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu, activeforeground=colors.LIGHT_BLUE, activebackground=colors.GREY, foreground=colors.BLUE, background=colors.GREY)

        # To create a feature of description of the notepad
        self.__thisHelpMenu.add_command(label="About Notepad", command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu, activeforeground=colors.LIGHT_BLUE, activebackground=colors.GREY, foreground=colors.BLUE, background=colors.GREY)
        self.__root.config(menu=self.__thisMenuBar)
        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        # Scrollbar will adjust automatically accordin to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()

    def __showAbout(self):
        showinfo("Notepad", "Note pad using python3 and tkinter")

    def __openFile(self):
        self.__file =askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.__file == "":
            # No file to open
            self.__file = None
        else:
            # Try to open the file
            # Set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)
            file = open(self.__file, "r")
            self.__thisTextArea.insert(1.0, file.read())
            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):
        if self.__file == None:
            #save as a new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            
            if self.__file == "":
                self.__file = None
            else:
                # Try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                # Change the windo title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
        else:
             file = open(self.__file, "w")
             file.write(self.__thisTextArea.get(1.0, END))
             file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>") 

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):
        # Run main app
        self.__root.mainloop()

#Run main app          
notepad = Notepad(width=600, heigth=400)
notepad.run()