import random

user = int(input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors. \n"))
computer = random.randint(0, 2)


print(f"computer choose {computer}")

if user >= 3 or user < 0:  
    print("worng number you loose")
elif user == 1 and computer == 0:
    print("user wins")
elif user == 2 and computer == 1:
    print("user wins")
elif user == 0 and computer == 2:
    print("user wins")
elif computer == user:
    print("draw")
else:
    print("user loose")


