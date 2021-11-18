# Import "pygame" module and initialize it
import pygame
pygame.init() 

# Create a game screen and set its title 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Car Racing Game")

# TA1-Step 1: Create a variable "carx" to track car position along x-axis and assign initial value a 140

# TA1-Step 1: Create a variable "cary" to track car position along y-axis and assign initial value a 450


# Game loop
carryOn = True
while carryOn:    
    # Display the background image
    baImg_file = "road.png"
    bgImg = pygame.image.load(baImg_file).convert_alpha()
    bgImg_scaled = pygame.transform.smoothscale(bgImg,(650,600))
    screen.blit(bgImg_scaled,(0,0))
    
    # Update the position of yellow car image based on user input and then display it
    # Load the yellow car image and scale it
    yellow_car_file = "yellow_car.png"
    yellow_car = pygame.image.load(yellow_car_file).convert_alpha()
    yellow_car_scaled = pygame.transform.smoothscale(yellow_car,(230,150))
    
    # Check for the event type
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False              
    
    # TA1-Step 2:Check for the user pressing Up, Down, Right, Left arrow keys and 
    # increment or decrement the "carx" and "cary" varaibles by 10 based on user input 









          
    # TA1-Step 3:Display yellow car image upon updating "carx" and "cary" variable values 

    
    # Update the contents of the display
    pygame.display.flip()
# On the occurence of "pygame.QUIT" event close the game screen.
pygame.quit()