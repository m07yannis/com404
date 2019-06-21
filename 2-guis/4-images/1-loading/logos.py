
from tkinter import *



class Gui(Tk):
  def __init__(self):
    super().__init__()

    #set window attributes
    self.title("TRANSPORT")
    self.configure(bg="#eee",height=300,width=500)

    #add components
    self.add_heading_label()

    #load images/resourse
    self.ambulance_image = PhotoImage(file="ambulance.png")
    self.bike_image = PhotoImage(file="bike.png")
    self.plane_image = PhotoImage(file="plane.png")

    #add components
    self.add_ambulance_image_label()
    self.add_bike_image_label()
    self.add_plane_image_label()

  def add_heading_label(self):
    # create the component object
    self.heading_label = Label()
    self.heading_label.grid(row=0, column=1)
    # style the component
    self.heading_label.configure(font="Arial 18", fg= "black",
                                     text="Transport")

  def add_ambulance_image_label(self):
    self.ambulance_image_label = Label()
    self.ambulance_image_label.grid(row=1, column=0)
    self.ambulance_image_label.configure(image=self.ambulance_image,
                                         height=60, width=60)

  def add_bike_image_label(self):
    self.bike_image_label = Label()
    self.bike_image_label.grid(row=1, column=1)
    self.bike_image_label.configure(image=self.bike_image, height=60, width=60)

  def add_plane_image_label(self):
    self.plane_image_label = Label()
    self.plane_image_label.grid(row=1, column=2)
    self.plane_image_label.configure(image=self.plane_image, height=60, width=60)




#create an object of the Gui class when this module is executed

if __name__=="__main__":

    gui = Gui()

    gui.mainloop()




