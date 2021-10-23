import pygame
import sys
from random import randint

pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

bars = [pygame.Surface((8, randint(10, 600))) for _ in range(100)]
for bar in bars:
    bar.fill(white)
rects = [bar.get_rect() for bar in bars]

for i, rect in enumerate(rects):
    rect.move_ip(i * 8, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    for bar, rect in zip(bars, rects):
        screen.blit(bar, rect)

    screen.blit(pygame.transform.flip(screen, False, True), (0, 0))

    pygame.display.flip()
