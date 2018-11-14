# this is the main file saved


from gui import Gui

gui = Gui()
gui.mainloop()


# this file will be saved in gui

from tkinter import*                  
from tkinter import messagebox
class Gui(Tk):

    def __init__(self):
        super().__init__()

        #set windows attributes
        self.title("Events")                               #title
        self.configure(bg="#eee", height=300, width=400) #backgroung
        

        #add components foe each row
        self.add_heading_label()
        self.add_instruction_label()
        self.add_tickets_entry()
        self.add_submit_button()

    def add_heading_label(self): # this is the heading row
        # create the component object
        self.heading_label = Label()
        self.heading_label.place(x=80, y=20)
        # style the component
        self.heading_label.configure(font="Arial 24",
                                     text="Entrance Ticket")
    def add_instruction_label(self):    #this is the instrunction row,second
        self.instruction_label = Label()
        self.instruction_label.place(x=10, y=80)
        self.instruction_label.configure(font="Arial 18", 
                                         text="How many tickets are needed?")
    def add_tickets_entry(self):        #this isthe entry box for data input
        self.tickets_entry = Entry()
        self.tickets_entry.place(x=10, y=150)
        self.tickets_entry.configure(font="Arial 24",
                                     text=())

    def add_submit_button(self):        #this is the button "Submit"
        self.submit_button = Button()
        self.submit_button.place(x=150, y=220)
        self.submit_button.configure(font="Arial 16",
                                     text="Submit")
        #bind events
        self.submit_button.bind("<ButtonRelease-1>", self.submit_button_clicked)

        #letf click response after clicking the button
        
    def submit_button_clicked(self, event):  
        num_tickets = self.tickets_entry.get()
        messagebox.showinfo("Gui", "You have purchased"
                            + num_tickets + "tickets!")
        
        




        


