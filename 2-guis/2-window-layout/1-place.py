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

        

    def add_heading_label(self):   
        # 1. create the component object
        self.heading_label = Label()
        self.heading_label.place(x=2, y=5)
        # 2. style the component
        self.heading_label.configure(font="Arial 18",
                                     text="\n \t RECEIVE OUR NEWSLETTER")

    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.place(x=10, y=100)
        self.instruction_label.configure(font="Arial 8",
                                  text="Please enter your email below to receive our newsletter")
        
