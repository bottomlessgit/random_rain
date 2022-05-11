from random import randint
import pygame
from settings import Settings

p_settings = Settings()

drop_image = pygame.image.load("raindrop.bmp")
drop_images = [pygame.transform.scale(
    drop_image, 
    (int(p_settings.drop_width * (1 + x / 10)), int(p_settings.drop_height * (1 + x / 10)))
        ) for x in range(p_settings.min_rand_factor, p_settings.max_rand_factor)]


def generate_rand_factor(settings):
    """Generates a random factor with bias towards smaller numbers"""
    result = randint(settings.min_rand_factor, settings.max_rand_factor)
    result = randint(settings.min_rand_factor, result)
    result = randint(settings.min_rand_factor, result)
    result = randint(settings.min_rand_factor, result)
    return result

class Raindrop(pygame.sprite.Sprite):
    """Class represeting raindrop to be drawn to screen"""


    def __init__(self, settings, screen):
        """Initializes raindrop object"""
        # Initialize sprite sttributes
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Choose random factor for scaling up attributes

        # self.random_factor = randint(settings.min_rand_factor, settings.max_rand_factor - 1)
        self.random_factor = generate_rand_factor(settings)

        # Create scaling-up factor based on random_factor
        scale_up_factor = (1 + self.random_factor / 10)

        self.image = drop_images[self.random_factor]

        # Initialize rect, drop will be positioned by ccreate_drops function
        self.rect = self.image.get_rect()
        self.speed = settings.drop_speed * scale_up_factor ** settings.speed_scaling_exponent


        # randomize position at top of screen
        self.rect.bottom = self.screen_rect.top
        self.precise_y = float(self.rect.y)
        self.rect.x = randint(0 - self.rect.width, self.screen_rect.right)


    def update(self):
        """Update the position of the raindrop"""
        self.precise_y += self.speed
        self.rect.y = int(self.precise_y)
        # self.speed += .05

    def blitme(self):
        """Draw raindrop to screen"""
        self.screen.blit(self.image, self.rect)

    def off_screen(self):
        """Checks if randrop is off-screen"""
        if self.rect.top > self.screen_rect.bottom:
            return True
        else:
            return False

