from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90 + 100
r = 100
t = 0

while (True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    
    x = math.cos(t*2*math.pi)*r
    y = math.sin(t*2*math.pi)*r

    delay(0.01)
   

close_canvas()
