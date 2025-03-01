import pygame
from settings import *


class Button:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.font = pygame.font.Font('font.ttf', 30)
        self.font2 = pygame.font.Font('font.ttf', 40)

    def button_play(self):
        button_play = pygame.Rect(WINDOW_WIDTH / 2 - 140, WINDOW_HEIGHT / 2 - 100, 250, 60)
        return button_play

    def button_play_draw(self):
        self.surf_play = self.font2.render('Играть', True, 'Black')
        pygame.draw.rect(self.display, (0, 106, 138), self.button_play())
        self.display.blit(self.surf_play, (self.button_play().x + 10, self.button_play().y + 10))

    def button_play_draw_hover(self):
        self.surf_play = self.font2.render('Играть', True, 'Black')
        pygame.draw.rect(self.display, (0, 149, 195), self.button_play())
        self.display.blit(self.surf_play, (self.button_play().x + 10, self.button_play().y + 10))

    def button_settings(self):
        button_settings = pygame.Rect(WINDOW_WIDTH / 2 - 165, WINDOW_HEIGHT / 2, 300, 50)
        return button_settings

    def button_settings_draw(self):
        self.surf_settings = self.font.render('Настройки', True, 'Black')
        pygame.draw.rect(self.display, (0, 106, 138), self.button_settings())
        self.display.blit(self.surf_settings, (self.button_settings().x + 10, self.button_settings().y + 10))

    def button_settings_draw_hover(self):
        self.surf_settings = self.font.render('Настройки', True, 'Black')
        pygame.draw.rect(self.display, (0, 149, 195), self.button_settings())
        self.display.blit(self.surf_settings, (self.button_settings().x + 10, self.button_settings().y + 10))

    def button_rules(self):
        button_rules = pygame.Rect(WINDOW_WIDTH / 2 - 140, WINDOW_HEIGHT / 2 + 80, 225, 50)
        return button_rules

    def button_rules_draw(self):
        self.surf_quit = self.font.render('Правила', True, 'Black')
        pygame.draw.rect(self.display, (0, 106, 138), self.button_rules())
        self.display.blit(self.surf_quit, (self.button_rules().x + 10, self.button_rules().y + 10))

    def button_rules_draw_hover(self):
        self.surf_quit = self.font.render('Правила', True, 'Black')
        pygame.draw.rect(self.display, (0, 149, 195), self.button_rules())
        self.display.blit(self.surf_quit, (self.button_rules().x + 10, self.button_rules().y + 10))

    def button_check_mark(self):
        check_mark_button = pygame.Rect(WINDOW_WIDTH / 2 + 25, WINDOW_HEIGHT / 2 - 35, 40, 40)
        return check_mark_button

    def button_check_mark_draw(self):
        self.surf_check = self.font.render('Music', True, 'Black')
        pygame.draw.rect(self.display, (0, 106, 138), self.button_check_mark())
        self.display.blit(self.surf_check, (WINDOW_WIDTH / 2 - 200, WINDOW_HEIGHT / 2 - 25))

    def button_back(self):
        button_back = pygame.Rect(WINDOW_WIDTH / 2 - 110, WINDOW_HEIGHT / 2 + 100, 175, 50)
        return button_back

    def button_back_draw(self):
        self.surf_back = self.font.render('Назад', True, 'Black')
        pygame.draw.rect(self.display, (0, 89, 117), self.button_back())
        self.display.blit(self.surf_back, (self.button_back().x + 10, self.button_back().y + 10))

    def button_back_draw_hover(self):
        self.surf_back = self.font.render('Назад', True, 'Black')
        pygame.draw.rect(self.display, (0, 149, 195), self.button_back())
        self.display.blit(self.surf_back, (self.button_back().x + 10, self.button_back().y + 10))

    def button_back2(self):
        button_back = pygame.Rect(0, WINDOW_HEIGHT - 50, 175, 50)
        return button_back

    def button_back_draw2(self):
        self.surf_back = self.font.render('Назад', True, 'Black')
        pygame.draw.rect(self.display, (0, 89, 117), self.button_back2())
        self.display.blit(self.surf_back, (self.button_back2().x + 10, self.button_back2().y + 10))

    def button_back_draw_hover2(self):
        self.surf_back = self.font.render('Назад', True, 'Black')
        pygame.draw.rect(self.display, (0, 149, 195), self.button_back2())
        self.display.blit(self.surf_back, (self.button_back2().x + 10, self.button_back2().y + 10))

    def button_menu(self):
        menu_button = pygame.Rect(WINDOW_WIDTH // 2 - 75, WINDOW_HEIGHT // 2 - 50, 150, 50)
        return menu_button

    def button_menu_draw(self):
        self.surf_menu = self.font.render('Меню', True, 'Black')
        pygame.draw.rect(self.display, (0, 89, 117), self.button_menu())
        self.display.blit(self.surf_menu, (self.button_menu().x + 15, self.button_menu().y + 10))

    def button_menu_draw_hover(self):
        self.surf_menu = self.font.render('Меню', True, 'Black')
        pygame.draw.rect(self.display, (0, 149, 195), self.button_menu())
        self.display.blit(self.surf_menu, (self.button_menu().x + 15, self.button_menu().y + 10))

    def button_restart(self):
        button_restart = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 50, 230, 50)
        return button_restart

    def button_restart_draw(self):
        self.surf_restart = self.font.render('Заново', True, 'Black')
        pygame.draw.rect(self.display, (0, 89, 117), self.button_restart())
        self.display.blit(self.surf_restart, (self.button_restart().x + 15, self.button_restart().y + 10))

    def button_restart_draw_hover(self):
        self.surf_restart = self.font.render('Заново', True, 'Black')
        pygame.draw.rect(self.display, (0, 149, 195), self.button_restart())
        self.display.blit(self.surf_restart, (self.button_restart().x + 15, self.button_restart().y + 10))

    def button_play_snake(self):
        button_play_snake = pygame.Rect(60, 60, 800, 60)
        return button_play_snake

    def button_play_snake_draw(self):
        self.surf_play = self.font2.render('Змейка', True, 'Black')
        pygame.draw.rect(self.display, (0, 106, 138), self.button_play_snake())
        self.display.blit(self.surf_play, (self.button_play_snake().x + 10, self.button_play_snake().y + 10))

    def button_play_snake_hover_draw(self):
        self.surf_play = self.font2.render('Змейка', True, 'Black')
        pygame.draw.rect(self.display, (0, 149, 195), self.button_play_snake())
        self.display.blit(self.surf_play, (self.button_play_snake().x + 10, self.button_play_snake().y + 10))

    def button_play_arcade(self):
        button_play_snake = pygame.Rect(60, 150, 800, 60)
        return button_play_snake

    def button_play_arcade_draw(self):
        self.surf_play = self.font2.render('Arcade', True, 'Black')
        pygame.draw.rect(self.display, (0, 106, 138), self.button_play_arcade())
        self.display.blit(self.surf_play, (self.button_play_arcade().x + 10, self.button_play_arcade().y + 10))

    def button_play_arcade_hover_draw(self):
        self.surf_play = self.font2.render('Arcade', True, 'Black')
        pygame.draw.rect(self.display, (0, 149, 195), self.button_play_arcade())
        self.display.blit(self.surf_play, (self.button_play_arcade().x + 10, self.button_play_arcade().y + 10))

    def button_play_tictactoe(self):
        button_play_snake = pygame.Rect(60, 240, 800, 60)
        return button_play_snake

    def button_play_tictactoe_draw(self):
        self.surf_play = self.font2.render('Крестики-нолики', True, 'Black')
        pygame.draw.rect(self.display, (0, 106, 138), self.button_play_tictactoe())
        self.display.blit(self.surf_play, (self.button_play_tictactoe().x + 10, self.button_play_tictactoe().y + 10))

    def button_play_tictactoe_hover_draw(self):
        self.surf_play = self.font2.render('Крестики-нолики', True, 'Black')
        pygame.draw.rect(self.display, (0, 149, 195), self.button_play_tictactoe())
        self.display.blit(self.surf_play, (self.button_play_tictactoe().x + 10, self.button_play_tictactoe().y + 10))

