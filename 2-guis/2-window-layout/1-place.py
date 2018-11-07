from gui import Gui

# create the window object
gui = Gui()
gui.mainloop()




from tkinter import *

class Gui(Tk):

    # initialize the object
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="#eee",
                       height=300,
                       width=500)

        #add components/widgets
        self.add_heading_label()
        self.add_instruction_label()
        self.add_addres_label()
        self.add_bottom_button()
        

    def add_heading_label(self):   
        # 1. create the component object
        self.heading_label = Label()
        self.heading_label.place(x=100, y=10)
        # 2. style the component
        self.heading_label.configure(font="Arial 16",
                                     text="RECEIVE OUR NEWSLETTER")

    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.place(x=80, y=80)
        self.instruction_label.configure(font="Arial 10",
                                  text="Please enter your email below to receive our newsletter")
        
    def add_addres_label(self):
        self.addres_label = Label()
        self.addres_label.place(x=100, y=200)
        self.addres_label.configure(font="Arial 12",
                                         text="Email:")

    def add_bottom_button(self):
        self.bottom_button = Label()
        self.bottom_button.place(x=200, y=250)
        self.bottom_button.configure(font="Arial 12",
                                     text="Subscribe")
    

        
