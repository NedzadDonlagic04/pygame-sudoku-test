import pygame
from sys import exit
from classes import *

class Game:
    def __init__(self, width, height, title) -> None:
        pygame.init()

        self.WIDTH = width
        self.HEIGHT = height
        self.SCREEN = pygame.display.set_mode((width, height))
        
        pygame.display.set_caption(title)

        self.CLOCK = MyClock(60)

        cubeWidth = 60
        cubeHeight = 60
        offset = 5

        self.drawFromCubes = [ DrawFromCube(cubeWidth, cubeHeight, i * (cubeWidth + offset), 700, i + 1) for i in range(0, 9) ]
        self.drawOnCubes = [ DrawOnCube(cubeWidth, cubeHeight, i * (cubeWidth + offset), j * (cubeHeight + offset)) for i in range(0, 9) for j in range(0, 9)]

        self.clickedText = ''

    def quit(self) -> None:
        pygame.quit()
        exit()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            for drawOnCubes in self.drawOnCubes:
                drawOnCubes.update(self.clickedText)
                drawOnCubes.draw(self.SCREEN)

            for drawFromCube in self.drawFromCubes:
                state = drawFromCube.update()

                if state is not None:
                    self.clickedText = state

                drawFromCube.draw(self.SCREEN)

            pygame.display.update()
            self.CLOCK.tick()

if __name__ == '__main__':
    game = Game(800, 800, 'Idk')
    game.run()