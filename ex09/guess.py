import random

print('''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!''')
number = random.randint(1, 99)
attempts = 0
while True:
    user = input('''What's your guess between 1 and 99?\n''')
    if user == "exit":
        print("Goodbye!")
        break
    try:
        usernumber = int(user)
        attempts = attempts + 1
        if usernumber < number:
            print("Too low!")
        elif usernumber > number:
            print("Too high!")
        else:
            if number == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42")
            if attempts == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!")
                print("You won in", attempts, "attempts!")
            break
    except:
        print("only integers")