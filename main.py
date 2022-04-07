from tabnanny import check
import Game
import Input as IO

def play_game():
  io = IO.Input()
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





