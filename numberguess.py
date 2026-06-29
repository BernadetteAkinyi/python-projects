import random

number = random.randrange(1, 100)
won = False
for attempt in range(1, 8):
    print(f"Attempt {attempt} of 7.")
    try:
        guess = int(input("Guess a number between 1 and 99: "))
    except ValueError:
        print("Please Enter a valid number!")
        continue
    if guess == number:
        print("Correct!")
        print(f"You have made {attempt} attempts.")
        won = True
        break
    elif guess < number:
        print("Too little, try higher")
    else:
        print("Whoa! Thats a large one")
if not won:
    print("All attempts have been used!")
    print(f"The number was {number}")
