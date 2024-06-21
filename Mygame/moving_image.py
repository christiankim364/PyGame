#import pygame module
import pygame

#initialize pygame
pygame.init()


#Set the background color
background_colour=(150, 225, 240)

#Set the dimensions of the screen from width & height
screen = pygame.display.set_mode((500, 500))

#Set name of Window Screen
pygame.display.set_caption('Moving image left and right')

#Fill the background color of screen
screen.fill(background_colour)

#Load image & Copy Image have to be placed after setting the background
character=pygame.image.load('stick.jpg').convert()

#Copy image
screen.blit(character,(0,0))

#set image co-ordinates
x=220
y=385

#set dimensions of object image
width=20
height=20

#set speed of image object
speed=5

#Updates the entire screens display making any changes visible
pygame.display.flip()

#keeps the game loop running
running=True

# infinite loop
while running:
    # creates time delay of 10ms
    pygame.time.delay(10)

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # it will make exit the while loop
            running = False
    # stores keys pressed
    keys = pygame.key.get_pressed()

    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x > 0:
        # decrement in x co-ordinate
        x -= speed

        # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x < 460 - width:
        # increment in x co-ordinate
        x += speed

    # completely fill the surface object
    # with black colour
    screen.fill(background_colour)

    # Load image & Copy Image have to be placed after setting the background
    screen.blit(character, (x, y))

    # it refreshes the window
    pygame.display.update()

# closes the pygame window
pygame.quit()