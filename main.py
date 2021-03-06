from tabnanny import check
import Game
import Input as inout
import sys

def play_game():
  try:
    io = inout.Input()
    game = Game.Game()
    game.setup()
    player_input = None
    while player_input == 'r' or player_input == None:
      while not game.point:
        loading = input("press 's' to save your game")
        if loading == 's':
          io.save_game(game.player)
          

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
  except(KeyboardInterrupt):
    print('\n Game Over')
    sys.exit(0)


play_game()





