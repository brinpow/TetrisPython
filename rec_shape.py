import pyglet
import game_core

WIDTH, HEIGHT, WIN_HEIGHT = game_core.WIDTH, game_core.HEIGHT, game_core.WIN_HEIGHT


class RecShape:

    def __init__(self, size, batch, color):
        self.rec = pyglet.shapes.Rectangle(0, 0, width=size, height=size, batch=batch, color=color)
        self.size = size

    def can_move(self, x, y, grid):
        cor_x = self.rec.x // self.size
        cor_y = (WIN_HEIGHT - self.rec.y) // self.size

        if cor_x + x >= WIDTH or cor_x + x < 0 or cor_y+y > HEIGHT or (cor_y >= -y and grid[cor_y+y][cor_x+x]):
            return False
        else:
            return True

    def move(self, x=0, y=0):
        self.rec.x += x
        self.rec.y += y

    def stop(self, grid):
        cor_x = self.rec.x // self.size
        cor_y = (WIN_HEIGHT - self.rec.y) // self.size
        try:
            grid[cor_y][cor_x] = self
        except IndexError:
            print('Weird')
