print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# First decision: Left or Right
choice1 = input("left or right? ").lower()
if choice1 == "right":
    print("Game Over.")
else:
    # Second decision: Swim or Wait
    choice2 = input("swim or wait? ").lower()
    if choice2 == "swim":
        print("Game Over.")
    else:
        # Third decision: Choose a door
        choice3 = input("Which door? Red, Blue, or Yellow? ").lower()
        if choice3 == "red":
            print("Game Over.")
        elif choice3 == "blue":
            print("Game Over.")
        elif choice3 == "yellow":
            print("You Win!")
        else:
            print("Game Over.")