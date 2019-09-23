import time  # Imported time for clock() which waits for some seconds
import pygame # Main module for Game
import random  # Imported for Randomly placing apple on screen
#main programming goes from here.
gameover = False
pygame.init() # Initialise the gamescreen or pygame window
gamescreen = pygame.display.set_mode((800, 600)) # Sets the screen resolution(800X600)
pygame.display.set_caption("Snake V1.0") # Title for game
img = pygame.image.load('head1.png') # SnakeHead image
appleimg = pygame.image.load("applelogo.png") # Apple Image
black=(0,0,0)
Blue=(0,0,255)
White = (255, 255, 255)
green = (0,155,0)
pink=(255,192,203)
Light_Green = (34,252,194)
crimson = (220,20,60)
clock = pygame.time.Clock() # Created Object of clock()
size=10
direction = "Right"

def msg_on_screen(msg,type): # renders text on screen at the centre of the screen
    font = pygame.font.Font('freesansbold.ttf',30)#created Font object
    Screen_text = font.render(msg,True,type)
    textrect = Screen_text.get_rect()#Function for returning positioning of the centre position
    textrect.center = (400,300)
    gamescreen.blit(Screen_text,textrect)
def msg_Normal(text,type,pos): # Normal Message That not to be centered can be rendered on any position
    font = pygame.font.Font('freesansbold.ttf', 30)
    Screen_text = font.render(text, True, type)
    textrect = Screen_text.get_rect()
    textrect.center = (pos)
    gamescreen.blit(Screen_text, textrect)
def snake(size,snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "Left":
        head = pygame.transform.rotate(img, 90)
    if direction == "Up":
        head = img
    if direction == "Down":
        head = pygame.transform.rotate(img, 180)
    gamescreen.blit(img,(snakelist[-1][0],snakelist[-1][1]))
    for xy in snakelist[:-1]:
        pygame.draw.rect(gamescreen,green,(xy[0],xy[1],10,10))

def introduction(): # Welcome Screen
    intro = True
    while intro:
        gamescreen.fill(White)
        msg_on_screen("Welcome", black)
        msg_Normal("To Snake Game",black,(400,350))
        msg_Normal("Press Space To Start", Blue,(400,400))
        msg_Normal("Press A For About", Blue,(400,450))
        msg_Normal("Press Esc To Quit",Blue,(400,500))
        pygame.display.update()
        clock.tick(15)

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if events.key == pygame.K_a:
                    About()
                if events.key == pygame.K_SPACE:
                    gameloop()
def About():#Warning!!! :  Dont make any changes in this function.
    About = False
    gamescreen.fill(White)
    pygame.display.update()
    while not About:
        msg_Normal("About",Blue,(400,50))
        msg_Normal("Developed By : Abhay Gupta",Light_Green,(400,100))
        msg_Normal("Instagram : @abhaygupta1609",green,(400,150))
        msg_Normal("Email - Akgupta0777@gmail.com",pink,(400,200))
        msg_Normal("Press Backspace for Previous menu",Blue,(400,500))
        msg_Normal("Call for any query - +919354942524",black,(400,300))
        pygame.display.flip()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    introduction()
                    About = True
def Score(score): #Renders Score on the screen
    scorefont = pygame.font.Font('freesansbold.ttf', 30)
    text = scorefont.render("Score : " + str(score), True, black)
    gamescreen.blit(text,(0,0))
    pygame.display.update()
def gameloop(): # Main loop for Game
    global direction
    AppleX = round(random.randrange(10,780,10)/10.0)*10.0
    AppleY = round(random.randrange(10,580,10)/10.0)*10.0
    red = (255, 0, 0)
    lead_x = 300
    lead_y = 300
    lead_x_change = 10
    lead_y_change = 0
    gameClose = False
    snakelist=[]
    snakelen = 1
    while not gameClose:
        for events in pygame.event.get():  # Events Handling
            print(events) # For Logs
            if events.type == pygame.QUIT:
                gameClose = True
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RIGHT:
                    direction = "Right"
                    lead_x_change += 10
                    lead_y_change = 0
                elif events.key == pygame.K_LEFT:
                    direction = "Left"
                    lead_x_change -= 10
                    lead_y_change = 0
                elif events.key == pygame.K_UP:
                    direction = "Up"
                    lead_y_change -= 10
                    lead_x_change = 0
                elif events.key == pygame.K_DOWN:
                    direction = "Down"
                    lead_y_change += 10
                    lead_x_change=0
            if events.type == pygame.KEYUP:
                if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
                    lead_x_change = 0
                elif events.key == pygame.K_DOWN or events.key == pygame.K_UP:
                    lead_y_change = 0

        if lead_x >= 800 or lead_x < 10 or lead_y >= 600 or lead_y < 0: # Condition For Boundaries
            gameover = True
            while gameover == True:
                gamescreen.fill(White)
                msg_on_screen("Press Space To Retry or Esc To QUIT", red)
                msg_Normal("Your Score is "+ str(score),red,(400,400))
                pygame.display.update()
                for events in pygame.event.get():
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_SPACE:
                            gameover = False
                            gameloop()
                        elif events.key == pygame.K_ESCAPE:
                            gameClose = True
                            gameover = False
            time.sleep(2)

        lead_x += lead_x_change
        lead_y += lead_y_change
        clock.tick(20)
        gamescreen.fill(White)
        pygame.draw.rect(gamescreen, green, (lead_x, lead_y, 10, 10))
        gamescreen.blit(appleimg,(AppleX,AppleY,10,10))
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        snake(size, snakelist)
        if len(snakelist) > snakelen:
            del snakelist[0]
        #snake(size, snakelist)
        score = snakelen - 1
        Score(score)
        pygame.display.update()
        if lead_x == AppleX and lead_y == AppleY:
            AppleX = round(random.randrange(10, 780, 10) / 10.0) * 10.0
            AppleY = round(random.randrange(10, 580, 10) / 10.0) * 10.0
            snakelen += 1
            pygame.display.update()

introduction()
gameloop()
pygame.quit()
quit()


