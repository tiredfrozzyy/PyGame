import pygame
from settings import *
from game_screens import get_current_screen, ChangeScreen, add_screen


pygame.init()
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
import menu
import loading
import snake
import game_over
import game_menu
import arcade
import TicTacToe
import settings_window
import win
import winner_x
import winner_0
import drawn


class Main:
    def __init__(self):
        self.display = pygame.display.get_surface()
        pygame.display.set_caption('Space game')
        ChangeScreen('menu')

    def run(self):
        while True:
            get_current_screen().run()
            pygame.display.flip()


if __name__ == '__main__':
    main = Main()
    main.run()
