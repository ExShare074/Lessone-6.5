import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Arkanoid")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Классы игры
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = (screen_width - self.width) // 2
        self.y = screen_height - 20

    def draw(self):
        pygame.draw.rect(screen, white, [self.x, self.y, self.width, self.height])

    def move(self, x):
        self.x = x - self.width // 2
        if self.x < 0:
            self.x = 0
        if self.x > screen_width - self.width:
            self.x = screen_width - self.width

class Ball:
    def __init__(self):
        self.radius = 10
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.dx = 5
        self.dy = -5

    def draw(self):
        pygame.draw.circle(screen, blue, [self.x, self.y], self.radius)

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= 0 or self.x >= screen_width:
            self.dx = -self.dx

        if self.y <= 0:
            self.dy = -self.dy

class Brick:
    def __init__(self, x, y):
        self.width = 75
        self.height = 20
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, white, [self.x, self.y, self.width, self.height])

# Основной игровой цикл
def game_loop():
    paddle = Paddle()
    ball = Ball()
    bricks = []

    for i in range(7):
        for j in range(5):
            bricks.append(Brick(5 + i * 110, 5 + j * 40))

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_x, _ = pygame.mouse.get_pos()
        paddle.move(mouse_x)

        ball.move()

        # Проверка столкновения мяча с ракеткой
        if (paddle.y < ball.y + ball.radius < paddle.y + paddle.height and
                paddle.x < ball.x < paddle.x + paddle.width):
            ball.dy = -ball.dy

        # Проверка столкновения мяча с кирпичами
        for brick in bricks[:]:
            if (brick.y < ball.y - ball.radius < brick.y + brick.height and
                    brick.x < ball.x < brick.x + brick.width):
                ball.dy = -ball.dy
                bricks.remove(brick)

        if ball.y > screen_height:
            running = False

        screen.fill(black)
        paddle.draw()
        ball.draw()

        for brick in bricks:
            brick.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Запуск игры
game_loop()
