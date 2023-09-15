import random
# Creating the required variables for our game
random_number = random.randint(1, 10)
guess = ""
number_of_guesses = 0
guess_limit = 5
out_of_guesses = False
# The program will continue for as long as the guess and random_number are not equal and the guess limit is reached
while guess != str(random_number) and not(out_of_guesses):
    if number_of_guesses < guess_limit:
        guess = input("Enter random number : ")
        number_of_guesses += 1
        if int(guess) > random_number:
            print("Guess is too High!")
        if int(guess) < random_number:
            print("Guess is too low!")
# When guess limit is reached the program s terminated
    else:
        print("out_of_guesses!!")
        break

# You win if you guess the number with the number of tries and lose if you fail to guess the number correctly
if int(guess) == random_number:
    print("You win!!")
else:
    print("You Lose!!")



