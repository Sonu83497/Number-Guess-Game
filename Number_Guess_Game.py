import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts_allowed = 10
    attempts = 0
    score = 100

    while attempts < attempts_allowed:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{attempts_allowed} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print(" Too low!")
            score -= 10
        elif guess > secret_number:
            print("Too high!")
            score -= 10
        else:
            print(f"\n Correct! You guessed the number in {attempts} tries.")
            print(f" Your score: {score}")
            break
    else:
        print("\n You've used all your attempts.")
        print(f"The correct number was: {secret_number}")
        print(" Better luck next time!")

if __name__ == "__main__":
    number_guessing_game()
