# Dependencies
import pygame
from random import randrange

# Init the display
WIDTH, HEIGHT = 1920, 1080 # set display size
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # init display
Win = pygame.display.set_caption("COLOR") # name display
Win = pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0)) # make cursor invisable
Win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # set fullscreen

FPS = 10 # Refresh Rate is fixed, but can be changed; Saves Ressources by limiting updates; Influences Velocities

# function to handle rendering in the window
def draw_window():
    
    rgb = (randrange(256), randrange(256), randrange(256)) # generate a random color
    pygame.draw.rect(WIN, rgb, pygame.Rect(0, 0, WIDTH, HEIGHT)) # draw rect with random color

    pygame.display.update() # update display


def main():

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_window() # execute function in game loop

    main()
    

if __name__ == "__main__":
    main()