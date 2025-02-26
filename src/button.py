import pygame


class Button:
    """
    Class representing a Button object
    """
    def __init__(self, x, y, w, h, screen, text="Button", onClick=None, colors={"default":"#ffffff","hover":"#666666","clicked":"#333333"}):
        """
        Initializes a Button object.

        Parameters
        ----------
        x : int
            x position on screen
        y : int
            y position on screen
        w : int
            width of the button
        h : int
            height of the button
        screen : pygame display object
            screen to update to
        text : string
            button text (optional)
        onClick : function
            function to run when button is clicked
        colors : dict
            dictionary of colors for the button; keys: default, hover, clicked
        """
        self.x = x
        self.y = y

        self.w = w
        self.h = h

        self.screen = screen
        self.text = text
        self.onClick = onClick
        self.colors = colors

        self.isClicked = False

        self.generate()

    def generate(self):
        """
        Generates the surfaces for the button
        """
        self.buttonSurface = pygame.Surface((self.w, self.h))
        self.buttonRect = pygame.Rect(self.x, self.y, self.w, self.h)
        font = pygame.font.SysFont('Arial', 40)
        self.buttonText = font.render(self.text, True, (20, 20, 20))

    def update(self):
        """
        Updates the button states and manages clicks
        Call every loop when button exists
        """
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.colors["default"])

        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.colors["hover"])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.colors["clicked"])
                
                if not self.isClicked:
                    self.onClick()
                    self.isClicked = True
            
            else:
                self.isClicked = False
                
        self.buttonSurface.blit(self.buttonText, [
            self.buttonRect.width/2 - self.buttonText.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonText.get_rect().height/2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)





