import pygame
import sys
from button import *
from game_screens import dict_screens, ChangeScreen
from screen import GameScreen


class Win0(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.bg = pygame.image.load('1.jpg')
        self.button = Button()

    def draw(self):
        self.display.blit(self.bg, (0, 0))
        self.font = pygame.font.Font('font.ttf', 70)
        self.surf_back = self.font.render('win 0', True, 'White')
        self.display.blit(self.surf_back, (WINDOW_WIDTH // 2 - 240, 260))
        if self.button.button_back2().collidepoint(pygame.mouse.get_pos()):
            self.button.button_back_draw_hover2()
        else:
            self.button.button_back_draw2()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            self.check_buttons(event)

    def check_buttons(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pass
            if self.button.button_back2().collidepoint(event.pos):
                ChangeScreen('menu')

dict_screens['win_0'] = Win0()