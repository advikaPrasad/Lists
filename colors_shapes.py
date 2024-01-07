# this code will list out colors and shapes and create a colors_shapes list
import turtle

win = turtle.Screen()
win.setup(800,600)
win.title('colors and shapes')

t = turtle.Turtle()
t.speed("slowest")
t.pencolor("maroon")
t.pensize(3)

myfont = ("Arial", "230", "bold")

#adding items to a list

colors = []

colors.append("red")
colors.append("orange")
colors.append("yellow")
colors.append("green")
colors.append("blue")
colors.append("indigo")
colors.append("purple")
colors.append("pink")
t.write(colors)
t.hideturtle()

#joing lists

shapes = ["square","rectangle","triangle","circile","heart"]

colors_shapes = colors + shapes

t.write(colors_shapes)



