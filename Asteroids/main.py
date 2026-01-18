import pygame
import constants
from logger import log_state



def main():
    SCREEN_WIDTH = constants.SCREEN_WIDTH 
    SCREEN_HEIGHT = constants.SCREEN_HEIGHT
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}", 
          f"\nScreen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
