import pygame
import sys  

pygame.init()

screen = pygame.display.set_mode([300, 300])
pygame.display.set_caption("Lumemees - Marcus Kosk")


pygame.draw.circle(screen, [255, 255, 255], (150, 75), 40)
pygame.draw.circle(screen, [255, 255, 255], (150, 150), 50)
pygame.draw.circle(screen, [255, 255, 255], (150, 250), 60)
pygame.draw.circle(screen, [0, 0, 0], (160, 70), 5)
pygame.draw.circle(screen, [0, 0, 0], (140, 70), 5)
pygame.draw.line(screen, [245, 119, 22], [145,75], [155,75])


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
