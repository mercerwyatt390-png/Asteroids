import sys
import pygame
import constants
from logger import log_state, log_event
import player
import asteroid
import asteroidfield
import shot


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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = updatable, drawable
    asteroid.Asteroid.containers = updatable, drawable, asteroids
    asteroidfield.AsteroidField.containers = updatable
    shot.Shot.containers = updatable, drawable, shots

    # Asteroid Field
    ASTEROID_FIELD = asteroidfield.AsteroidField()

    
    # Player 
    PLAYER = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Shooting
    SHOT = shot.Shot(0, 0, pygame.Vector2(0, 0))

    
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
        PLAYER.fire_cooldown = max(0, PLAYER.fire_cooldown - dt)
        for rock in list(asteroids):
            for bullet in shots:
                if rock.collide_with(bullet):
                    log_event("asteroid_shot")
                    rock.split()
                    bullet.kill()
        
        for rock in asteroids:
            if rock.alive() and rock.collide_with(PLAYER):
                log_event("player_hit")
                print("Player hit an asteroid!")
                print("Game Over!")
                sys.exit()
        
        # Clear and draw
        screen.fill("black")  # Background color
        for sprite in drawable:
            sprite.draw(screen)  # Draw each sprite using its custom draw method
        
        # Screen refresh
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
