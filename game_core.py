import pyglet

import tetrominoe
from pyglet.window.key import *
import os

window = pyglet.window.Window()
BATCH = pyglet.graphics.Batch()
button_batch = pyglet.graphics.Batch()
SIZE = tetrominoe.SIZE
WIDTH = 12
HEIGHT = 24
WIN_WIDTH = WIDTH*SIZE
WIN_HEIGHT = HEIGHT*SIZE
GRID = [[None for j in range(WIDTH)] for i in range(HEIGHT+1)]
pause = False
game_over = False
background = (1, 1, 1)
my_tetrominoe = 0
score = 0

workingDir = os.path.dirname(os.path.realpath(__file__))
pyglet.resource.path = [os.path.join(workingDir, 'resources/images'), os.path.join(workingDir, 'resources/sounds')]
pyglet.resource.reindex()

key_state = set()
key_state_old = set()

score_text = pyglet.text.Label()
pause_text = pyglet.text.Label()
game_over_text = pyglet.text.Label()
line = pyglet.shapes.Line(WIN_WIDTH, 0, WIN_WIDTH, WIN_HEIGHT, batch=BATCH)


@window.event
def on_draw():
    pyglet.gl.glClearColor(*background, 1)
    window.clear()
    BATCH.draw()
    tetrominoe.BATCH.draw()

    score_text.text = f"Score:\n{score}"
    score_text.draw()

    if pause:
        pause_text.draw()
        button_batch.draw()

    if game_over:
        game_over_text.draw()
        button_batch.draw()


@window.event
def on_key_press(symbol, modifiers):
    key_state.add(symbol)


@window.event
def on_key_release(symbol, modifiers):
    key_state.discard(symbol)


def init_scene(fn, color):
    pause_text.font_size = SIZE
    pause_text.font_name = fn
    pause_text.text = "PAUSE"
    pause_text.x = (WIN_WIDTH + 3*SIZE - pause_text.content_width)//2
    pause_text.y = WIN_HEIGHT//2
    pause_text.color = color

    score_text.font_size = SIZE//2
    score_text.font_name = fn
    score_text.width = 3 * SIZE
    score_text.multiline = True
    score_text.x = WIN_WIDTH + 10
    score_text.y = WIN_HEIGHT - score_text.font_size
    score_text.color = color

    game_over_text.font_size = SIZE
    game_over_text.font_name = fn
    game_over_text.text = "GAME OVER"
    game_over_text.x = (WIN_WIDTH + 3 * SIZE - game_over_text.content_width) // 2
    game_over_text.y = WIN_HEIGHT // 2
    game_over_text.color = color

    line._width = 10
    line.color = color[:3]


def key(k):
    return k in key_state


def key_old(k):
    return k in key_state_old


time_sum = 0
time_min = SIZE*1/60*0.6


def move(dt):
    global time_sum, my_tetrominoe, pause, key_state_old, game_over, GRID

    time_sum += dt

    if not game_over:
        if key(P) and not key_old(P):
            pause = not pause

        if not pause:
            if key(A) and not key_old(A):
                my_tetrominoe.move(-1, 0, GRID)

            if key(W) and not key_old(W):
                my_tetrominoe.change_form(GRID)

            if key(D) and not key_old(D):
                my_tetrominoe.move(1, 0, GRID)

            if key(S) and not key_old(S):
                my_tetrominoe.move_down(GRID)

            if time_sum >= time_min:
                time_sum = 0

                if not my_tetrominoe.move_down(GRID):
                    game_over = my_tetrominoe.check_bounds()
                    if game_over:
                        game_over_sound.play()
                    my_tetrominoe = tetrominoe.Tetrominoe()

                GRID.reverse()
                old_grid = [row[:] for row in GRID]
                GRID = []
                rows_deleted = 0
                for index, row in enumerate(old_grid):
                    rec_in_row = 0
                    for rec in row:
                        if rec is not None:
                            rec_in_row += 1
                    if rec_in_row == len(row):
                        global score
                        score += 1
                        rows_deleted += 1
                        try:
                            line_full_sound.play()
                        except Exception:
                            print("Already played")
                    else:
                        GRID.append(row)
                        for rec in row:
                            if rec:
                                rec.move(0, -rows_deleted*SIZE)
                for i in range(HEIGHT+1-len(GRID)):
                    GRID.append([None for _ in range(WIDTH)])

                GRID.reverse()
                old_grid.clear()

    key_state_old = key_state.copy()


def sound(path):
    snd = pyglet.resource.media(path, streaming=True)
    return snd


game_over_sound = sound("gameOver.mp3")
line_full_sound = sound("line_full.wav")


def image(path):
    img = pyglet.resource.image(path)
    img.anchor_x = img.width//2
    img.anchor_y = img.height//2
    img.width = 4*SIZE
    img.height = 2*SIZE
    return img


button_image = image("button_image.png")
replay_button = pyglet.gui.PushButton((WIN_WIDTH+3*SIZE)/2, WIN_HEIGHT/2 - SIZE,
                                      button_image, button_image, batch=button_batch)


@replay_button.event
def on_press():
    global GRID, pause, game_over, score, my_tetrominoe
    GRID = [[None for __ in range(WIDTH)] for _ in range(HEIGHT + 1)]
    pause = False
    game_over = False
    my_tetrominoe = tetrominoe.Tetrominoe()
    score = 0


def play(bg=(1, 1, 1), fs=False, tc=(0.5, 0.5, 0.5), tfn='Broadway'):
    global background, my_tetrominoe

    my_tetrominoe = tetrominoe.Tetrominoe()
    background = bg
    window.set_size(WIN_WIDTH + 3*SIZE, WIN_HEIGHT)
    window.set_fullscreen(fs)

    color = int(255*tc[0]), int(255*tc[1]), int(255*tc[2]), 255
    init_scene(tfn, color)

    pyglet.clock.schedule(move)
    pyglet.app.run()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if pause or game_over:
        replay_button.on_mouse_press(x, y, button, modifiers)


if __name__ == '__main__':
    play((0.1, 0.1, 0.2), False, (1, 1, 1, 255))
