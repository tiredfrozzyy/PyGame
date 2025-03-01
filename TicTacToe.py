import pygame
from game_screens import dict_screens, ChangeScreen
from button import *
from screen import GameScreen


class TicTacToe(GameScreen):
    def __init__(self):
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.can_move = 9
        self.x, self.y = 0, 0
        self.flag = "X"
        self.matrix = [["-", "-", "-"] for _ in range(3)]
        self.drawn = False
        self.winner_x = False
        self.winner_0 = False
        self.stenka = 40
        self.color = (0, 0, 0)
        self.block = 200
        self.fon = pygame.image.load('1.jpg')
        self.display = pygame.display.get_surface()
        self.crest = pygame.image.load('crest100.png')
        self.nolik = pygame.image.load('nolik100.png')

    def new_game(self):
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.can_move = 9
        self.x, self.y = 0, 0
        self.flag = "X"
        self.matrix = [["-", "-", "-"] for _ in range(3)]
        self.drawn = False
        self.winner_x = False
        self.winner_0 = False
        self.stenka = 40
        self.color = (0, 0, 0)
        self.block = 200
        self.fon = pygame.image.load('1.jpg')
        self.display = pygame.display.get_surface()

    def check_winner(self):
        for i in self.matrix:
            if i[0] == i[1] == i[2] == "X":
                self.winner_x = True
            elif i[0] == i[1] == i[2] == "0":
                self.winner_0 = True
        for i in range(3):
            if self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] == "X":
                self.winner_x = True
            elif self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] == "0":
                self.winner_0 = True
        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == "X":
            self.winner_x = True
        elif self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] == "0":
            self.winner_0 = True
        if self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == "X":
            self.winner_x = True
        elif self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] == "0":
            self.winner_0 = True
        if self.can_move == 0 and not self.winner_x and not self.winner_0:
            self.drawn = True
        self.winner()

    def draw(self):
        self.display.blit(self.fon, (0, 0))
        for row in range(3):
            for col in range(3):
                x = col * self.block + (col + 1) * self.stenka
                y = row * self.block + (row + 1) * self.stenka
                if self.matrix[row][col] == "X":
                    self.color = (255, 0, 0)
                    self.display.blit(self.crest, (x, y))
                elif self.matrix[row][col] == "0":
                    self.color = (0, 255, 0)
                    self.display.blit(self.nolik, (x, y))
        pygame.draw.rect(self.display, (0, 0, 0), (0, 0, 760, 40))
        pygame.draw.rect(self.display, (0, 0, 0), (0, 240, 760, 40))
        pygame.draw.rect(self.display, (0, 0, 0), (0, 480, 760, 40))
        pygame.draw.rect(self.display, (0, 0, 0), (0, 720, 760, 40))
        pygame.draw.rect(self.display, (0, 0, 0), (0, 0, 40, 760))
        pygame.draw.rect(self.display, (0, 0, 0), (240, 0, 40, 760))
        pygame.draw.rect(self.display, (0, 0, 0), (480, 0, 40, 760))
        pygame.draw.rect(self.display, (0, 0, 0), (720, 0, 40, 760))

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0] // (self.block + self.stenka)
                y = pos[1] // (self.block + self.stenka)
                if self.matrix[y][x] != "X" and self.matrix[y][x] != "0":
                    if self.flag == "X":
                        self.matrix[y][x] = "X"
                        self.flag = "0"
                        self.can_move -= 1
                    elif self.flag == "0":
                        self.matrix[y][x] = "0"
                        self.flag = "X"
                        self.can_move -= 1
        self.check_winner()

    def winner(self):
        if self.winner_0:
            ChangeScreen('win_0')
            self.new_game()
        elif self.winner_x:
            ChangeScreen('win_x')
            self.new_game()
        elif self.drawn:
            ChangeScreen('draw')
            self.new_game()

    def move(self, x, y):
        if 200 <= x <= 500 and 200 <= y <= 500:
            self.x = x
            self.y = y


dict_screens['tictactoe'] = TicTacToe()