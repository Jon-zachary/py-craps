import pickle

class Input():
  def __init__(self):
    self.unicode_to_dice = {'1': '\U00012680'}

  def save_game(self, player):
    with open('savefile', 'wb') as f:
      pickle.dump(player, f)
      print('Game saved')

  def load_game(self):
    with open('savefile', 'wb') as f:
      player = pickle.load(f)
    return player

  def roll_or_quit(self):
    player_input = input('press r to roll or e to exit: ')
    self.check_input(player_input)
    return player_input

  def check_input(self, player_input):
    return player_input in ['r', 'e']

  def get_player_input(self):
    player_input = self.roll_or_quit()
    while not self.check_input(player_input):
      player_input = self.roll_or_quit()
    return player_input

  def print_dice(self):
    pass
