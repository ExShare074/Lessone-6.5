import pygame
pygame.init()
import time

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")

image = pygame.image.load('ps-plus.png')
image_rect = image.get_rect()

image2 = pygame.image.load('Gosling.webp')
image_rect2 = image2.get_rect()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if event.type == pygame.MOUSEMOTION:
        mouseX, mouseY = pygame.mouse.get_pos()
        image_rect.x = mouseX - 600
        image_rect.y = mouseY - 315

    if image_rect.colliderect(image_rect2):
       print("Произошло столкновение")
       time.sleep(1) # Sleep for 1 time


    screen.fill((0, 241, 1))
    screen.blit(image, image_rect)
    screen.blit(image2, image_rect2)


    pygame.display.flip()

pygame.quit()
