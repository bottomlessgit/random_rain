# random_rain
Animation of rain random falling on a blank screen  
![](https://github.com/bottomlessgit/random_rain/blob/main/random_rain_example.gif)


## How To Run
### Software Requirements
Space Hunt is written in python 3, so being able to run python code is required. The only module used that is not in the Python Standard Library is the pygame module, a set of modules meant to assist in creating animations and handling collisions(and a number of other game-related functionalities). It's largely a wrapper for SDL(Simple DirectMedia Layer), and it is not unlikely that if you have a computer with which you can code in and run python, the pygame module will work with it.    
To download the latest version of python, go to https://www.python.org/downloads/ and follow the instructions for your OS.  
Your version of python will likely come with python's standard package installer, pip(package installer for python), but if it does not you can download it following the instructions at this link: https://pip.pypa.io/en/stable/installation/    
Finally, if you have pip installed you should be able to use the command
`python3 -m pip install -U pygame`
in your command line to install pygame, but if this does not work and you want more detailed instructions go to https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation
### Running the game
The file containing the executable code is the "rain.py" file. To run the program compile and run this file.


## Settings Manipulation
The settings.py file contains all the settings for the game. You can change the default falling speed of raindrops, how that speed scales with size, change the frequency distribution of how often larger or smaller raindrops fall to bias bigger or smaller drops, change the range of sizes of raindrops, and if you like, add your own image and change the raindrop filename so that it's that image falling instead of raindrops. Have fun! 


## Credits
I both learnt python and specifically the basics of pygame from *Python Crash Course: A Hands-On, Project-Based Introduction to Programming* by Eric Matthes. 
The text can be found for purchase at tbe nostarch publisher's website, https://nostarch.com/pythoncrashcourse2e.  
I'd also like to thank Pete Shinners and the pygame developer community for creating the pygame libraries. 
I also learnt a great deal about pygame from the tutorials and documentation, which can be found at https://www.pygame.org/docs/.


