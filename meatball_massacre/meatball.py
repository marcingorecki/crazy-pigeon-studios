import pygame, sys, math, os
from pygame.locals import *
from datetime import datetime

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Meatball game')
fpsClock = pygame.time.Clock()

# set up the colors
WHITE = (255, 255, 255)
RED = (0,0,255)
COLOUR_EMPTY_SPACE = (45,82,160)
COLOUR_SPOON = (230,30,30)
COLOUR_MEATBALL = (230,230,30)
COLOUR_WALL = (0,0,0)
COLOUR_SAUCE = (0,0,255)



table=[
       [0,0,0,0,0,1,0,0,0,3],
       [0,0,0,0,0,5,0,1,0,3],
       [0,0,0,1,0,0,0,5,0,3],
       [0,0,0,5,0,0,0,0,0,3]
    ]

table_width=10
table_height=4

mx=0
my=0

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'meatball_resources', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()
    
def render():
    DISPLAYSURF.fill(WHITE)
    for x in range(0,table_width):
        for y in range(0,table_height):            
            if(table[y][x]==0):
                #this is the empty space
                #pygame.draw.rect(DISPLAYSURF,COLOUR_EMPTY_SPACE,(40*x,40*y,40, 40))
                DISPLAYSURF.blit(IMG_desk,(40*x,40*y))
            elif(table[y][x]==1):
                #this is a spoon
                #pygame.draw.rect(DISPLAYSURF,COLOUR_SPOON,(40*x,40*y,40, 40))
                DISPLAYSURF.blit(IMG_spoon_top,(40*x,40*y))
            elif(table[y][x]==5):
                #this is a spoon
                #pygame.draw.rect(DISPLAYSURF,COLOUR_SPOON,(40*x,40*y,40, 40))
                DISPLAYSURF.blit(IMG_spoon_bottom,(40*x,40*y))
            elif(table[y][x]==3):
                #this is the destination
                #pygame.draw.rect(DISPLAYSURF,COLOUR_WALL,(40*x,40*y,40, 40))
                DISPLAYSURF.blit(IMG_plate,(40*x,40*y))
            elif(table[y][x]==2):
                #this is a sauce
                #pygame.draw.rect(DISPLAYSURF,COLOUR_SAUCE,(40*x,40*y,40, 40))
                DISPLAYSURF.blit(IMG_sauce,(40*x,40*y))

    #and this is the meatball!!!
    #pygame.draw.circle(DISPLAYSURF, COLOUR_MEATBALL, (40*mx+20,40*my+20), 20)
    DISPLAYSURF.blit(IMG_meatball,(40*mx,40*my))
    pygame.display.update()

def checkCollision():
    if table[my][mx]==1 or table[my][mx]==5:
        DISPLAYSURF.fill(RED)
        myfont = pygame.font.SysFont("monospace", 40)
        label = myfont.render("MUNCHED HAHAHA!", 1, (WHITE))
        DISPLAYSURF.blit(label, (25, 100))
        pygame.display.update()
        sys.exit()
    
def checkWin():
    if table[my][mx]==3:
        DISPLAYSURF.fill(RED)
        myfont = pygame.font.SysFont("monospace", 40)
        label = myfont.render("CONGRATS", 1, (WHITE))
        DISPLAYSURF.blit(label, (125, 100))
        label = myfont.render("YOU WON!", 1, (WHITE))
        DISPLAYSURF.blit(label, (125, 160))
        pygame.display.update()
        sys.exit()

#initialize images
IMG_meatball=load_image("meatball.png")
IMG_desk=load_image("desk.png")
IMG_plate=load_image("plate.png")
IMG_sauce=load_image("sauce.png")
IMG_spoon_top=load_image("spoon_top.png")
IMG_spoon_bottom=load_image("spoon_bottom.png")

# run the game loop
while True:
    render()


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if mx<9:
                    table[my][mx]=2
                    mx=mx+1
                    checkCollision()
                    checkWin()

            if event.key == pygame.K_LEFT:
                if mx>0:
                    table[my][mx]=2
                    mx=mx-1
                    checkCollision()
                    checkWin()
            if event.key == pygame.K_UP:
                if my>0:
                    table[my][mx]=2
                    my=my-1
                    checkCollision()
                    checkWin()
            if event.key == pygame.K_DOWN:
                if my<3:
                    table[my][mx]=2
                    my=my+1
                    checkCollision()
                    checkWin()
                    
    fpsClock.tick(5)
