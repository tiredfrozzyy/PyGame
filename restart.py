from arcade import *
from TicTacToe import *
from snake import *


class Restart:
    def __init__(self):
        self.tictactoe = TicTacToe()
        self.arcade = Arcade()
        self.snake = Snake()

    def restart_game(self):
        self.tictactoe.new_game()
        self.arcade.new_game_arcade()
        self.snake.new_game_snake()



