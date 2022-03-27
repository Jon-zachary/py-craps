import random as rnd
from tabnanny import check
import json

class Dice:
  """Creates a pair of six sided dice with a roll method"""
  face1 = None
  face2 = None

  def roll(self):
    self.face1 = rnd.randrange(1,7)
    self.face2 = rnd.randrange(1,7)
    return [self.face1, self.face2]

class Player():
  """Creates a player object with a name and bankroll"""
  def __init__(self, name, bankroll):
    self.name = name
    self.bankroll = int(bankroll)

class Game():
  """Creates a game with game state and player and dice instances"""
  def __init__(self):
    self.player = None
    self.is_come_out = True
    self.point = None
    self.dice = Dice()
    self.rolls = []
    self.working_bets = [10]

  def add_roll(self, roll):
    self.rolls.push(roll)
  def add_working_bet(self, bet):
    self.working_bets.push(bet)




# TODO make sure user input is two values, space seperated, one string one int
def setup(game):
  """Sets the init player state and adds it to a game"""
 # name, bankroll = input('enter name and starting bankroll: ').split(' ')
  game.player = Player('jon', 100)
  print(f"Welcome to command line craps {game.player.name}")

def come_out(game):
  roll = game.dice.roll()
  if sum(roll) in [7, 11]:
    print(f"winner {sum(roll)}")
    on_win(game)
  elif sum(roll) in [2, 3, 12]:
    print(f"{sum(roll)} craps")
    on_loss(game)
  else:
    game.point = sum(roll)
    print(f"the point is {game.point}")
    game.is_come_out = False

def on_point(game):
  roll = game.dice.roll()
  if sum(roll) == game.point:
    print(f"Winner! you hit your point {game.point}")
    on_win(game)
    game.point = None
  elif sum(roll) == 7:
    print("Seven out, pay the don't")
    on_loss(game)
    game.point = None
  else: 
    print(f"the point is {game.point}, you rolled a {sum(roll)}")

def check_input(player_input):
  return player_input in ['r', 'e']

def roll_or_quit():
  player_input = input('press r to roll or e to exit: ')
  check_input(player_input)
  return player_input

def get_player_input():
  player_input = roll_or_quit()
  while not check_input(player_input):
    player_input = roll_or_quit()
  return player_input

def on_win(game):
  bet_amount = game.working_bets[0]
  game.player.bankroll += bet_amount
  print(f"you added {bet_amount} to your bankroll for a total of {game.player.bankroll}")

def on_loss(game):
  bet_amount = game.working_bets[0]
  game.player.bankroll -= bet_amount
  print(f"you lost {bet_amount} your bankroll is now {game.player.bankroll}")

def play_game():
  game = Game()
  setup(game)
  player_input = 'r'
  while player_input == 'r':
    if player_input == 'r':
      while not game.point:
        come_out(game) 
        player_input = get_player_input()
        if player_input == 'e':
          exit()
      while game.point != None: 
        on_point(game)
        player_input = get_player_input()
        if player_input == 'e':
          exit()
          
play_game()





