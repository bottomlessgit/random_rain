# File to hold useful functions for game
from raindrop import Raindrop


def update_drops(raindrops):
    # Update raindrop position
    raindrops.update()

    for drop in raindrops:
        # Check if top of drop is below screen
        if drop.off_screen():
            raindrops.remove(drop)

    for drop in raindrops:
        drop.blitme()


def update_screen(screen, settings, raindrops):
    """Function to update screen"""
    screen.fill(settings.screen_color)
    update_drops(raindrops)