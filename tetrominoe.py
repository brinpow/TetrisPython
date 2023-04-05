import random
import pyglet

BATCH = pyglet.graphics.Batch()
SIZE = 25
HEIGHT = 24
WIN_HEIGHT = HEIGHT*SIZE
import rec_shape


class Tetrominoe:
    def __init__(self):
        color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.tetraminoe = [rec_shape.RecShape(SIZE, BATCH, color) for _ in range(4)]
        self.type = random.randint(0, 6)
        self.form = 0

        if self.type == 0:
            self.tetraminoe[0].move(4*SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[1].move(5*SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[2].move(6*SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[3].move(7*SIZE, WIN_HEIGHT + SIZE)
        elif self.type == 1:
            self.tetraminoe[0].move(5 * SIZE, WIN_HEIGHT + 2*SIZE)
            self.tetraminoe[1].move(5 * SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[2].move(6 * SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[3].move(7 * SIZE, WIN_HEIGHT + SIZE)
        elif self.type == 2:
            self.tetraminoe[0].move(4 * SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[1].move(5 * SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[2].move(6 * SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[3].move(6 * SIZE, WIN_HEIGHT + 2*SIZE)
        elif self.type == 3:
            self.tetraminoe[0].move(5 * SIZE, WIN_HEIGHT + 2*SIZE)
            self.tetraminoe[1].move(5 * SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[2].move(6 * SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[3].move(6 * SIZE, WIN_HEIGHT + 2*SIZE)
        elif self.type == 4:
            self.tetraminoe[0].move(5 * SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[1].move(6 * SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[2].move(6 * SIZE, WIN_HEIGHT + 2*SIZE)
            self.tetraminoe[3].move(7 * SIZE, WIN_HEIGHT + 2*SIZE)
        elif self.type == 5:
            self.tetraminoe[0].move(5 * SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[1].move(6 * SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[2].move(6 * SIZE, WIN_HEIGHT + 2*SIZE)
            self.tetraminoe[3].move(7 * SIZE, WIN_HEIGHT + SIZE)
        else:
            self.tetraminoe[0].move(5 * SIZE, WIN_HEIGHT + 2*SIZE)
            self.tetraminoe[1].move(6 * SIZE, WIN_HEIGHT + 2*SIZE)
            self.tetraminoe[2].move(6 * SIZE, WIN_HEIGHT + SIZE)
            self.tetraminoe[3].move(7 * SIZE, WIN_HEIGHT + SIZE)

    def move_down(self, grid):
        if self.tetraminoe[0].can_move(0, 1, grid) and self.tetraminoe[1].can_move(0, 1, grid) \
                and self.tetraminoe[2].can_move(0, 1, grid) and self.tetraminoe[3].can_move(0, 1, grid):
            for rec in self.tetraminoe:
                rec.move(y=-SIZE)
            return True
        else:
            for rec in self.tetraminoe:
                rec.stop(grid)
        return False

    def move(self, x, y, grid):
        if self.tetraminoe[0].can_move(x, y, grid) and self.tetraminoe[1].can_move(x, y, grid) \
                and self.tetraminoe[2].can_move(x, y, grid) and self.tetraminoe[3].can_move(x, y, grid):
            for rec in self.tetraminoe:
                rec.move(x=x*SIZE, y=-y*SIZE)
            return True
        return False

    def change_form(self, grid):
        self.form = (self.form+1) % 4
        tmp = self.tetraminoe
        if self.type == 0:
            if self.form % 2:
                if tmp[2].can_move(0, -1, grid) and tmp[2].can_move(0, 1, grid) and tmp[2].can_move(0, 2, grid):
                    self.tetraminoe[0].move(2*SIZE, SIZE)
                    self.tetraminoe[1].move(SIZE, 0)
                    self.tetraminoe[2].move(0, -SIZE)
                    self.tetraminoe[3].move(-SIZE, -2*SIZE)
            else:
                if tmp[1].can_move(-2, 0, grid) and tmp[1].can_move(-1, 0, grid) and tmp[1].can_move(1, 0, grid):
                    self.tetraminoe[0].move(-2 * SIZE, -SIZE)
                    self.tetraminoe[1].move(-SIZE, 0)
                    self.tetraminoe[2].move(0, SIZE)
                    self.tetraminoe[3].move(SIZE, 2*SIZE)
        elif self.type == 2:
            if self.form == 1:
                if tmp[1].can_move(0, -1, grid) and tmp[1].can_move(0, 1, grid) and tmp[1].can_move(1, 1, grid):
                    self.tetraminoe[0].move(SIZE, SIZE)
                    self.tetraminoe[2].move(-SIZE, -SIZE)
                    self.tetraminoe[3].move(0, -2*SIZE)
            elif self.form == 2:
                if tmp[1].can_move(1, 0, grid) and tmp[1].can_move(-1, 0, grid) and tmp[1].can_move(-1, 1, grid):
                    self.tetraminoe[0].move(SIZE, -SIZE)
                    self.tetraminoe[2].move(-SIZE, SIZE)
                    self.tetraminoe[3].move(-2 * SIZE, 0)
            elif self.form == 3:
                if tmp[1].can_move(0, 1, grid) and tmp[1].can_move(0, -1, grid) and tmp[1].can_move(-1, -1, grid):
                    self.tetraminoe[0].move(-SIZE, -SIZE)
                    self.tetraminoe[2].move(SIZE, SIZE)
                    self.tetraminoe[3].move(0, 2*SIZE)
            else:
                if tmp[1].can_move(1, 0, grid) and tmp[1].can_move(-1, 0, grid) and tmp[1].can_move(1, -1, grid):
                    self.tetraminoe[0].move(-SIZE, SIZE)
                    self.tetraminoe[2].move(SIZE, -SIZE)
                    self.tetraminoe[3].move(2 * SIZE, 0)
        elif self.type == 1:
            if self.form == 1:
                if tmp[2].can_move(0, -1, grid) and tmp[2].can_move(0, 1, grid) and tmp[2].can_move(1, -1, grid):
                    self.tetraminoe[0].move(2 * SIZE, 0)
                    self.tetraminoe[1].move(SIZE, SIZE)
                    self.tetraminoe[3].move(-SIZE, -SIZE)
            elif self.form == 2:
                if tmp[2].can_move(1, 0, grid) and tmp[2].can_move(-1, 0, grid) and tmp[2].can_move(1, 1, grid):
                    self.tetraminoe[0].move(0, -2 * SIZE)
                    self.tetraminoe[1].move(SIZE, -SIZE)
                    self.tetraminoe[3].move(-SIZE, SIZE)
            elif self.form == 3:
                if tmp[2].can_move(0, 1, grid) and tmp[2].can_move(0, -1, grid) and tmp[2].can_move(-1, 1, grid):
                    self.tetraminoe[0].move(-2 * SIZE, 0)
                    self.tetraminoe[1].move(-SIZE, -SIZE)
                    self.tetraminoe[3].move(SIZE, SIZE)
            else:
                if tmp[2].can_move(1, 0, grid) and tmp[2].can_move(-1, 0, grid) and tmp[2].can_move(-1, -1, grid):
                    self.tetraminoe[0].move(0, 2 * SIZE)
                    self.tetraminoe[1].move(-SIZE, SIZE)
                    self.tetraminoe[3].move(SIZE, -SIZE)
        elif self.type == 4:
            if self.form % 2:
                if tmp[1].can_move(1, 0, grid) and tmp[1].can_move(1, 1, grid):
                    self.tetraminoe[0].move(SIZE, SIZE)
                    self.tetraminoe[2].move(SIZE, -SIZE)
                    self.tetraminoe[3].move(0, -2 * SIZE)
            else:
                if tmp[1].can_move(1, 0, grid) and tmp[1].can_move(1, -1, grid):
                    self.tetraminoe[0].move(-SIZE, -SIZE)
                    self.tetraminoe[2].move(-SIZE, SIZE)
                    self.tetraminoe[3].move(0, 2*SIZE)
        elif self.type == 5:
            if self.form == 1:
                if tmp[1].can_move(0, 1, grid):
                    self.tetraminoe[0].move(SIZE, -SIZE)
            elif self.form == 2:
                if tmp[1].can_move(-1, 0, grid):
                    self.tetraminoe[2].move(-SIZE, -SIZE)
            elif self.form == 3:
                if tmp[1].can_move(0, -1, grid):
                    self.tetraminoe[3].move(-SIZE, SIZE)
            else:
                if tmp[1].can_move(1, 0, grid):
                    self.tetraminoe[0].move(-SIZE, SIZE)
                    self.tetraminoe[2].move(SIZE, SIZE)
                    self.tetraminoe[3].move(SIZE, -SIZE)
        elif self.type == 6:
            if self.form % 2:
                if tmp[2].can_move(0, 1, grid) and tmp[2].can_move(1, -1, grid):
                    self.tetraminoe[0].move(2 * SIZE, 0)
                    self.tetraminoe[1].move(SIZE, -SIZE)
                    self.tetraminoe[3].move(-SIZE, -SIZE)
            else:
                if tmp[2].can_move(0, -1, grid) and tmp[2].can_move(-1, -1, grid):
                    self.tetraminoe[0].move(-2 * SIZE, 0)
                    self.tetraminoe[1].move(-SIZE, SIZE)
                    self.tetraminoe[3].move(SIZE, SIZE)

    def check_bounds(self):
        for rec in self.tetraminoe:
            if rec.rec.y >= WIN_HEIGHT:
                return True
        return False
