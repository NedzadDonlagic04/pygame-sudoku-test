import pygame

class MyClock:
    def __init__(self, fps) -> None:
        self.CLOCK = pygame.time.Clock()
        self.FPS = fps
    
    def tick(self) -> None:
        self.CLOCK.tick(self.FPS)

class CubeWithText:
    def __init__(self, width, height, x, y, text='', color=(255, 255, 255)) -> None:
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = self.image.get_rect( topleft = (x, y) )

        self.font = pygame.font.Font(None, 30)
        self.textColor = (0, 0, 0)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.setText(text)
    
    def checkCollisionWithMouse(self) -> bool:
        click = pygame.mouse.get_pressed()[0]

        if click:
            pos = pygame.mouse.get_pos()

            if pos[0] >= self.rect.left and pos[0] <= self.rect.right and pos[1] >= self.rect.top and pos[1] <= self.rect.bottom:
                return True
        
        return False
    
    def setText(self, text) -> None:
        self.text = str(text)
        self.textImage = self.font.render(self.text, True, self.textColor)
        self.textRect = self.textImage.get_rect( center = ( self.x + self.width / 2, self.y + self.height / 2) )
    
    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)
        screen.blit(self.textImage, self.textRect)

class DrawFromCube(CubeWithText):
    def __init__(self, width, height, x, y, text) -> None:
        super().__init__(width, height, x, y, text)

    def update(self) -> None:
        if self.checkCollisionWithMouse():
            return self.text

class DrawOnCube(CubeWithText):
    def __init__(self, width, height, x, y) -> None:
        super().__init__(width, height, x, y)

    def update(self, text) -> None:
        if self.checkCollisionWithMouse():
            self.setText(text)