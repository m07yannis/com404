# this is the main file saved
from gui import Gui

gui = Gui()
gui.mainloop()



# this file will be saved in gui file, ACTIVIRY 2

from tkinter import *



class Gui(Tk):

    def __init__(self):
        super().__init__()


        #set windows attributes

        self.title("Box&Events")
        self.configure(bg="#eee", height=300, width=400)

        #add components for each row

        self.add_heading_label()
        self.add_instruction_label()
        self.add_lyric_entry()
        self.add_submit_button()
        self.add_subtitle_label()
        self.add_lyrics_entry()



    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.place(x=120, y=20)
        self.heading_label.configure(font="Arial 22",
                                     text="Song Maker")

        
    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.place(x=10, y=80)
        self.instruction_label.configure(font="Arial 16",
                                             text="Lyric to add:")
        
    def add_lyric_entry(self):
        self.lyric_entry = Entry()
        self.lyric_entry.place(x=10, y=120)
        self.lyric_entry.configure(font="Arial 20",
                                   text=())

    def add_submit_button(self):
        self.submit_button = Button()
        self.submit_button.place(x=325, y=120)
        self.submit_button.configure(font="Arial 14",
                                     text="Add")

    def add_subtitle_label(self):
        self.subtitle_label = Label()
        self.subtitle_label.place(x=10, y=200)
        self.subtitle_label.configure(font="Arial 16",
                                      text="Lyrics:")

    def add_lyrics_entry(self):
        self.lyrics_entry = Entry()
        self.lyrics_entry.place(x=10, y=240)
        self.lyrics_entry.configure(font="Arial 25")
        pass


        
        

        

    



    
