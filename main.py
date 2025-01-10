import sys

import pygame
from Grid import Grid

pygame.init()
dark_blue = (44,44,127)

#Esto setea el tamaño de la ventana en 300 de ancho y 600 de alto
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")

#Esto se utiliza para controlar la velocidad de actualización de tu juego.
clock = pygame.Clock()

#Esto crea un objeto de la clase Grid.
game_grid = Grid()
game_grid.print_grid()

while True:
    #Esto controla los eventos del juego, estamos obteniendo todos los eventos que ocurren en el juego.
    for event in pygame.event.get():
        #Esto está evaluando si el evento es de tipo QUIT, si es así, cerrará la ventana.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Esto pinta la pantalla de color azul.
    screen.fill(dark_blue)
    #Esto dibuja el tablero en la pantalla
    game_grid.draw(screen)
    #Esto actualiza la pantalla del juego.
    pygame.display.update()
    #Esto controla la velocidad de actualización de tu juego (en este caso 60 FPS).
    clock.tick(60)
