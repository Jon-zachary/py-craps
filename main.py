from tabnanny import check
import Game

#TODO create input module
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

# FIX ask player to roll or quit after bet
def play_game():
  game = Game.Game()
  game.setup()
  player_input = None
  while player_input == 'r' or player_input == None:
    while not game.point:
      game.come_out() 
      player_input = get_player_input()
      if player_input == 'e':
        exit()

    while game.point: 
      game.on_point()
      player_input = get_player_input()
      if player_input == 'e':
        exit()

  player_input = get_player_input()
  if player_input == 'e':
      exit()

play_game()





