from tkinter import *
from tkinter import messagebox

class Hotel(Tk):
    def __init__(self):
        super().__init__()

        #set windows attributes
        self.title("HotelCheckIn")
        self.configure(bg="#eee", height=300, width="400")

        #add components
        self.add_heading_label()
        self.add_instruction_label()
        self.add_instruction_label2()
        self.add_instruction_label3()
        self.add_name_entry()
        self.add_passport_entry()
        self.add_nights_entry()
        self.add_check_button1()
        self.add_check_button2()
        self.add_check_button3()
        self.add_submit_button()

        #defining objects
    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.place(x=100, y=0)
        self.heading_label.configure(font="Arial 20", fg= "red",
                                     text="Hotel Check In")

    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.place(x=0, y=50)
        self.instruction_label.configure(font="Arial 16", fg="black", bg="#eee",
                                         text="Name:")

    def add_instruction_label2(self):
        self.instruction_label2 = Label()
        self.instruction_label2.place(x=0, y=100)
        self.instruction_label2.configure(font="Arial 16", fg="black", bg="#eee",
                                         text="Passport Number:")

    def add_instruction_label3(self):
        self.instruction_label3 = Label()
        self.instruction_label3.place(x=0, y=150)
        self.instruction_label3.configure(font="Arial 16", fg="black", bg="#eee",
                                          text="Nr of nights:")



    def add_name_entry(self):
        self.name_entry = Entry()
        self.name_entry.place(x=200, y=50)
        self.name_entry.configure(font="Arial 18", bg="pink", width="10"
                                  , text=())

    def add_passport_entry(self):
        self.passport_entry = Entry()
        self.passport_entry.place(x=200, y=100)
        self.passport_entry.configure(font="Arial 18", bg="pink", width="10"
                                  , text=())
        


    def add_nights_entry(self):
        self.nights_entry = Entry()
        self.nights_entry.place(x=200, y=150)
        self.nights_entry.configure(font="Arial 18", bg="pink", width="10"
                                  , text=())

    def add_check_button1(self):
        self.check_button1 = Checkbutton()
        self.check_button1.place(x=350, y=50)
        self.check_button1.configure(font="Arial 18", onvalue = 1,
                                     offvalue = 0)

    def add_check_button2(self):
        self.check_button2 = Checkbutton()
        self.check_button2.place(x=350, y=100)
        self.check_button2.configure(font="Arial 18", onvalue = 1,
                                     offvalue = 0)

    def add_check_button3(self):
        self.check_button3 = Checkbutton()
        self.check_button3.place(x=350, y=150)
        self.check_button3.configure(font="Arial 18", onvalue = 1,
                                     offvalue = 0)

    def add_submit_button(self):
        self.submit_button = Button()
        self.submit_button.place(x=150, y=240)
        self.submit_button.configure(font="Arial 16", fg="red", bg="yellow",
                                     text="Check In")

        self.submit_button.bind("<ButtonRelease-1>", self.submit_button_clicked)

    def submit_button_clicked(self, event):
        messagebox.showinfo("Hotel", "Guest Checked In")
                                     





if __name__=="__main__":

    hotel = Hotel()

    hotel.mainloop()
