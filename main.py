# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as turtle_module
import random
list_color = [(246, 242, 235), (248, 242, 245), (240, 246, 242), (239, 242, 247), (198, 165, 116), (144, 79, 55), (221, 201, 138), (58, 93, 121), (167, 153, 48), (132, 34, 23), (137, 162, 181), (69, 40, 34), (51, 117, 87), (195, 93, 75), (146, 178, 150), (18, 93, 72), (231, 176, 165), (162, 143, 158), (35, 60, 75), (105, 73, 77), (180, 204, 177), (148, 19, 23), (83, 147, 127), (70, 37, 40), (18, 70, 60), (27, 82, 88), (40, 66, 89), (190, 86, 89), (68, 64, 58), (223, 176, 180), (174, 194, 209), (110, 130, 147), (108, 134, 142), (185, 195, 196)]

tom = turtle_module.Turtle()
turtle_module.colormode(255)
screen = turtle_module.Screen()
tom.hideturtle()
tom.penup()
tom.setheading(225)
tom.forward(150)
tom.setheading(0)
tom.speed("fastest")
tom.hideturtle()

for color_index in range(1, len(list_color) + 1):
    tom.dot(20, random.choice(list_color))
    tom.forward(50)
    if (color_index % 6 == 0):
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(300)
        tom.setheading(0)

screen.exitonclick()
