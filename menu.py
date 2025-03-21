import pygame
import sys
from button import *
from game_screens import dict_screens, ChangeScreen
from screen import GameScreen
from restart import *


class Select(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.bg = pygame.image.load('space_end.jpg')
        self.button = Button()
        self.restart = Restart()

    def draw(self):
        self.display.blit(self.bg, (0, 0))
        if self.button.button_play().collidepoint(pygame.mouse.get_pos()):
            self.button.button_play_draw_hover()
        else:
            self.button.button_play_draw()
        if self.button.button_rules().collidepoint(pygame.mouse.get_pos()):
            self.button.button_rules_draw_hover()
        else:
            self.button.button_rules_draw()
        if self.button.button_rules().collidepoint(pygame.mouse.get_pos()):
            self.button.button_rules_draw_hover()
        else:
            self.button.button_rules_draw()
        if self.button.button_settings().collidepoint(pygame.mouse.get_pos()):
            self.button.button_settings_draw_hover()
        else:
            self.button.button_settings_draw()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.check_buttons(event)
        self.restart.restart_game()

    def check_buttons(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pass
            if self.button.button_play().collidepoint(event.pos):
                ChangeScreen('game_menu')
            if self.button.button_settings().collidepoint(event.pos):
                ChangeScreen('settings_window')
            if self.button.button_rules().collidepoint(event.pos):
                pass


dict_screens['menu'] = Select()