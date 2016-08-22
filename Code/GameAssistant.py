from pygame.locals import *
import pygame
import glob
import operator

class GameAssistant:
    def __init__(self, enableMusic = True):
        self.objects = []
        if enableMusic:
            allMusic = glob.glob("..\\Content\\Music\\*")
            if len(allMusic) >= 1:
                pygame.mixer.music.load(allMusic[0])
                pygame.mixer.music.play()
                if len(allMusic) >= 2:
                    for eachMusicFile in allMusic[1:]:
                        pygame.mixer.music.queue(eachMusicFile)
    def addObject(self,obj):
        self.objects.append(obj)
    def removeObjectById(self,identifier):
        for eachObject in self.objects:
            if eachObject.id == identifier:
                self.objects.remove(eachObject)
                return True
        return False
    def getObjectById(self,identifier):
        for eachObject in self.objects:
            if eachObject.id == identifier:
                return eachObject
        return None
    def getObjectsByTag(self,searchTag):
        itemList = []
        for eachObject in self.objects:
            if searchTag in eachObject.tags:
                itemList.append(eachObject)
        return itemList
    def getObjectsByDescription(self,desc):
        for eachObject in self.objects:
            if eachObject.description.lower() == desc.lower():
                return eachObject
        return None
    def resetObjectIds(self):
        currId = 0
        descs = []
        for eachObject in self.objects:
            eachObject.id = currId
            descs.append(eachObject.description)
        return descs
    def applyGravity(self):
        for eachObject in self.objects:
            eachObject.applyGravity()
    def updatePositions(self):
        for eachObject in self.objects:
            eachObject.updatePosition()
    def update(self):
        self.applyGravity()
        self.updatePositions()
        self.bounceInBounds()
        outOfBoundsObjects = self.keepInBounds()
        return outOfBoundsObjects
    def keepInBounds(self):
        outOfBoundsObjects = []
        for eachObject in self.objects:
            outX,outY = eachObject.keepInBounds()
            if outX or outY:
                outOfBoundsObjects.append(eachObject)
        return outOfBoundsObjects
    def bounceInBounds(self):
        for eachObject in self.objects:
            eachObject.bounceInBounds()
    def drawAllObjects(self,screen):
        for eachObject in sorted(self.objects, key=operator.attrgetter('drawingLayer')):
            eachObject.draw(screen)
        #screen.flip()
        return screen
    def checkForCollisions(self):
        collisions = []
        for eachObject in self.objects:
            if eachObject.collides:
                for eachOtherObject in self.objects:
                    if eachOtherObject.collides and eachObject != eachOtherObject and not((eachOtherObject,eachObject) in collisions):
                        
                        eoRE = eachObject.position[0] + eachObject.collisionPos[0] + eachObject.collisionSize[0] #right edge
                        eoLE = eachObject.position[0] + eachObject.collisionPos[0] #-- Left edge
                        eoTE = eachObject.position[1] + eachObject.collisionPos[1] #-- Top edge
                        eoBE = eachObject.position[1] + eachObject.collisionPos[1] + eachObject.collisionSize[1] #-- Bottom edge
                        ooRE = eachOtherObject.position[0] + eachOtherObject.collisionPos[0] + eachOtherObject.collisionSize[0] #right edge
                        ooLE = eachOtherObject.position[0] + eachOtherObject.collisionPos[0] #-- Left edge
                        ooTE = eachOtherObject.position[1] + eachOtherObject.collisionPos[1] #-- Top edge
                        ooBE = eachOtherObject.position[1] + eachOtherObject.collisionPos[1] + eachOtherObject.collisionSize[1] #-- Bottom edge
                        '''
                        eoRE = eachObject.position[0]  + eachObject.size[0] #right edge
                        eoLE = eachObject.position[0]  #-- Left edge
                        eoTE = eachObject.position[1]  #-- Top edge
                        eoBE = eachObject.position[1]  + eachObject.size[1] #-- Bottom edge
                        ooRE = eachOtherObject.position[0]  + eachOtherObject.size[0] #right edge
                        ooLE = eachOtherObject.position[0]  #-- Left edge
                        ooTE = eachOtherObject.position[1]  #-- Top edge
                        ooBE = eachOtherObject.position[1]  + eachOtherObject.size[1] #-- Bottom edge
                        '''
                        if eoRE > ooLE and eoLE < ooRE and eoBE > ooTE and eoTE < ooBE: #they are colliding
                            collisions.append((eachObject,eachOtherObject))
        return len(collisions) != 0,collisions
