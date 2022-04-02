import Dice
import Player

class Game():
  """Creates a game with game state and player and dice instances"""

  def __init__(self):
    self.player = None
    self.is_come_out = True
    self.point = None
    self.dice = Dice.Dice()
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
      self.player = Player.Player(name, bankroll)
      if (type(name) != str) or (type(bankroll) != int):
        raise ValueError
      print(f"Welcome to command line craps {self.player.name}")
    except ValueError:
      print("Oops! Please enter your name followed by your bankroll e.g 'jon 10000'")
      self.setup()

  def place_bet(self):
    bet_amount = input("Enter your bet amount: ")
    if self.check_bet(int(bet_amount)):
      self.working_bets.insert(0, bet_amount)
      return
    self.place_bet()

  def check_bet(self, bet):
      if bet > self.player.bankroll:
        print(
            f"That bet is more than you have, your maximum bet is {self.player.bankroll}")
        return False
      return True
      
  def on_win(self):
    bet_amount = int(self.working_bets[0])
    self.player.bankroll += bet_amount
    print(
        f"you added {bet_amount} to your bankroll for a total of {self.player.bankroll}")

  def on_loss(self):
    bet_amount = int(self.working_bets[0])
    self.player.bankroll -= bet_amount
    print(f"you lost {bet_amount} your bankroll is now {self.player.bankroll}")

  def on_point(self):
    roll = self.dice.roll()
    if sum(roll) == self.point:
      print(f"Winner! you hit your point {self.point}")
      self.on_win()
      self.point = None
    elif sum(roll) == 7:
      print("Seven out, pay the don't")
      self.on_loss()
      self.point = None
    else:
      print(f"the point is {self.point}, you rolled a {sum(roll)}")

  def come_out(self):
    self.place_bet()
    roll = self.dice.roll()
    if sum(roll) in [7, 11]:
      print(f"winner {sum(roll)}")
      self.on_win()
    elif sum(roll) in [2, 3, 12]:
      print(f"{sum(roll)} craps")
      self.on_loss()
    else:
      self.point = sum(roll)
      print(f"the point is {self.point}")
      self.is_come_out = False

    
# END OF CLASS
