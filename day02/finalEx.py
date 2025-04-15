# if the bill was $150.00, spilt between 5 people, with 12% tip.
# each person should pay (150.00 / 5)* 1.12
# round the result to 2 decimal places = 33.60

print("sup")

# *commented out the three input func because it was looping the questions* 
# input("what was the total bill? $")
# input("what percentage tip would u like to give? 10, 12, or 15? ")
# input("how many people are splitting the bill? ")

bill = float(input("what was the total bill? "))
tip = int(input("what percentage tip would u like to give? 10, 12, or 15? "))
people = int(input("how many people are splitting the bill? "))

tip_percent = tip/100
total_tip = bill*tip_percent
total_bill = bill+total_tip
bill_per_person = total_bill/people
final_amount = "{:.2f}".format(bill_per_person, 2) # added "{:.2f}".format to round of the decimal to 2 places

print(f"each person will pay ${final_amount} ")