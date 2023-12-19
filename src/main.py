import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)

TITLE = "Arkanoid"


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("platform.png")
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 30))

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.clamp_ip(screen.get_rect())


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = 10
        self.image = pygame.image.load("ball.png")
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


class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("whole_heart.png"), (40, 40))
        self.rect = self.image.get_rect(topleft=(x, y))

    @staticmethod
    def draw(col):
        x = (col + 1) * 50
        y = 30
        hearts.add(Heart(x, y))

    def set_broken_heart(self):
        self.image = pygame.transform.scale(pygame.image.load("broken_heart.png"), (40, 40))


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load("obstacle.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(x, y))


pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("background.jpg")
clock = pygame.time.Clock()

paddle = Paddle()
ball = Ball()
hearts = pygame.sprite.Group()
lives = 3
obstacles = pygame.sprite.Group()
playing = True

for col in range(lives):
    Heart.draw(col)

obstacle_width = 60
obstacle_height = 60

obstacles_row = 10
obstacles_amount = obstacles_row * 2

horizontal_spacing = WIDTH // (obstacles_row + 1)
vertical_spacing = 60

for row in range(2):
    for col in range(obstacles_row):
        x = (col + 1) * horizontal_spacing
        y = (row + 2) * vertical_spacing
        obstacle = Obstacle(x, y, obstacle_width, obstacle_height)
        obstacles.add(obstacle)

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    paddle.update()
    ball.update()

    hit_obstacles = pygame.sprite.spritecollide(ball, obstacles, True)

    screen.blit(background, (0, 0))

    for heart in hearts:
        screen.blit(heart.image, heart.rect)

    for obstacle in obstacles:
        screen.blit(obstacle.image, obstacle.rect)

    screen.blit(paddle.image, paddle.rect)
    screen.blit(ball.image, ball.rect)

    if not obstacles:
        font = pygame.font.Font(None, 100)
        text = font.render("YOU WON!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(4000)
        playing = False

    pygame.display.flip()

    clock.tick(FPS)
