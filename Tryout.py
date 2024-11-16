from tkinter import *
import math

def draw_triangle(event):
    cnv.create_rectangle(event.x - 5, event.y - 5,
                         event.x + 5, event.y +5)

def create_star(size, amount, center_x, center_y):
    points = []
    angle = math.pi / 2

    for i in range(amount):
        outer_x = center_x + size * math.cos(angle)
        outer_y = center_y - size * math.sin(angle)
        points.append((outer_x, outer_y))
        angle += 2 * math.pi / amount

        inner_angle = angle - math.pi / amount
        inner_x = center_x + (size / 2) * math.cos(inner_angle)
        inner_y = center_y - (size / 2) * math.sin(inner_angle)
        points.append((inner_x, inner_y))

    return [coord for point in points for coord in point]

window = Tk()

cnv = Canvas(window)
cnv.bind("<Button-1>", draw_triangle)
cnv.pack()

cnv.create_polygon(create_star(50, 5, 0, 0))

window.mainloop()