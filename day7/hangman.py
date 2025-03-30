import random
import os  # Import os module for clearing the screen

from hangmanArt import hangmanArt, logo
print(logo)
from hangmanWordlist import hangmanWordlist

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')  # 'cls' for Windows, 'clear' for Unix/Linux

def main():
    print("Welcome to Hangman")
    secret_word = random.choice(hangmanWordlist).lower()
    guessed_letters = []
    attempts_left = 6

    while True:
        # display game state
        print(hangmanArt[attempts_left])

        # show word with blanks
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {' '.join(guessed_letters)}")

        # check win/lose conditions
        if all(letter in guessed_letters for letter in secret_word):
            print("\nYou win! The word was:", secret_word)
            break

        if attempts_left == 0:
            print("\nGame over! The word was:", secret_word)
            break

        # get player guess
        while True:
            guess = input("\nGuess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already guessed that letter!")
                else:
                    break
            else:
                print("Please enter a single letter (a-z).")
        guessed_letters.append(guess)

        # check if guess is wrong
        if guess not in secret_word:
            attempts_left -= 1
            print("Wrong guess!")

        # Clear the screen after processing the guess
        clear_screen()
        print(logo)  # Reprint the logo after clearing the screen

if __name__ == "__main__":
    main()