import random as rnd
from tabnanny import check

class Dice:
  face1 = None
  face2 = None

  def roll(self):
    self.face1 = rnd.randrange(1,7)
    self.face2 = rnd.randrange(1,7)
    return [self.face1, self.face2]

class Player():
  def __init__(self, name, sbr):
    self.name = name
    self.sbr = int(sbr)

def check_roll(roll):
  if sum(roll) == 7:
    print('seven seven')
    return True

def til_seven(dice):
  while True:
    roll = dice.roll()
    print(roll[0],roll[1])
    if check_roll(roll):
      break


dice = Dice()
# TODO make sure user input is two values, space seperated, one string one int
name, sbr = input('enter name and starting bank roll: ').split(' ')
player = Player(name, sbr)


def check_input(player_input):
  return player_input in ['r', 'e']

def welcome():
  player_input = input(f'welcome to command line craps {player.name}, press r to roll or e to exit: ')
  check_input(player_input)
  return player_input


def play_game():
  player_input = welcome()
  
  while not check_input(player_input):
    player_input = welcome()

  if player_input == 'r':
    til_seven(dice)
  elif player_input == 'e':
    exit()

play_game()





