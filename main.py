# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #create groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable, shots)

    #create player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_one = Player(x, y)

    #create asteroid field object
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update updateable group
        updateable.update(dt)
        
        #check for collision with player
        for i in asteroids:
            if i.collision_detect(player_one):
                print("GAME OVER")
                sys.exit()

        for i in asteroids:
            for shot in shots:
                if i.collision_detect(shot):
                    i.kill()

        screen.fill((0,0,0))
        
        #Draw all items
        for i in drawable:
            i.draw(screen)

        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
