MAX_ROBOTS = 10
print("How many  faces should i draw?")
num_robots = int(input())

#Dislay robots
robots_displayed = 0

if (num_robots < MAX_ROBOTS):
 for robots_displayed in range(0,num_robots, 1):
   print(":-)")
else:
  for robots_displayed in range (0, MAX_ROBOTS, 1):
    print(":-)")
