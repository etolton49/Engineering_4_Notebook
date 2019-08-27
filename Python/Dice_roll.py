from random import randint
import sys

while True:
    key = input("Press Enter for number or X to quit")
    if key == "":
        dice_roll = randint(1,6)
        print("Your roll is %d" % (dice_roll))
    if key == "x":
        sys.exit()


