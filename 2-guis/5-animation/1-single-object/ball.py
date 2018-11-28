#Bouncing ball

from tkinter import *
import time

#the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()

        #load resources
        self.ball_image = PhotoImage(file="ball.gif")

        #set window attributes
        self.title("MyAnimation")
        self.configure(height=500, width=500)

        #set animation attributes
        self.ball_x_pos = 10
        self.ball_y_pos = 200
        self.ball_x_change = 10
        self.ball_y_change = -10

        #add components
        self.add_ball_image_label()

        #start the timer
        self.tick()

    #the timer tick function
    def tick(self):
        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)

        if self.ball_y_pos <= 0:
            self.ball_y_change = -self.ball_y_change

        if self.ball_x_pos >= 460:
            self.ball_x_change = -self.ball_x_change

        if self.ball_y_pos >= 460:
            self.ball_y_change = -self.ball_y_change

        if self.ball_x_pos <= 0:
            self.ball_x_change = -self.ball_x_change

        
            
             

        
        self.after(100, self.tick)
        

    #the ball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)

# the object (using this line we dont need to have 2 files saved when build the code)
if __name__=="__main__":
    gui = AnimatedGui()
    gui.mainloop()



        

