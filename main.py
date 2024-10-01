import pygame
import random
from pygame.examples.go_over_there import screen, target_position

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Игра тир")
icon = pygame.image.load("img/target.png")
pygame.display.set_icon(icon)
target_width = 80
target_height = 80
target_x = random.randint(0, screen_width-target_width)
target_y = random.randint(0, screen_width-target_height)
color =(random.randint(0,255), random.randint(0,255), random.randint(0,255))
running = True
while running:
    pass
pygame.quit()
