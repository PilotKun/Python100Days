from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def choose_difficulty():
    level = input("Choose a difficulty. Type 'e' for easy or 'h' for hard: ").lower()
    if level == "e":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return turns

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = choose_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")
    while turns > 0:
        try:
            guess = int(input("Make a guess: "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            turns = check_answer(guess, answer, turns)
            if guess == answer:
                break
            if turns > 0:
                print(f"You have {turns} attempts remaining.")
            else:
                print(f"You've run out of attempts. The answer was {answer}.")
        except ValueError:
            print("Please enter a valid number.")
    play_again = input("Would you like to play again? Type 'y' or 'n': ").lower()
    if play_again == 'y':
        game()
    else:
        print("Thanks for playing!")

game()