#Writing a class(into main.py)

class Bot:
  def __init__(self, name, age, energy, shield):
    self.name = name
    self.age = age
    self.energy = energy
    self.shield = shield
    

  def display_name(self):
   print(self.name)

  def display_age(self):
   print(self.age)

  def display_energy(self):
    print(self.energy)
    
  def dislay_shield(self):
    print(self.shield)

  def display_summary(self):
   print("{} is {} years old, has energy {} level and shield {} power". format(self.name, self.age, self.energy, self.shield))
 
 #Creating an object(into bot.py)
 
 
from bot import Bot

yannis_bot = Bot("Yannis", 30, 100, 100)
yannis_bot.display_summary()
