from art import logo
from art import vs
from gameData import data
import random
import os

# todo: display art
# todo: generate a random account from the game data
# todo: format the account data into printable format
# todo: ask user for a guess
# todo: check if user is correct
# todo: get follower count of each account
# todo: use if statement to check if user is correct
# todo: give user ffedback on their guess
# todo: score keeping 
# todo: make the game repeatable
# todo: making account at position B become the next account at position a 
# todo: clear the screen between rounds

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_account():
    return random.choice(data)

def format_account_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(guess , a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def playGame():
    score = 0
    game_should_continue = True
    
    #! get accounts
    account_a = get_random_account()
    account_b = get_random_account()
    # Ensure accounts are different at the start
    while account_a == account_b:
        account_b = get_random_account()

    while game_should_continue:
        #!display logo
        clear_screen()
        print(logo)

        #!display current score
        if score > 0:
            print(f"You're right! Current score: {score}")
        
        #!display the accounts to compare
        print(f"Compare A: {format_account_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_account_data(account_b)}")

        #!ask for user guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        #!get follower counts
        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']
        
        #!check if the user is correct
        is_correct = check_answer(guess, a_followers, b_followers)
        #! give feedback
        if is_correct:
            score += 1
            #! make account B the new account A
            account_a = account_b
            #! get a new account B
            account_b = get_random_account()
            #!make sure account B is different from account A
            while account_b == account_a:
                account_b = get_random_account()
        else:
            game_should_continue = False
            clear_screen()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")

#*start game
playGame()