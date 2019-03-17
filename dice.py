from Tkinter import *
from ttk import *
import random
from intertools import groupby
dice = 0

def roll(roll_number):
  numbers = range(1,7)
  dice = range(roll_number)
  iterations = 0
  while iterations < roll_number:
    iterations = iterations + 1
    dice[iterations-1] = random.choice(numbers)
  return dice

def hand(slice):
  dice_hand = [len(list(group)) for key, group in groupby(dice)]
  dice_hand.sort(reverse=True)
  straight_1 = [1,2,3,4,5]
  straight_2 = [2,3,4,5,6]
  if dice == straight_1 or dice == straight_2:
    return "It's a straight!"
    elif dice_hand[0] == 5:
      return "Five of a kind!"
    elif dice_hand[0] == 4:
      return "Four of a kind!"
    elif dice_hand[0] == 3:
      if dice_hand[1] == 2:
        return "Two pair"
      else:
        return "One pair"
    else:
      return "High card"
    
def gui():
  global dice
  dice = roll(5)
  dice.sort()
  nine = 1
  ten = 2
  jack = 3
  queen = 4
  king = 5
  ace = 6
  names = {
    nine: "9",
    ten: "10",
    jack: "J",
    queen: "Q",
    king: "K",
    ace: "A"
  }
  result = "You have " + hand(dice)

def game():
  throws()

def throws()
  global dice
  dice1_check = dice1.get()
  dice2_check = dice2.get()
  dice3_check = dice3.get()
  dice4_check = dice4.get()
  dice5_check = dice5.get()
  dice_rerolls = [dice1_check, dice2_check, dice3_check, dice4_check, dice5_check]
  for i in range(len(dice_rerolls)):
      if 0 in dice_rerolls:
        dice_rerolls.remove(0)
      if len(dice_rerolls) == 0:
        result = "You finish with " + hand(dice)
        hand_output.set(result)
      else:
        roll_number = len(dice_rerolls)
        number_rerolls = roll(roll_number)
        dice_changes = range(len(dice_rerolls))
        iterations = 0
        while iterations < roll_number:
          iterations = iterations + 1
          replacement = number_rerolls[iterations-1]
          dice[dice_changes[iterations-1]] = replacement
          dice.sort()
          new_dice_list = [0,0,0,0,0]
          for i in range(len(dice)):
            new_dice_list[i] = names[dice[i]]
            final_dice = " ".join(new_dice_list)
            dice_output.set(final_dice)
            final_result = "You finish with " + hand(dice)
            hand_output.set(final_result)

def reset_game():
  global dice
  dice = roll(5)
  dice.sort()
  for i in range(len(dice)):
    empty_dice[i] = names[dice[i]]
  first_dice = " ".join(empty_dice)
  dice_output.set(first_dice)
  result = "You have " + hand(dice)
  hand_output.set(result)

if __name__ == '__main__':
  gui()































      














    