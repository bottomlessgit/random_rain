import pygame

class Settings():
    """Class to keep track of relevant settings"""
    def __init__(self):
        """Initialize settings object"""
        # Screen size settings
        self.screen_dimensions = (1400, 800)
        self.screen_color = (0, 0, 0)

        # Raindrop settings
        self.drop_filename = "raindrop.bmp"
        self.drop_dimensions = (self.drop_width, self.drop_height) = (60, 100)
        self.image_resize_factor = 1.0
        """Frames_per_drop determines the number of frames it takes to release a drop.
        In other words, it is inversely proportional to how heavily it is raining,
        so I higher number means less rain"""
        self.frames_per_drop = 5

        # Image sizing settings
        self.scale_image_by_dimensions = False
        self.scale_image_by_resizing_factor = False

        # Set image value using auxiliary function
        self.prepare_image()

        # Set standard drop falling speed
        self.drop_speed = 2.5
        # Settings for randomly resizing drops (number divided by 10 is size ratio increase)
        self.min_rand_factor = 0
        self.max_rand_factor = 60
        # speed scaling exponent is used to make bigger drops exponentially faster
        self.speed_scaling_exponent = 1.5
        """small size bias is used to decide how strong of a bias towards smaller
        raindrops the program has by calling the randint function that number
        of times when choosing a random sizing factor for a given raindrop object
        The higher the bias the smaller the average drop"""
        self.small_size_bias = 3
        # raindrop acceleration affects how speed of raindrop increases while falling
        # (I set it to 0 as I find no acceleration to be more aesthetically pleasing)
        self.raindrop_acceleration = 0


    def prepare_image(self):
        """Formats image according to specifications in settings. If 
        scale_image_by_dimensions is True then you scale the image according to
        drop_height and drop_width. If it's not true and scale_image_by_resizing_factor
        is True then you scale the image up or down by the resizing factor. Otherwise
        the original image is used."""
        image = pygame.image.load(self.drop_filename)
        image_rect = image.get_rect()
        dimensions = image_rect.size
        if self.scale_image_by_dimensions:
            image = pygame.transform.scale(image, self.drop_dimensions)
        elif self.scale_image_by_resizing_factor:
            new_dimensions = tuple(int(i * self.image_resize_factor) for i in dimensions)
            image = pygame.transform.scale(image, new_dimensions)
        # Now assign image to object for later use
        self.raindrop_image = image







