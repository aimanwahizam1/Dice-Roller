# ---------------------------------------------------------------------------- #
#                                  Dice Roller                                 #
# ---------------------------------------------------------------------------- #

# MVP

# ---------------------------------- Imports --------------------------------- #

import time
import random
import matplotlib.pyplot as plt

# ----------------------------------- Setup ---------------------------------- #

print("Welcome to...")
time.sleep(1)
print("""
 .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ________    | || |     _____    | || |     ______   | || |  _________   | | | |  _______     | || |     ____     | || |   _____      | || |   _____      | || |  _________   | || |  _______     | |
| | |_   ___ `.  | || |    |_   _|   | || |   .' ___  |  | || | |_   ___  |  | | | | |_   __ \    | || |   .'    `.   | || |  |_   _|     | || |  |_   _|     | || | |_   ___  |  | || | |_   __ \    | |
| |   | |   `. \ | || |      | |     | || |  / .'   \_|  | || |   | |_  \_|  | | | |   | |__) |   | || |  /  .--.  \  | || |    | |       | || |    | |       | || |   | |_  \_|  | || |   | |__) |   | |
| |   | |    | | | || |      | |     | || |  | |         | || |   |  _|  _   | | | |   |  __ /    | || |  | |    | |  | || |    | |   _   | || |    | |   _   | || |   |  _|  _   | || |   |  __ /    | |
| |  _| |___.' / | || |     _| |_    | || |  \ `.___.'\  | || |  _| |___/ |  | | | |  _| |  \ \_  | || |  \  `--'  /  | || |   _| |__/ |  | || |   _| |__/ |  | || |  _| |___/ |  | || |  _| |  \ \_  | |
| | |________.'  | || |    |_____|   | || |   `._____.'  | || | |_________|  | | | | |____| |___| | || |   `.____.'   | || |  |________|  | || |  |________|  | || | |_________|  | || | |____| |___| | |
| |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
      """)
time.sleep(0.9)
print("In this version we will roll 2 d6")
time.sleep(0.9)
print("Let's get rolling!\n")
time.sleep(0.9)

# ----------------------------- Global Variables ----------------------------- #

number_of_rolls = 1
roll_history = {
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    10:0,
    11:0,
    12:0,
}

# ------------------------------ Graph Creation ------------------------------ #

def create_graph(array, total_rolls):
    plt.bar(array.keys(),array.values(), color = (1,0,0,0.5))

    plt.xlabel("Dice Roll")
    plt.xticks(range(2,13))
    plt.ylabel("Frequency")

    title = "Dice Roll Frequency. Total Rolls = " + str(total_rolls)
    plt.title(title)

    if max(array.values()) > 10:
        plt.yticks(range(0, max(array.values()) + 1, 2))
    else:
        plt.yticks(range(0, max(array.values()) + 1))

# ------------------------------ Dice Roll Logic ----------------------------- #

while True:
    print("-------------------------------------------")
    # Roll dice
    print("Rolling...")
    time.sleep(1)
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2 

    print(f'Roll #{number_of_rolls}: {dice1}, {dice2}\n')

    time.sleep(1)

    # Update roll history
    roll_history[total] += 1

    # Print roll frequency graph
    create_graph(roll_history, number_of_rolls)
    plt.show()

    # Ask for more rolls
    while True:
        try:
            roll_again = input("Roll again? Y or N\n")
            if roll_again.upper() not in ["Y", "N"]:
                raise TypeError
        except TypeError:
            print("Only Y or N")
            continue
        else:
            break

    if roll_again.upper() == "N":
        break
    
    # Update roll number
    number_of_rolls += 1

    continue

time.sleep(0.3)
print("\nThanks for rolling with us.")

create_graph(roll_history, number_of_rolls)
plt.title(f'Dice Rolls this game. Total Rolls = {number_of_rolls}')
plt.show()

