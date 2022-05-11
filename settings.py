import pygame

class Settings():
    """Class to keep track of relevant settings"""
    def __init__(self):
        """Initialize settings object"""
        # Screen size settings
        self.screen_dimensions = (1200, 800)
        self.screen_color = (0, 0, 0)

        # Raindrop settings
        self.drop_filename = "raindrop.bmp"
        self.drop_width = 60
        self.drop_height = 100
        self.drop_speed = 2.5
        self.edge_space_x = 10
        self.edge_space_y = 10

        # Settings for randomly resizing drops (number divided by 10 is ratio)
        self.min_rand_factor = 0
        self.max_rand_factor = 40
        # speed scaling exponent is used to make bigger drops exponentially faster
        self.speed_scaling_exponent = 2

        """
        To save space and the repetition of effort, and because each raindrop 
        is the same size, I load and scale the image in settings, and pass the
        same image to every instance of the Raindrop class
        """
        # Load image
        self.drop_image = pygame.image.load(self.drop_filename)
        # Scale image
        self.drop_image = pygame.transform.scale(self.drop_image, (self.drop_width, self.drop_height))
