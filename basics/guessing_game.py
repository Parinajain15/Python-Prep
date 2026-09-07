import random

def guessing_game():
    lucky_num = random.randint(1, 10)

    attempts = 1
    user_num = int(input("Guess the lucky number between 1-10: "))

    while user_num != lucky_num:

        if user_num > lucky_num:
            print("Too High")
        else:
            print("Too Low")

        user_num = int(input("Guess again: "))
        attempts += 1

    print("Correct!")
    print("Attempts:", attempts)


guessing_game()