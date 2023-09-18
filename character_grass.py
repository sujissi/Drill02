from pico2d import *


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
isRight = True
isLeft = False
isUp = False
isDown = False

while (True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    if isRight:
        x = x + 2
        if x >= 780:
            isRight = False
            isUp = True
    elif isLeft:
        x = x - 2
        if x <= 0:
            isLeft = False
            isDown = True
    elif isUp:
        y = y + 2
        if y >= 550:
            isUp = False
            isLeft = True
    elif isDown:
        y = y - 2
        if y <= 0:
            isDown = False
            isRight = True
    delay(0.01)
   

close_canvas()
