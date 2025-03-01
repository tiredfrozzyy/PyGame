import pygame
from random import randrange
from game_screens import dict_screens, ChangeScreen
from button import *
from screen import GameScreen


class Snake(GameScreen):
    def __init__(self):
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.SIZE = 50
        self.x = randrange(0, self.WIDTH, self.SIZE)
        self.y = randrange(0, self.HEIGHT, self.SIZE)
        self.apple = randrange(0, self.WIDTH, self.SIZE), randrange(0, self.HEIGHT, self.SIZE)
        self.move = {"W": True, "A": True, "S": True, "D": True}
        self.snake_len = 1
        self.snake = [(self.x, self.y)]
        self.delta_x = 0
        self.delta_y = 0
        self.score = 0
        self.fon = pygame.image.load('1.jpg')
        self.display = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def new_game_snake(self):
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.SIZE = 50
        self.x = randrange(0, self.WIDTH, self.SIZE)
        self.y = randrange(0, self.HEIGHT, self.SIZE)
        self.apple = randrange(0, self.WIDTH, self.SIZE), randrange(0, self.HEIGHT, self.SIZE)
        self.move = {"W": True, "A": True, "S": True, "D": True}
        self.snake_len = 1
        self.snake = [(self.x, self.y)]
        self.delta_x = 0
        self.delta_y = 0
        self.score = 0
        self.fon = pygame.image.load('1.jpg')
        self.display = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def draw(self):
        self.display.blit(self.fon, (0, 0))
        self.font = pygame.font.Font("font.ttf", 28)
        self.font_score = self.font.render(f"SCORE: {self.score}", 1, pygame.Color("orange"))
        self.font_end = self.font.render("GAME OVER", 1, pygame.Color("orange"))
        [(pygame.draw.rect(self.display, pygame.Color("green"), (i, j, self.SIZE - 2, self.SIZE - 2))) for i, j in
         self.snake]
        pygame.draw.rect(self.display, pygame.Color("red"), (*self.apple, self.SIZE, self.SIZE))
        self.display.blit(self.font_score, (5, 5))

    def event_loop(self):
        for event in pygame.event.get():
            self.check_keyboard(event)
            if event.type == pygame.QUIT:
                exit()
        self.move_snake()
        self.clock.tick(15)


    def move_snake(self):
        self.x += self.delta_x * self.SIZE
        self.y += self.delta_y * self.SIZE
        self.snake.append((self.x, self.y))
        self.snake = self.snake[-self.snake_len:]
        if self.snake[-1] == self.apple:
            self.apple = randrange(0, self.WIDTH, self.SIZE), randrange(0, self.HEIGHT, self.SIZE)
            self.snake_len += 1
            self.score += 1
        if self.x < 0 or self.x > self.WIDTH - self.SIZE or self.y < 0 or self.y > self.HEIGHT - self.SIZE or len(self.snake) != len(set(self.snake)):
            self.game_over()

    def game_over(self):
        ChangeScreen('game_over')
        self.new_game_snake()

    def check_keyboard(self, event):
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_w] and self.move["W"]:
                self.delta_x, self.delta_y = 0, -1
                self.move = {"W": True, "A": True, "S": False, "D": True}
            if key[pygame.K_a] and self.move["A"]:
                self.delta_x, self.delta_y = -1, 0
                self.move = {"W": True, "A": True, "S": True, "D": False}
            if key[pygame.K_s] and self.move["S"]:
                self.delta_x, self.delta_y = 0, 1
                self.move = {"W": False, "A": True, "S": True, "D": True}
            if key[pygame.K_d] and self.move["D"]:
                self.delta_x, self.delta_y = 1, 0
                self.move = {"W": True, "A": False, "S": True, "D": True}


dict_screens['snake'] = Snake()