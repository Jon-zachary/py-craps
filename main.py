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
    self.working_bets = []

  def add_roll(self, roll):
    self.rolls.push(roll)
  def add_working_bet(self, bet):
    self.working_bets.push(bet)

  def setup(self):
    try:
      """Sets the init player state and adds it to a game"""
      name, bankroll = input('enter name and starting bankroll: ').split(' ')
      bankroll = int(bankroll)
      self.player = Player(name, bankroll)
      if (type(name) != str) or (type(bankroll) != int):
        raise ValueError
      print(f"Welcome to command line craps {self.player.name}")
    except ValueError:
      print("Oops! Please enter your name followed by your bankroll e.g 'jon 10000'")
      self.setup()

  def place_bet(self):
    bet_amount = input("Enter your bet amount: ")
    if check_bet(self, int(bet_amount)):
      self.working_bets.insert(0, bet_amount)
      return
    self.place_bet()

  def on_win(self):
    bet_amount = int(self.working_bets[0])
    self.player.bankroll += bet_amount
    print(f"you added {bet_amount} to your bankroll for a total of {self.player.bankroll}")
# END OF CLASS




def come_out(game):
  game.place_bet()
  roll = game.dice.roll()
  if sum(roll) in [7, 11]:
    print(f"winner {sum(roll)}")
    game.on_win()
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
    game.on_win()
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

def on_loss(game):
  bet_amount = int(game.working_bets[0])
  game.player.bankroll -= bet_amount
  print(f"you lost {bet_amount} your bankroll is now {game.player.bankroll}")

#TODO make sure input is an int and does not exceed bankroll
def check_bet(game, bet):
  if bet > game.player.bankroll:
    print(f"That bet is more than you have, your maximum bet is {game.player.bankroll}")
    return False
  return True




# FIX ask player to roll or quit after bet
def play_game():
  game = Game()
  game.setup()
  player_input = None
  while player_input == 'r' or player_input == None:
    while not game.point:
      come_out(game) 
      player_input = get_player_input()
      if player_input == 'e':
        exit()

    while game.point: 
      on_point(game)
      player_input = get_player_input()
      if player_input == 'e':
        exit()

  player_input = get_player_input()
  if player_input == 'e':
      exit()

play_game()





