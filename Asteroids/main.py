import pygame
import constants
from logger import log_state
import player



def main():

    # Variables
    SCREEN_WIDTH = constants.SCREEN_WIDTH   # Screen
    SCREEN_HEIGHT = constants.SCREEN_HEIGHT # Resolution
    dt = 0  # Delta Time


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}", 
          f"\nScreen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    
    # Initializing pygame function
    pygame.init()

    # Delta time clock
    clock = pygame.time.Clock()
    

    # Screen resolution
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = updatable, drawable
    
    # Player 
    PLAYER = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    # Game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Calculate delta time FIRST
        dt = clock.tick(60) / 1000  # FPS clock
        
        # Update game state
        updatable.update(dt)
        
        # Clear and draw
        screen.fill("black")  # Background color
        for sprite in drawable:
            sprite.draw(screen)  # Draw each sprite using its custom draw method
        
        # Screen refresh
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
