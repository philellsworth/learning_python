'''
    tkinter is a module.
    The tkinter module defines types Tk and Label among others.
    
    When the name of the type Label is used as a function,
    python:
       (1) Creates an object of type Label
       (2) Calls the Label type's __init__() function
    Label.__init(Parent,Text):
       (1) Assigns the Object to a Parent
       (2) Assigns a string as the Label Object's text
    Label.pack():
       requests tkinter's "packer geometry manager" arrange the Label object
       within its Container / Parent / Master Window
    Label.mainloop()
       (1) Asks tkinter display the main window
       (2) Start tkinter's event loop
    When the name of the type Tk is used as a function,
    python creates an object of type Tk.

    the module tkinter automatically creates an object of type Tk as the default parent for a widget:
       (1) When the widget creating function is not called with a parent
       (2) When the widget creating function is called with a parent of None
'''
def Hello00():
    from tkinter import Label                       # Tell Python to Make tkinter's Label Function Available
    
    LabelWidget = Label(None, text='Hello World!')  # Set LabelWidget to a Label Object and run tkinter.Label.__init__() on it.
    LabelWidget.pack()                              # LabelWidget Requests Arrangement in Container/Parent/Master Window
    LabelWidget.mainloop()                          # LabelWidget Requests tkinter Display Main Window & Start Event Loop

def Hello01():
    import tkinter                                          # Get Access to all of tkinter via the module interface
    LabelWidget = tkinter.Label(None, text='Hello World!')  # Since we didn't import it directly, access to Label is through the module
    LabelWidget.pack()
    LabelWidget.mainloop()

from tkinter import *                           # Get Direct access to all of tkinter's types   
def Hello02():
    ParentWindow = Tk()                             # Set ParentWindow to the Tk Object and run tkinter.Tk.__init__() on it   
    '''
    In the Following Line:
       (1) Using Label's type name as a function:
          (a) Makes an object of type Label
          (b) Calls the nameless Label's __init__() function, which:
             (*) Set's the Label's parent to ParentWindow
             (*) Set's the Label's text to a string
         (c) Returns a Reference to the Nameless Label
       (2) Since the Label Object is instantiated,
           we can use its member function pack(),
           which asks tkinter to arrange it in its containing window
       
    '''
    Label(ParentWindow, text='Hello World!').pack(side=TOP) # Create Object of type Label, Make its container ParentWindow, Request Packer Arrangement
    ParentWindow.mainloop()                                 # ParentWindow Requests tkinter Display Main Window & Start Event Loop
'''
The Next One is about as minimal as you can get,
relying on default behaviours and importing only what's used  
'''
def Hello03():
    from tkinter import Label                       # Tell Python to Make tkinter's Label Function Available
    Label(text='Hello World!').pack()               # Assign Object of type Label to Automatic Tk Container, and Request Packer Arrangement
    mainloop()                                      # Automatic Tk Object Requests Display Main Window and Start Event Loop
Hello03()
