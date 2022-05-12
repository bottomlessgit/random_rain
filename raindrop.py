from random import randint
import pygame
from settings import Settings

# Give the class a settings object for creating class-level raindrop array
p_settings = Settings()

"""So we don't need to repeatedly scale images of randomly-sized randrops for each
raindrop, we prepare an array of all possible sized raindrop images and give 
each raindrop object the raindrop image of appropriate size"""
# Get dimensions of raindrop image scaled in settings from image rect
drop_rect = p_settings.raindrop_image.get_rect()
drop_images = [pygame.transform.scale(
    p_settings.raindrop_image, 
    (int(drop_rect.w * (1 + x / 10)), int(drop_rect.h * (1 + x / 10)))
        ) for x in range(p_settings.min_rand_factor, p_settings.max_rand_factor)]


def generate_rand_factor(settings):
    """Generates a random factor with bias towards smaller numbers"""
    # First generate random scaling number within chosen bounds
    result = randint(settings.min_rand_factor, settings.max_rand_factor)
    # Call randint on number to scale down randomly chosen number of times
    for random_call in range(settings.small_size_bias):
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

        # Choose random integer factor for scaling up attributes
        self.random_factor = generate_rand_factor(settings)

        # Create scaling-up factor based on random_factor
        scale_up_factor = (1 + self.random_factor / 10)

        """The integer scale-up factor can be mapped to an already scaled
        image scaled in the aforementioned scaled raindrop array"""
        self.image = drop_images[self.random_factor]

        # Initialize rect, drop will be positioned by create_drops function
        self.rect = self.image.get_rect()
        self.speed = settings.drop_speed * scale_up_factor ** settings.speed_scaling_exponent
        self.raindrop_acceleration = settings.raindrop_acceleration * self.speed


        # randomize position at top of screen
        self.rect.bottom = self.screen_rect.top
        self.precise_y = float(self.rect.y)
        self.rect.x = randint(0 - self.rect.width, self.screen_rect.right)


    def update(self):
        """Update the position of the raindrop"""
        self.precise_y += self.speed
        self.rect.y = int(self.precise_y)
        self.speed += self.raindrop_acceleration

    def blitme(self):
        """Draw raindrop to screen"""
        self.screen.blit(self.image, self.rect)

    def off_screen(self):
        """Checks if randrop is off-screen"""
        if self.rect.top > self.screen_rect.bottom:
            return True
        else:
            return False

