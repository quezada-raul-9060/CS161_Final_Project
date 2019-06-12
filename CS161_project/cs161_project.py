#  This is as much as I could to do while understanding most of the code.\
#  Watched few videos on pygame tutorials, mainly Tech With Tim.
#  Didn't finish code, got stuck on how to get SPRITE to stand on blocks.
#  I had told you I was going to make the snake game, but it got to the point\
#  where the code was too much and I could not understand it all.
#  Also kept getting importing error for pygame and caused issues with pylint.
"""
This is a game with a random SPRITE that can jump on blocks to get to a flag.

This code uses pygame and its functions to create the game.
This file contains the code for the BACKground and movement.

Raul Quezada
"""


import pygame

pygame.init()

THE_WINDOW = pygame.display.set_mode((500, 480))

pygame.display.set_caption("First Game")

WALK_RIGHT = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

WALK_LEFT = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

BACK = pygame.image.load('bg.jpg')
CHAR = pygame.image.load('standing.png')

CLOCK = pygame.time.Clock()


class Player():
    """
    Created a class for the Player.

    The class is for a random SPRITE used.
    Will be able to move left and right, jump, and have a hitbox_var.
    """

    def __init__(self, x_var, y_var, width, height):
        """
        Names and sets variables for the SPRITE.

        This code gives the specifics of the SPRITE.
        Like his actions, location, speed, and dimensions.

        Parameters
        ----------
        arg1 : int
            Takes integer to represent coordinate x_var.
        arg2 : int
            Takes integer to represent coordinate y_var.
        arg3 : int
            Takes integer to represent the width of the SPRITE.
        arg4 : int
            Takes integer to represent the height of the SPRITE.

        """
        self.x_var = x_var
        self.y_var = y_var
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False
        self.left = False
        self.right = False
        self.walk_count = 0
        self.jump_count = 10
        self.standing = True
        self.hitbox = (self.x_var + 17, self.y_var + 11, 29, 52)

    def draw(self, the_window):
        """
        Will draw hitbox and adjust WINDOW.

        Sets the WINDOW and 'syncronizes' it with the SPRITE.

        Parameters
        ----------
        arg1 : int
            Uses WINDOW variable in code below for adjusting it.

        """
        for the_brick in BRICKS:
            pygame.draw.rect(the_window, BRICK_COLOR, the_brick)

        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        if not self.standing:
            if self.left:
                THE_WINDOW.blit(WALK_LEFT[self.walk_count // 3], (self.x_var, self.y_var))
                self.walk_count += 1
            elif self.right:
                THE_WINDOW.blit(WALK_RIGHT[self.walk_count // 3], (self.x_var, self.y_var))
                self.walk_count += 1
        else:
            if self.right:
                THE_WINDOW.blit(WALK_RIGHT[0], (self.x_var, self.y_var))
            else:
                THE_WINDOW.blit(WALK_LEFT[0], (self.x_var, self.y_var))
        self.hitbox = (self.x_var + 17, self.y_var + 11, 29, 52)
        pygame.draw.rect(THE_WINDOW, (255, 0, 0), self.hitbox, 2)


def redraw_game_window():
    """
    Redraws WINDOW, SPRITE, and BACKground.

    Takes variables and updates them.

    """
    THE_WINDOW.blit(BACK, (0, 0))
    SPRITE.draw(THE_WINDOW)

    pygame.display.update()


#  Creating blocks for CHARacter to jump on
BRICK_COLOR = (250, 50, 0)
BRICKS = []
for row in range(1):
    for col in range(1):
        brick1 = pygame.Rect(col + 150, row + 300, 60, 20)
        brick2 = pygame.Rect(col + 300, row + 200, 50, 20)
        brick3 = pygame.Rect(col + 150, row + 180, 40, 20)
        brick4 = pygame.Rect(col + 30, row + 160, 30, 20)
        brick5 = pygame.Rect(col + 400, row + 70, 30, 20)
        brick6 = pygame.Rect(col + 240, row + 150, 30, 20)
        BRICKS.append(brick1)
        BRICKS.append(brick2)
        BRICKS.append(brick3)
        BRICKS.append(brick4)
        BRICKS.append(brick5)
        BRICKS.append(brick6)

#  Loops for SPRITE actions and calling Play_varer class.
SPRITE = Player(200, 410, 64, 64)
RUN = True
while RUN:
    CLOCK.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    KEYS = pygame.key.get_pressed()

    if KEYS[pygame.K_LEFT] and SPRITE.x_var > SPRITE.vel:
        SPRITE.x_var -= SPRITE.vel
        SPRITE.left = True
        SPRITE.right = False
        SPRITE.standing = False
    elif KEYS[pygame.K_RIGHT] and SPRITE.x_var < 500 - SPRITE.width - SPRITE.vel:
        SPRITE.x_var += SPRITE.vel
        SPRITE.right = True
        SPRITE.left = False
        SPRITE.standing = False
    else:
        SPRITE.standing = True
        SPRITE.walk_count = 0

    if not SPRITE.is_jump:
        if KEYS[pygame.K_UP]:
            SPRITE.is_jump = True
            SPRITE.right = False
            SPRITE.left = False
            SPRITE.walk_count = 0
    else:
        if SPRITE.jump_count >= -10:
            NEG = 1
            if SPRITE.jump_count < 0:
                NEG = -1
            SPRITE.y_var -= (SPRITE.jump_count ** 2) * 0.5 * NEG
            SPRITE.jump_count -= 1
        else:
            SPRITE.is_jump = False
            SPRITE.jump_count = 10

    redraw_game_window()

pygame.quit()
