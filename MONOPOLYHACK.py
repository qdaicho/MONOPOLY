# MONOPOLYHACK.py
# description

# =============================================================== IMPORT LIBRARIES AND SCREEN SETTINGS ===============================================================
from pygame import *  # all graphics programs we do will need this
# from tkinter import *
from math import *
from random import *

screen = display.set_mode((0, 0), FULLSCREEN)  # Will create an 800 x 600 window. We will
# use the screen variable for all of the drawing we do.

WHITE = (255, 255, 255)
screen.fill(WHITE)

# =============================================================== LOADING IMAGES =====================================================================================
background = image.load("Visuals/monopoly.jpg")
background = transform.scale(background, (850, 850))

# =============================================================== CREATING RECTS =====================================================================================
mainBoard = Rect(30, 30, 840, 840)
FreeParking = Rect(30, 30, 115, 115)
red1 = Rect(145, 30, 70, 115)
blueChance = Rect(215, 30, 70, 115)
red2 = Rect(285, 30, 70, 115)
red3 = Rect(355, 30, 70, 115)
fenchurch = Rect(425, 30, 70, 115)
yellow1 = Rect(495, 30, 70, 115)
yellow2 = Rect(565, 30, 70, 115)
WaterWorks = Rect(635, 30, 70, 115)
yellow3 = Rect(705, 30, 70, 115)
Jail = Rect(766, 30, 115, 115)
green1 = Rect(766, 145, 115, 69)
green2 = Rect(766, 214, 115, 69)
ChestR = Rect(766, 284, 115, 69)
green3 = Rect(766, 354, 115, 69)
liverpool = Rect(766, 424, 115, 69)
orangeChance = Rect(766, 494, 115, 69)
dblue1 = Rect(766, 564, 115, 69)
supertax = Rect(766, 634, 115, 69)
dblue2 = Rect(766, 704, 115, 69)
GO = Rect(766, 766, 115, 115)
brown1 = Rect(705, 768, 70, 115)
ChestB = Rect(635, 768, 70, 115)
brown2 = Rect(565, 768, 70, 115)
incomeTax = Rect(495, 768, 70, 115)
kingcross = Rect(425, 768, 70, 115)
lblue1 = Rect(355, 768, 69, 115)
blueChance = Rect(285, 768, 70, 115)
lblue2 = Rect(215, 768, 70, 115)
lblue3 = Rect(145, 768, 70, 115)
injail = Rect(30, 768, 115, 115)
pink1 = Rect(30, 704, 115, 69)
electricco = Rect(30, 634, 115, 69)
pink2 = Rect(30, 564, 115, 69)
pink3 = Rect(30, 494, 115, 69)
marylebone = Rect(30, 424, 115, 69)
orange1 = Rect(30, 354, 115, 69)
ChestL = Rect(30, 284, 115, 69)
orange2 = Rect(30, 214, 115, 69)
orange3 = Rect(30, 145, 115, 69)

rectList = [FreeParking, red1, blueChance, red2, red3, fenchurch, yellow1, yellow2, WaterWorks, yellow3, Jail, green1,
            green2, ChestR, green3, liverpool, orangeChance, dblue1, supertax, dblue2, GO, brown1,
            ChestB, brown2, incomeTax, kingcross, lblue1, blueChance, lblue2, lblue3, injail, pink1, electricco, pink2,
            pink3, marylebone, ChestL, orange2, orange3]

p1pos = 0
p2pos = 0
turn = 0;
pos = [[735, 830], [665, 834], [594, 835], [518, 832], [442, 837], [384, 837], [319, 837], [247, 834], [178, 837],
       [94, 838], [43, 811], [42, 739], [40, 662], [40, 592], [43, 530], [41, 448], [41, 387]
    , [42, 312], [42, 244], [47, 174], [42, 99], [173, 50], [249, 45], [321, 43], [384, 47], [456, 43], [518, 43],
       [607, 46], [663, 40], [727, 44], [829, 41], [830, 179], [835, 241], [830, 316], [834, 391],
       [834, 465], [831, 529], [839, 598], [838, 655], [838, 739]]
money = [0, 60, 0, 60, 200, 200, 100, 0, 100, 100, 0, 140, 150, 140, 160, 200, 180, 0, 180, 200, 0, 220, 0, 220, 240,
         200, 260, 260, 150, 280, 0, 300, 300, 0, 320, 200, 0, 350, 100, 400]
# =============================================================== FUNCTIONS =====================================================================================
playerplaying = 2


def createBoxes():
    for i in rectList:
        draw.rect(screen, (0, 0, 0), i, 2)


# def movep1(x1,y1,turn):
rollRect = Rect(300, 300, 100, 100)

# =============================================================== MAIN LOOP FOR THE CODE===============================================================================
running = True
while running:

    #######################THIS MODULE DEALS WITH THE EXITING OF THE PROGRAM#########################

    for evt in event.get():  # Windows sends all events that happen to your program. We
        if evt.type == QUIT:  # need to deal with these or our program will slow down/crash.
            running = False  # For now the only event we care about is when the user clicks
            # on the X at the top right corner.
        if evt.type == KEYDOWN:
            if evt.key == K_ESCAPE:
                running = False

    ################################################

    mx, my = mouse.get_pos()  # getting the x and y position of the mouse
    print(len(pos))
    print(len(money))
    if mouse.get_pressed()[0] == 1:  # checking for left click
        print(mx, my)
    createBoxes()
    screen.blit(background, (mainBoard))

    draw.rect(screen, (0, 0, 0), rollRect)
    if mouse.get_pressed()[0] == 1:
        if rollRect.collidepoint(mx, my) and turn == 0:
            num = randint(2, 12)
            if p1pos + num >= len(pos):
                p1pos = (num + p1pos) - len(pos)

            else:
                p1pos = p1pos + num

            turn = 1
        elif rollRect.collidepoint(mx, my) and turn == 1:
            num = randint(2, 12)
            if p2pos + num >= len(pos):
                p2pos = (num + p2pos) - len(pos)

            else:
                p2pos = p2pos + num

            turn = 0

    draw.rect(screen, (255, 255, 0), (pos[p1pos][0], pos[p1pos][1], 30, 30))
    draw.rect(screen, (0, 0, 0), (pos[p2pos][0], pos[p2pos][1], 30, 30))
    # movep1(x1,y1,turn)
    # Draws a single 20 radius red circle at location 400,100
    display.flip()  # Everything we "draw" is actually copied to a place in RAM, this

    # copies that to the actual screen.
quit()  # closes out pygame window
# ================================================================END OF MAIN LOOP FOR THE CODE===========================================================================
