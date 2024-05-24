import pygame
import sys  # Import for optional script termination

pygame.init()

screen = pygame.display.set_mode([1280, 960], pygame.RESIZABLE)
pygame.display.set_caption("My Screen")
screen.fill([48, 25, 52])
#Joonistame
pygame.draw.line(screen, [255,0,0], [690,200], [550,300], 2) #Joonistab joone
pygame.draw.rect(screen, [0, 225, 0], [400, 500, 200, 300], 2) #Joonistab ristküliku
pygame.draw.circle(screen, [0, 0, 255], [1000,800], 100, 1) #Joonistab ringi
pygame.draw.polygon(screen, [255, 0, 255], [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2)# Joonistab hulknurga
pygame.draw.ellipse(screen, [0, 225, 0], [1000, 80, 200, 300], 2) #Joonistab ovaali
pygame.draw.arc(screen,[255,255,255], [700,200,250,200], 0, 3.14*1.5, 1)#Joonistab kaart
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        # Essential check for closing the window
        if event.type == pygame.QUIT:
            running = False  # Break out of the main loop
            pygame.quit()   # Clean up Pygame resources
            
            
sys.exit()
