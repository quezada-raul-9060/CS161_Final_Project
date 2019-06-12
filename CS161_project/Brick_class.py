class theBrick(object):
    """
    Created a class for the brick.

    The class is for a brick/rectangle created.
    Will make a hitbox for the brick.
    """

    def __init__(self, x, y, width, height):
        """
        Sets variables for the brick.

        This code gives the specifics of the brick.
        Like his dimensions location.

        Parameters
        ----------
        arg1 : int
            Takes integer to represent coordinate x.
        arg2 : int
            Takes integer to represent coordinate y.
        arg3 : int
            Takes integer to represent the width of the brick.
        arg4 : int
            Takes integer to represent the height of the brick.

        """
        self.x = x
        self.y = y
        self.width = width
        self.height = width
        self.hitbox = (self.x + 150, self.y + 300, 60, 20)

    def draw(self, window):
        self.hitbox = (self.x + 150, self.y + 300, 60, 20)
        pygame.draw.rect(window, (0, 255, 0), self.hitbox, 2)
