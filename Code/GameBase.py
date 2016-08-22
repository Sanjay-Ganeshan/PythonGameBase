import sys
import pygame
import time
import ColorClass
import GameAssistant
import GameObject
import copy
import random
import GameSettings

from pygame.locals import *


#global colors
#colors = ColorClass.ColorClass()
#global gmtime

def declareGlobals():
    global clearName
    global gmtime
    global windowSize
    global multiplayerEnabled
    global keyState
    global sprites
    global Font
    global winFont
    global gameEnded
    global testObject
    global testObject2
    global quitSequence
    global coolDown

    quitSequence = ["F","U"]

    gameEnded = False
    clearName = 'indianred'
    sprites = {}
    #multiplayerEnabled = False
    windowSize = [500,500]
    keyState = {}

    '''
    Some Test Code
    '''
    
    testObject = GameObject.GameObject(description = "Test Object",identifier = 1, sprite = None, position = [0, windowSize[1] * 0.25], gravityEnabled = True, gravityStrength = [0.0,0.2],tags=["ball","test"],speed=[2,0],size=[30,30],bounded=True,boundingWindow=((0,0),(windowSize[0],windowSize[1])),bounces = True, bounceStrength = 75.0)
    coolDown = 0
    
    #Font = None
    #winFont = None

def Initialize():
    global screen
    global windowSize
    pygame.init()
    screen = pygame.display.set_mode((windowSize[0],windowSize[1]))
    #screen = pygame.display.set_mode(toTuple(windowSize),pygame.FULLSCREEN)
    LoadContent()

def LoadContent():
    global screen
    global song
    global testObject
    global testObject2

    global thisGame
    thisGame = GameAssistant.GameAssistant(GameSettings.Settings.MusicOn)

    '''
    TO LOAD FONTS
    '''
    
    '''
    #fontPaths = pygame.font.match_font("QuartzMS")
    #if fontPaths != None and len(fontPaths) > 1:
    #    #fontPaths = fontPaths[0]
    #print fontPaths,'\n'
    #Font = pygame.font.Font(fontPaths,58)
    #winFont = pygame.font.Font(fontPaths,86)
    '''

    '''
    TO LOAD IMAGES
    '''
    
    '''
    #sprites['Ball'] = pygame.image.load("..\\Content\\ball.png")
    '''

    '''
    Just some testing code for game objects.
    '''
    
    
    testObject.sprite = pygame.image.load("..\\Content\\ball.png")

    testObject2 = copy.deepcopy(testObject)
    testObject2.bounceStrength = 50.0
    testObject2.id = 2
    testObject2.position[0] += 50
    testObject.speed[0] += 0.5
    testObject2.sprite = pygame.image.load("..\\Content\\ball.png")

    testObject3 = copy.deepcopy(testObject2)
    testObject3.bounceStrength = 68.4
    testObject3.id = 3
    testObject3.position[0] += 60
    testObject3.sprite = pygame.image.load("..\\Content\\ball.png")

    testObject4 = copy.deepcopy(testObject3)
    testObject4.bounceStrength = 90.0
    testObject4.id = 4
    testObject4.speed[0] += 2
    testObject4.gravityStrength[0] += 0.03
    testObject4.position[0] += 50
    testObject4.sprite = pygame.image.load("..\\Content\\ball.png")

    #print testObject2.speed
    thisGame.addObject(testObject)
    thisGame.addObject(testObject2)
    thisGame.addObject(testObject3)
    thisGame.addObject(testObject4)
    
    


    global gmtime
    gmtime = time.clock()
    Run(gmtime)

def UnloadContent():
    pass

def Run(gametime):
    while True:
        gametime = Update(gametime) #keeps it running at approximately 60 fps 
        Draw(gametime)

def CheckForEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            UnloadContent() 
            sys.exit()

def Update(gametime):
    global thisGame
    global keyState
    global coolDown

    CheckForEvents()
    getKeyStates()


    #########################
    # Add Update Logic Here #
    #########################

    '''
    Some more testing code
    '''

    
    if keyState['SPACE'] and coolDown == 0:
        balls = thisGame.getObjectsByTag("ball")
        for eachBall in balls:
            eachBall.speed[0] -= random.random() * 4
            eachBall.speed[1] -= random.random() * 10
        coolDown += 1

    if coolDown != 0:
        coolDown += 1
        coolDown %= 10
    


    thisGame.update()

    newTime = time.clock()
    timeToDelay = 0.016 - (newTime - gametime)
    #print time.clock() - To check framrate
    if timeToDelay > 0:
        time.sleep(timeToDelay)
    #print colors.getColors()
    return time.clock() 
def Draw(gametime):
    global colors
    #global testObject
    global thisGame
    global screen
    #######################
    # Add Draw Logic Here #
    #######################
    screen.fill(Color('black'))

    #testObject.draw(screen)
    screen = thisGame.drawAllObjects(screen)

    drawScreen()
    return time.clock()

def drawScreen():
    pygame.display.flip()

def getKeyStates():
    global keyState
    GameAssistant.getKeyStates(keyState,pygame.key.get_pressed())
    '''
    keyState['Down'] = pygame.key.get_pressed()[K_DOWN]
    keyState['Up'] = pygame.key.get_pressed()[K_UP]
    keyState['Right'] = pygame.key.get_pressed()[K_RIGHT]
    keyState['W'] = pygame.key.get_pressed()[K_w]
    keyState['S'] = pygame.key.get_pressed()[K_s]
    keyState['A'] = pygame.key.get_pressed()[K_a]
    keyState['F'] = pygame.key.get_pressed()[K_f]
    keyState['U'] = pygame.key.get_pressed()[K_u]
    '''
    #IMPORTANT: DO NOT REMOVE THIS CODE!!!!! OTHERWISE IT WILL STOP YOUR PROGRAM IMMEDIATELY
    for exitKey in quitSequence:
        if not(keyState[exitKey]):
            return
    
    UnloadContent() 
    sys.exit()

def main():
    declareGlobals()
    Initialize()


if __name__ == '__main__':
    main()