def getKeyStates(dictToMap,pressedKeys):
    dictToMap["TAB"] = pressedKeys[K_TAB]
    dictToMap["CLEAR"] = pressedKeys[K_CLEAR]
    dictToMap["RETURN"] = pressedKeys[K_RETURN]
    dictToMap["PAUSE"] = pressedKeys[K_PAUSE]
    dictToMap["ESCAPE"] = pressedKeys[K_ESCAPE]
    dictToMap["SPACE"] = pressedKeys[K_SPACE]
    dictToMap["EXCLAIM"] = pressedKeys[K_EXCLAIM]
    dictToMap["QUOTEDBL"] = pressedKeys[K_QUOTEDBL]
    dictToMap["HASH"] = pressedKeys[K_HASH]
    dictToMap["DOLLAR"] = pressedKeys[K_DOLLAR]
    dictToMap["AMPERSAND"] = pressedKeys[K_AMPERSAND]
    dictToMap["QUOTE"] = pressedKeys[K_QUOTE]
    dictToMap["LEFTPAREN"] = pressedKeys[K_LEFTPAREN]
    dictToMap["RIGHTPAREN"] = pressedKeys[K_RIGHTPAREN]
    dictToMap["ASTERISK"] = pressedKeys[K_ASTERISK]
    dictToMap["PLUS"] = pressedKeys[K_PLUS]
    dictToMap["COMMA"] = pressedKeys[K_COMMA]
    dictToMap["MINUS"] = pressedKeys[K_MINUS]
    dictToMap["PERIOD"] = pressedKeys[K_PERIOD]
    dictToMap["SLASH"] = pressedKeys[K_SLASH]
    dictToMap["0"] = pressedKeys[K_0]
    dictToMap["1"] = pressedKeys[K_1]
    dictToMap["2"] = pressedKeys[K_2]
    dictToMap["3"] = pressedKeys[K_3]
    dictToMap["4"] = pressedKeys[K_4]
    dictToMap["5"] = pressedKeys[K_5]
    dictToMap["6"] = pressedKeys[K_6]
    dictToMap["7"] = pressedKeys[K_7]
    dictToMap["8"] = pressedKeys[K_8]
    dictToMap["9"] = pressedKeys[K_9]
    dictToMap["COLON"] = pressedKeys[K_COLON]
    dictToMap["SEMICOLON"] = pressedKeys[K_SEMICOLON]
    dictToMap["LESS"] = pressedKeys[K_LESS]
    dictToMap["EQUALS"] = pressedKeys[K_EQUALS]
    dictToMap["GREATER"] = pressedKeys[K_GREATER]
    dictToMap["QUESTION"] = pressedKeys[K_QUESTION]
    dictToMap["AT"] = pressedKeys[K_AT]
    dictToMap["LEFTBRACKET"] = pressedKeys[K_LEFTBRACKET]
    dictToMap["BACKSLASH"] = pressedKeys[K_BACKSLASH]
    dictToMap["RIGHTBRACKET"] = pressedKeys[K_RIGHTBRACKET]
    dictToMap["CARET"] = pressedKeys[K_CARET]
    dictToMap["UNDERSCORE"] = pressedKeys[K_UNDERSCORE]
    dictToMap["BACKQUOTE"] = pressedKeys[K_BACKQUOTE]
    dictToMap["A"] = pressedKeys[K_a]
    dictToMap["B"] = pressedKeys[K_b]
    dictToMap["C"] = pressedKeys[K_c]
    dictToMap["D"] = pressedKeys[K_d]
    dictToMap["E"] = pressedKeys[K_e]
    dictToMap["F"] = pressedKeys[K_f]
    dictToMap["G"] = pressedKeys[K_g]
    dictToMap["H"] = pressedKeys[K_h]
    dictToMap["I"] = pressedKeys[K_i]
    dictToMap["J"] = pressedKeys[K_j]
    dictToMap["K"] = pressedKeys[K_k]
    dictToMap["L"] = pressedKeys[K_l]
    dictToMap["M"] = pressedKeys[K_m]
    dictToMap["N"] = pressedKeys[K_n]
    dictToMap["O"] = pressedKeys[K_o]
    dictToMap["P"] = pressedKeys[K_p]
    dictToMap["Q"] = pressedKeys[K_q]
    dictToMap["R"] = pressedKeys[K_r]
    dictToMap["S"] = pressedKeys[K_s]
    dictToMap["T"] = pressedKeys[K_t]
    dictToMap["U"] = pressedKeys[K_u]
    dictToMap["V"] = pressedKeys[K_v]
    dictToMap["W"] = pressedKeys[K_w]
    dictToMap["X"] = pressedKeys[K_x]
    dictToMap["Y"] = pressedKeys[K_y]
    dictToMap["Z"] = pressedKeys[K_z]
    dictToMap["DEL"] = pressedKeys[K_DELETE]
    dictToMap["KP0"] = pressedKeys[K_KP0]
    dictToMap["KP1"] = pressedKeys[K_KP1]
    dictToMap["KP2"] = pressedKeys[K_KP2]
    dictToMap["KP3"] = pressedKeys[K_KP3]
    dictToMap["KP4"] = pressedKeys[K_KP4]
    dictToMap["KP5"] = pressedKeys[K_KP5]
    dictToMap["KP6"] = pressedKeys[K_KP6]
    dictToMap["KP7"] = pressedKeys[K_KP7]
    dictToMap["KP8"] = pressedKeys[K_KP8]
    dictToMap["KP9"] = pressedKeys[K_KP9]
    dictToMap["KP_PERIOD"] = pressedKeys[K_KP_PERIOD]
    dictToMap["KP_DIVIDE"] = pressedKeys[K_KP_DIVIDE]
    dictToMap["KP_MULTIPLY"] = pressedKeys[K_KP_MULTIPLY]
    dictToMap["KP_MINUS"] = pressedKeys[K_KP_MINUS]
    dictToMap["KP_PLUS"] = pressedKeys[K_KP_PLUS]
    dictToMap["KP_ENTER"] = pressedKeys[K_KP_ENTER]
    dictToMap["KP_EQUALS"] = pressedKeys[K_KP_EQUALS]
    dictToMap["UP"] = pressedKeys[K_UP]
    dictToMap["DOWN"] = pressedKeys[K_DOWN]
    dictToMap["RIGHT"] = pressedKeys[K_RIGHT]
    dictToMap["LEFT"] = pressedKeys[K_LEFT]
    dictToMap["INSERT"] = pressedKeys[K_INSERT]
    dictToMap["HOME"] = pressedKeys[K_HOME]
    dictToMap["END"] = pressedKeys[K_END]
    dictToMap["PAGEUP"] = pressedKeys[K_PAGEUP]
    dictToMap["PAGEDOWN"] = pressedKeys[K_PAGEDOWN]
    dictToMap["F1"] = pressedKeys[K_F1]
    dictToMap["F2"] = pressedKeys[K_F2]
    dictToMap["F3"] = pressedKeys[K_F3]
    dictToMap["F4"] = pressedKeys[K_F4]
    dictToMap["F5"] = pressedKeys[K_F5]
    dictToMap["F6"] = pressedKeys[K_F6]
    dictToMap["F7"] = pressedKeys[K_F7]
    dictToMap["F8"] = pressedKeys[K_F8]
    dictToMap["F9"] = pressedKeys[K_F9]
    dictToMap["F10"] = pressedKeys[K_F10]
    dictToMap["F11"] = pressedKeys[K_F11]
    dictToMap["F12"] = pressedKeys[K_F12]
    dictToMap["F13"] = pressedKeys[K_F13]
    dictToMap["F14"] = pressedKeys[K_F14]
    dictToMap["F15"] = pressedKeys[K_F15]
    dictToMap["NUMLOCK"] = pressedKeys[K_NUMLOCK]
    dictToMap["CAPSLOCK"] = pressedKeys[K_CAPSLOCK]
    dictToMap["SCROLLOCK"] = pressedKeys[K_SCROLLOCK]
    dictToMap["RSHIFT"] = pressedKeys[K_RSHIFT]
    dictToMap["LSHIFT"] = pressedKeys[K_LSHIFT]
    dictToMap["RCTRL"] = pressedKeys[K_RCTRL]
    dictToMap["LCTRL"] = pressedKeys[K_LCTRL]
    dictToMap["RALT"] = pressedKeys[K_RALT]
    dictToMap["LALT"] = pressedKeys[K_LALT]
    dictToMap["RMETA"] = pressedKeys[K_RMETA]
    dictToMap["LMETA"] = pressedKeys[K_LMETA]
    dictToMap["LSUPER"] = pressedKeys[K_LSUPER]
    dictToMap["RSUPER"] = pressedKeys[K_RSUPER]
    dictToMap["MODE"] = pressedKeys[K_MODE]
    dictToMap["HELP"] = pressedKeys[K_HELP]
    dictToMap["PRINT"] = pressedKeys[K_PRINT]
    dictToMap["SYSREQ"] = pressedKeys[K_SYSREQ]
    dictToMap["BREAK"] = pressedKeys[K_BREAK]
    dictToMap["MENU"] = pressedKeys[K_MENU]
    dictToMap["POWER"] = pressedKeys[K_POWER]
    dictToMap["EURO"] = pressedKeys[K_EURO]
