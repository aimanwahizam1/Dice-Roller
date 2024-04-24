# ---------------------------------------------------------------------------- #
#                                  Dice Roller                                 #
# ---------------------------------------------------------------------------- #

# MVP

# ---------------------------------- Imports --------------------------------- #

import time
import random
import matplotlib.pyplot as plt

# ----------------------------------- Setup ---------------------------------- #

def setup():
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

# ------------------------------- Roll History ------------------------------- #

def create_roll_history(dice_array):
    history = {}
    
    for i in range(len(dice_array), sum(dice_array) + 1):
        history[i] = 0

    return history

# -------------------------------- Custom Dice ------------------------------- #

def custom_dice_setup():
    faces_array = []

    while True:
        try:
            number_of_die = int(input("How many dice are you rolling?\n"))
            if number_of_die <= 0:
                raise ValueError
        except ValueError:
            print("Input a valid number of dice.")
            continue
        else:
            print(f'\nRolling with {number_of_die} dice.')
            break

    for i in range(1, number_of_die + 1):
        while True:
            try:
                die_face = int(input(f'\nHow many faces are on dice {i}?\n'))
                if die_face <= 0:
                    raise ValueError
            except ValueError:
                print("Input a valid dice face value.")
                continue
            else:
                print(f'\nDice {i} is a d{die_face}.')
                faces_array.append(die_face)
                break
    
    return faces_array

# --------------------------------- Dice Roll -------------------------------- #

def roll_dice(dice_array, total_rolls):
    for dice in dice_array:
        rolls.append(random.randint(1, dice))

    total = sum(rolls)

    print(f'Roll #{total_rolls}: {str(rolls)[1:-1]}')

    return total

# ------------------------------ Graph Creation ------------------------------ #

def create_graph(rolls_array, total_rolls, dice_array):
    plt.bar(rolls_array.keys(), rolls_array.values(), color = (1,0,0,0.5))

    plt.xlabel("Dice Roll")
    plt.xticks(range(len(dice_array), sum(dice_array) + 1))
    plt.ylabel("Frequency")

    title = "Dice Roll Frequency. Total Rolls = " + str(total_rolls)
    plt.title(title)

    if max(rolls_array.values()) > 10:
        plt.yticks(range(0, max(rolls_array.values()) + 1, 2))
    else:
        plt.yticks(range(0, max(rolls_array.values()) + 1))

# -------------------------------- Roll Again -------------------------------- #

def ask_roll_again():
    while True:
        try:
            roll_again = input("\nRoll again? Y or N\n")
            if roll_again.upper() not in ["Y", "N", "YES", "NO"]:
                raise TypeError
        except TypeError:
            print("Only Y or N")
            continue
        else:
            if roll_again.upper() in ["Y", "YES"]:
                return True
            return False  

# ------------------------------------- - ------------------------------------ #

if __name__ == '__main__':
    
    # ----------------------------------- Setup ---------------------------------- #

    number_of_rolls = 1
    setup()
    dice_faces = custom_dice_setup()
    roll_history = create_roll_history(dice_faces)
    print("\nLet's get rolling!\n")
    time.sleep(0.9)

    # -------------------------------- Execution --------------------------------- #

    while True:
        print("-------------------------------------------")
        print("Rolling...")
        time.sleep(1)

        rolls = []

        # Roll dice
        roll_total = roll_dice(dice_faces, number_of_rolls)

        time.sleep(1)

        # Update roll history
        roll_history[roll_total] += 1

        # Print roll frequency graph
        create_graph(roll_history, number_of_rolls, dice_faces)
        plt.show()

        # Ask for more rolls
        if not ask_roll_again():
            break
    
        # Update roll number
        number_of_rolls+= 1

        continue

    time.sleep(0.3)
    print("\nThanks for rolling with us.")

    # Give final graph
    create_graph(roll_history, number_of_rolls, dice_faces)
    plt.title(f'Dice Rolls this game. Total Rolls = {number_of_rolls}')
    plt.show()
