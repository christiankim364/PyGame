import pygame

#Set the background color
background_colour=(150, 225, 240)

#Set the dimensions of the screen from width & height
screen = pygame.display.set_mode((500, 500))


#Set name of Window Screen
pygame.display.set_caption('First Python Game Background')

#Fill the background color of screen
screen.fill(background_colour)

#Load image & Copy Image have to be placed after setting the background
character=pygame.image.load('stick.jpg').convert()

#Copy image
screen.blit(character,(0,0))



#Updates the entire screens display making any changes visible
pygame.display.flip()

#keeps the game loop running
running=True

#game while loop, YOU MUST INDENT IN PYTHON FOR LOOPS TO WORK!
while running:

#game for loop
    for event in pygame.event.get():

#Checks if user closes the window
        if event.type==pygame.QUIT:
            running=False
