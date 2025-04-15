print("welcome")
size = input("what size pizza u want? S, M, L? ")
add_pepperoni = input("u want pepperoni? Y or N? ")
extra_cheese = input("u want extra cheese? Y or N? ")

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":  # changed `elif` to `if`
        bill += 1
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":  # changed `elif` to `if`
        bill += 1 
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":  # changed `elif` to `if`
        bill += 1

print(f"final bill is {bill}")
