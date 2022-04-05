from tabnanny import check
import Game

#TODO create input module

class Input():
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

# FIX ask player to roll or quit after bet
def play_game():
  io = Input()
  game = Game.Game()
  game.setup()
  player_input = None
  while player_input == 'r' or player_input == None:
    while not game.point:
      game.come_out() 
      player_input = io.get_player_input()
      if player_input == 'e':
        exit()

    while game.point: 
      game.on_point()
      player_input = io.get_player_input()
      if player_input == 'e':
        exit()

  player_input = io.get_player_input()
  if player_input == 'e':
      exit()

play_game()





