import pygame
import random
from config import WIDTH, HEIGHT, FPS, WHITE, BLACK, RED, GREEN, BLUE


pygame.init()  # старт pygame
pygame.mixer.init()  # тут что-то со звуком
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создание окна
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()  # эт для фпс, но, вроде бы, это просто часы

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # check for closing window
            running = False

    # Обновление

    # Рендеринг
    screen.fill(BLACK)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()  # Для двойной буферизации, что бы это ни было

pygame.quit()