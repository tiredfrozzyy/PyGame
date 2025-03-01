import pygame
from random import randrange
from game_screens import dict_screens, ChangeScreen
from button import *
from screen import GameScreen


class Arcade(GameScreen):
    def __init__(self):
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.place_w = 330
        self.place_h = 35
        self.place_speed = 15
        self.ball_radius = 20
        self.ball_speed = 6
        self.ball_rect = int(self.ball_speed * 2 ** 0.5)
        self.delta_x = 1
        self.hit = 0
        self.delta_y = -1
        self.rect = 0
        self.display = pygame.display.get_surface()
        self.ball = pygame.Rect(randrange(self.ball_rect, self.WIDTH - self.ball_rect), self.HEIGHT // 2,
                                self.ball_rect, self.ball_rect)
        self.place = pygame.Rect(self.WIDTH // 2 - self.place_w // 2, self.HEIGHT - self.place_h - 10, self.place_w,
                                 self.place_h)
        self.block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
        self.fon = pygame.image.load('1.jpg')
        self.clock = pygame.time.Clock()

    def new_game_arcade(self):
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.place_w = 330
        self.place_h = 35
        self.place_speed = 15
        self.ball_radius = 20
        self.ball_speed = 6
        self.ball_rect = int(self.ball_speed * 2 ** 0.5)
        self.delta_x = 1
        self.hit = 0
        self.delta_y = -1
        self.rect = 0
        self.display = pygame.display.get_surface()
        self.ball = pygame.Rect(randrange(self.ball_rect, self.WIDTH - self.ball_rect), self.HEIGHT // 2,
                                self.ball_rect, self.ball_rect)
        self.place = pygame.Rect(self.WIDTH // 2 - self.place_w // 2, self.HEIGHT - self.place_h - 10, self.place_w,
                                 self.place_h)
        self.block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
        self.fon = pygame.image.load('1.jpg')
        self.clock = pygame.time.Clock()

    def draw(self):
        self.display.blit(self.fon, (0, 0))
        [pygame.draw.rect(self.display, pygame.Color("pink"), block) for color, block in enumerate(self.block_list)]
        pygame.draw.rect(self.display, pygame.Color('orange'), self.place)
        pygame.draw.circle(self.display, pygame.Color('white'), self.ball.center, self.ball_radius)

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        self.place_move()
        self.break_block()
        self.move_ball()
        self.clock.tick(60)

    def collision(self, delta_x, delta_y, ball, rect):
        if delta_x > 0:
            delta_x_ret = ball.right - rect.left
        else:
            delta_x_ret = rect.right - ball.left
        if delta_y > 0:
            delta_y_ret = ball.bottom - rect.top
        else:
            delta_y_ret = rect.bottom - ball.top
        if abs(delta_x_ret - delta_y_ret) < 1:
            delta_x, delta_y = -delta_x, -delta_y
        elif delta_x_ret > delta_y_ret:
            delta_y = -delta_y
        elif delta_y_ret > delta_x_ret:
            delta_x = -delta_x
        return delta_x, delta_y

    def move_ball(self):
        self.ball.x += self.ball_speed * self.delta_x
        self.ball.y += self.ball_speed * self.delta_y
        if self.ball.centerx < self.ball_speed or self.ball.centerx > self.WIDTH - self.ball_radius:
            self.delta_x = -self.delta_x
        if self.ball.centery < self.ball_radius:
            self.delta_y = -self.delta_y
        if self.ball.colliderect(self.place) and self.delta_y > 0:
            self.delta_x, self.delta_y = self.collision(self.delta_x, self.delta_y, self.ball, self.place)
        if self.ball.bottom > self.HEIGHT:
            self.game_over()

    def game_over(self):
        ChangeScreen('game_over')
        self.new_game_arcade()

    def break_block(self):
        self.hit = self.ball.collidelist(self.block_list)
        if self.hit != -1:
            self.hit_rect = self.block_list.pop(self.hit)
            self.delta_x, self.delta_y = self.collision(self.delta_x, self.delta_y, self.ball, self.hit_rect)
            pygame.draw.rect(self.display, False, self.hit_rect)

    def place_move(self):
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_LEFT] and self.place.left > 0:
            self.place.left -= self.place_speed
        if self.key[pygame.K_RIGHT] and self.place.right < self.WIDTH:
            self.place.right += self.place_speed


dict_screens['arcade'] = Arcade()