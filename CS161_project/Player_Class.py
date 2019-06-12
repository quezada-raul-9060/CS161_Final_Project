class player(object):
    """
    Created a class for the player.

    The class is for a random sprite used.
    Will be able to move left and right, jump, and have a hitbox. 
    """
    def __init__(self, x, y, width, height):
        """
        Names and sets variables for the sprite.

        This code gives the specifics of the sprite.
        Like his actions, location, speed, and dimensions.

        Parameters
        ----------
        arg1 : int
            Takes integer to represent coordinate x.
        arg2 : int
            Takes integer to represent coordinate y.
        arg3 : int
            Takes integer to represent the width of the sprite.
        arg4 : int
            Takes integer to represent the height of the sprite.

        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, window):
        """
        Will draw hitbox and adjust window.

        Sets the window and 'syncronizes' it with the sprite.

        Parameters
        ----------
        arg1 : int
            Uses window variable in code below for adjusting it.

        """
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                window.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                window.blit(walkRight[0], (self.x, self.y))
            else:
                window.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(window, (255,0,0), self.hitbox,2)
