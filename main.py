import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра тир")
icon = pygame.image.load("img/about-us.jpg")
sound = pygame.mixer.Sound("musik/shmyak.wav")
pygame.display.set_icon(icon)
f1 = pygame.font.Font(None, 35)
hit = 0




target_img = pygame.image.load("img/target.png")
target2_img = pygame.image.load("img/target2_img.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGHT-target_height)

color =(random.randint(0,255), random.randint(0,255), random.randint(0,255))

running = True
while running:
   screen.fill(color)
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y =pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                screen.blit(target2_img, (target_x, target_y))
                sound.play()
                hit = hit+1
                pygame.display.update()
                pygame.time.delay(80)
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            else:
                hit = hit-1
   screen.blit(target_img, (target_x, target_y))
   text1 = f1.render(f"Количество попаданий {hit}", 1, (180, 0, 0))
   screen.blit(text1, (250, 10))
   pygame.display.update()
pygame.quit()
