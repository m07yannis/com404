from tkinter import

class Gui(tK):
  def __init__(self):
    super().__init__()

    #et window attributes
    self.title(Gui)

    #load images/resoursec
    self.ambulance_image = PhotoImage(file="ambulance.gif")
    self.bike_image = PhotoImage(file="bike.gif")
    self.plane_image = PhotoImage(file="plane")

    #add components
    self.add_ambulance_image_label()
    self.add_bike_image_label()
    self.add_plane_image_label()

  def add_ambulance_image_label(self):
    self.ambulance_image_label = Label()
    self.ambulance_image_label.grid(row=0, column=0)
    self.ambulance_image_label.configure(image=self.ambulance_image, height=60, width=60)

  def add_bike_image_label(self):
    self.bike_image_label = Label()
    self.bike_image_label.grid(row=0, column=1)
    self.bike_image_label.configure(image=self.bike_image, height=60, width=60)

  def add_plane_image_label(self):
    self.plane_image_label = Label()
    self.plane_image_label.grid(row=0, column=2)
    self.plane_image_label.configure(image=self.plane_image, height=60, width=60)


#create an object of the gui class when this module is executed
if (__name__ == ""__main__"):
    gui = Gui()
    gui.mainloop()




