import pygame
import sys
from button import *
from game_screens import dict_screens, ChangeScreen
from screen import GameScreen
from what_the_game import count_game

class GameMenu(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.bg = pygame.image.load('1.jpg')
        self.button = Button()

    def draw(self):
        self.display.blit(self.bg, (0, 0))
        if self.button.button_play_snake().collidepoint(pygame.mouse.get_pos()):
            self.button.button_play_snake_hover_draw()
        else:
            self.button.button_play_snake_draw()
        if self.button.button_play_arcade().collidepoint(pygame.mouse.get_pos()):
            self.button.button_play_arcade_hover_draw()
        else:
            self.button.button_play_arcade_draw()
        if self.button.button_play_tictactoe().collidepoint(pygame.mouse.get_pos()):
            self.button.button_play_tictactoe_hover_draw()
        else:
            self.button.button_play_tictactoe_draw()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.check_buttons(event)

    def check_buttons(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pass
            if self.button.button_play_snake().collidepoint(event.pos):
                count_game(1)
                ChangeScreen('load')
            if self.button.button_play_arcade().collidepoint(event.pos):
                count_game(2)
                ChangeScreen('load')
            if self.button.button_play_tictactoe().collidepoint(event.pos):
                count_game(3)
                ChangeScreen('load')


dict_screens['game_menu'] = GameMenu()