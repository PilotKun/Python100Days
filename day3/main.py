# if and else satements - day 3

print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

bill = 0

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        bill = 12
    
    wants_photos = input("u want photos? Y or N. ")
    if wants_photos == "Y":
        bill += 3
    
    print(f"final bill is {bill}")
else:
    print("sorry u can't ride the rollercoaster..")

# Logical operators 
# and, or, not
# A and B
# A or B
# not A

