print("Please enter the second number")
number_2 = float(input())

print("Please enter the third number")
number_3 = float(input())

#declare some counters
evens = 0
odds = 0

if(number_1 % 2 == 0):
  evens = evens + 1
else:
    odds = odds +1

if(number_2 % 2 == 0):
  evens = evens + 1
else:
    odds = odds +1

if(number_3 % 2 == 0):
  evens = evens + 1
else:
    odds = odds +1

print("Total numbers of evens is", evens)
print("Total numbers of odds is", odds)
