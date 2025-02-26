import pygame


class Button:
    def __init__(self, x, y, w, h, screen, text="Button", onClick=None, colors={"default":"#ffffff","hover":"#666666","clicked":"#333333"}):
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
        self.buttonSurface = pygame.Surface((self.w, self.h))
        self.buttonRect = pygame.Rect(self.x, self.y, self.w, self.h)
        font = pygame.font.SysFont('Arial', 40)
        self.buttonText = font.render(self.text, True, (20, 20, 20))

    def update(self):
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





