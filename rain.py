import sys

import pygame
import auxiliary_functions as af
from settings import Settings
from raindrop import Raindrop


# Initialize pygame
pygame.init()

# Initialize settings object to pass to 
settings = Settings()

# Initialize screen
screen = pygame.display.set_mode(settings.screen_dimensions)

# Set screen caption
pygame.display.set_caption("Random Rain")

# Create group for raindrops
raindrops = pygame.sprite.Group()

counter = 0

# Create while loop that only quits with user exit command
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            sys.exit()

    counter+=1
    # Add a drop at a frequency specified in settings
    af.add_drop(settings, screen, raindrops, counter)
    # Move the drops down the screen
    af.update_screen(screen, settings, raindrops)
    # Load new screen from pygame buffer
    pygame.display.flip()




