import pygame

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.colors = self.get_cell_color()


    # Esto imprime la matriz completa
    def print_grid(self):
        """for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end=' ')
            print()"""
        print('\n'.join(' '.join(map(str, row)) for row in self.grid))

    #Esto define los colores de las piezas y las regresa en una lista
    def get_cell_color(self):

        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]

    #Esto dibuja el tablero en la pantalla
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size+1, row*self.cell_size+1,
                                        self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen,self.colors[cell_value],cell_rect)
