import pygame
import sys

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)

TITLE = "Arkanoid"
pygame.display.set_caption(TITLE)

Background = pygame.image.load("images\\1 (1).jpg")

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images\\platform.png")
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 30))

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.clamp_ip(screen.get_rect())

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = 10
        self.image = pygame.image.load("images\\ball.png")
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = pygame.Vector2(5, 5)

    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed.x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed.y *= -1
        if self.rect.colliderect(paddle):
            self.speed.y *= -1

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

paddle = Paddle()
ball = Ball()

