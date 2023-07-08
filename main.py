import random

def play_game():
    balance = 100  # Initial balance for the player

    print("Welcome to the Number Guessing Game!")
    print("You have 100 coins . Each guess costs $10. Win the game to double your money!\n")

    while balance >= 10:
        secret_number = random.randint(1, 100)
        attempts = 0

        while True:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                winnings = 10 * attempts  # Calculate the winnings based on the number of attempts
                balance += winnings
                print(f"You've won ${winnings}! Your new balance is ${balance}.\n")
                break

        balance -= 10  # Deduct 10 coins from the balance for each guess

    print("Game Over!")
    print(f"Final balance: ${balance}")

play_game()
