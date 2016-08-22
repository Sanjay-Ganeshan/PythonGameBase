import copy
class GameObject:
    def __init__(self,
    description = "object", identifier = 1, tags = [],   
    sprite = None, drawingLayer = 0, 
    position = [0,0], speed = [0,0], size = [], rotation = 0,
    gravityEnabled = False, gravityStrength = [0,0.2], 
    bounceStrength = 0, bounded = False, bounces = False, boundingWindow = None, 
    collides = True, collisionPos = [0,0], collisionSize = [0,0]):
        self.description = description
        self.id = identifier
        self.sprite = sprite
        self.position = position
        self.gravityEnabled = gravityEnabled
        self.gravityStrength = gravityStrength
        self.tags = tags
        self.speed = speed
        self.bounceStrength = bounceStrength
        self.size = size
        self.bounded = bounded
        self.bounces = bounces
        self.boundingWindow = boundingWindow
        self.collides = collides
        self.collisionPos = collisionPos
        self.collisionSize = collisionSize
        self.drawingLayer = drawingLayer
    def copyParent(self, parent):
        self.description = parent.description
        self.id = parent.identifier
        self.sprite = parent.sprite
        self.position = parent.position[:]
        self.gravityEnabled = parent.gravityEnabled
        self.gravityStrength = parent.gravityStrength[:]
        self.tags = parent.tags[:]
        self.speed = parent.speed[:]
        self.bounceStrength = parent.bounceStrength
        self.size = parent.size[:]
        self.bounded = parent.bounded
        self.bounces = parent.bounces
        self.boundingWindow = parent.boundingWindow[:]
        self.collides = parent.collides
        self.collisionPos = parent.collisionPos
        self.collisionSize = parent.collisionSize
        self.drawingLayer = parent.drawingLayer
    def duplicate(self):
        newObj = copy.deepcopy(self)
        return newObj
    def applyGravity(self):
        #print self.speed
        #print self.gravityStrength

        if self.gravityEnabled:
            self.speed[0] += self.gravityStrength[0]
            self.speed[1] += self.gravityStrength[1]
    def updatePosition(self):
        #self.applyGravity()
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
    def keepInBounds(self,windowCorners = None):
        wasOutOfBoundsX = False
        wasOutOfBoundsY = False
        if windowCorners == None:
            if self.bounded:
                if(self.position[0] < self.boundingWindow[0][0]):
                    self.position[0] = self.boundingWindow[0][0]
                    wasOutOfBoundsX = True
                if(self.position[1] < self.boundingWindow[0][1]):
                    self.position[1] = self.boundingWindow[0][1]
                    wasOutOfBoundsY = True
                if(self.position[0] + self.size[0] > self.boundingWindow[1][0]):
                    self.position[0] = self.boundingWindow[1][0] - self.size[0]
                    wasOutOfBoundsX = True
                if(self.position[1] + self.size[1] > self.boundingWindow[1][1]):
                    self.position[1] = self.boundingWindow[1][1]-self.size[1]
                    wasOutOfBoundsY = True
        else:
            if(self.position[0] < windowCorners[0][0]):
                self.position[0] = windowCorners[0][0]
                wasOutOfBoundsX = True
            if(self.position[1] < windowCorners[0][1]):
                self.position[1] = windowCorners[0][1]
                wasOutOfBoundsY = True
            if(self.position[0] + self.size[0] > windowCorners[1][0]):
                self.position[0] = windowCorners[1][0] - self.size[0]
                wasOutOfBoundsX = True
            if(self.position[1] + self.size[1] > windowCorners[1][1]):
                self.position[1] = windowCorners[1][1] - self.size[1]
                wasOutOfBoundsY = True
        #print self.position
        return (wasOutOfBoundsX,wasOutOfBoundsY)

    def bounceInBounds(self,windowCorners = None):
        didBounceX = False
        didBounceY = False
        if self.bounces:
            bounceSides = self.keepInBounds(windowCorners)
            if bounceSides[0]:
                #print self.speed[0] * 1
                #print self.bounceStrength 
                self.speed[0] *= -1.0 * self.bounceStrength / 100.0
                didBounceX = True
            if bounceSides[1]:
                self.speed[1] *= -1.0 * self.bounceStrength / 100.0
                didBounceY = True
        return (didBounceX,didBounceY)

    def draw(self,screen):
        screen.blit(self.sprite,(self.position[0],self.position[1]))