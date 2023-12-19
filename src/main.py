import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
TITLE = "Arcanoid"

OBSTACLES_ROW_NUMBER = 2
OBSTACLES_IN_FIRST_ROW = 14
SPACES_FROM_TOP = 1
VERTICAL_OBSTACLES_SPACING = 60
HORIZONTAL_OBSTACLES_SPACING = WIDTH / OBSTACLES_IN_FIRST_ROW
calculate_margin = lambda obstacles_num: ((OBSTACLES_IN_FIRST_ROW - obstacles_num)
                                          / 2) if obstacles_num != OBSTACLES_IN_FIRST_ROW else 0


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


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("obstacle.png"), (60, 60))
        self.rect = pygame.Rect(x, y, 35, 35)

    @staticmethod
    def draw_row(obstacles_num, row, margin):
        for col in range(obstacles_num):
            x = (col + margin) * HORIZONTAL_OBSTACLES_SPACING
            y = (row + SPACES_FROM_TOP) * VERTICAL_OBSTACLES_SPACING
            obstacles.add(Obstacle(x, y))


pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("background.jpg")
clock = pygame.time.Clock()

paddle = Paddle()
ball = Ball()
obstacles = pygame.sprite.Group()
playing = True

for row in range(OBSTACLES_ROW_NUMBER):
    obstacles_per_row = OBSTACLES_IN_FIRST_ROW - row
    Obstacle.draw_row(obstacles_per_row, row, calculate_margin(obstacles_per_row))


while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    paddle.update()
    ball.update()

    hit_obstacles = pygame.sprite.spritecollide(ball, obstacles, True)

    screen.blit(background, (0, 0))

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
