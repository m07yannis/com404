#Read current amount from user
print("Please enter savings amount (£)")
amount = float(input())

#Read interest rate from user
print("Please enter your interest rate (%)")
interest_rate = float(input())

#Calculate new amount
interest_amount = (interest_rate / 100) * amount
new_amount = amount + interest_amount

#Dispaly the results
print("The new amount is £", str(new_amount))
