import pyglet

from pyglet import shapes
from pyglet.window import mouse

window = pyglet.window.Window(100, 800)
batch = pyglet.graphics.Batch()

# def gradient(a, b, n):
#     gr = [a]
#     d = (b - a) / (n + 1)
#     for i in range(1, n + 1):  # 0 - a b = 11 n =10 [0,10,20,30,40,50,60,70,80,90,100,110]
#         gr.append(int(gr[i - 1] + d))
#     gr.append(b)
#     return gr


color1 = [255, 50, 100]
color2 = [100, 100, 0]
n = 10


def color_gradient(color1, color2):  # color - a color - b
    color_list = [color1]
    list_d = [0, 0, 0]
    for i in range(3):
        list_d[i] = (color2[i] - color1[i]) / (n + 1)
    for i in range(1, n + 1):
        new_color = [int(color_list[i - 1][0] + list_d[0]), int(color_list[i - 1][1] + list_d[1]),
                     int(color_list[i - 1][2] + list_d[2])]
        color_list.append(new_color)
    color_list.append(color2)
    return color_list


print(color_gradient(color1, color2))
list_color = color_gradient(color1,color2)
height_sh = 50
shape_rect = []
for i in range(n + 2):
    shape_rect.append(
        shapes.Rectangle(x=10, y=10+height_sh*i, width=50, height=height_sh, color=(list_color[i][0],list_color[i][1],list_color[i][2]), batch=batch))


@window.event
def on_draw():
    window.clear()
    batch.draw()


pyglet.app.run()
