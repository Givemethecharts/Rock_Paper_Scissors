import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

our_option = input("Choose [r]ock, [p]aper or [s]cissors: ")

if our_option == "r":
    our_option = rock
elif our_option == "p":
    our_option = paper
elif our_option == "s":
    our_option = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random_number = random.randint(1, 3)

computer_move = ""
if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors

print(f"The computer chose {computer_move}")

if (our_option == rock and computer_move == scissors) or (our_option == paper and computer_move == rock) or (our_option == scissors and computer_move == paper):
    print("You win!")
elif our_option == rock and computer_move == rock or our_option == paper and computer_move == paper or our_option == scissors and computer_move == scissors:
    print("Draw")
else:
    print("You lose!")







