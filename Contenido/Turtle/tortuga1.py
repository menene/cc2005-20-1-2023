# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# 123
#
# Primer programa utilizando turtle
# 09/02/2023
# ==============================================================


import turtle


def cuadrado(largo):
    for numero in range(4):
        santiago.forward(largo)
        santiago.right(90)


window = turtle.Screen()

santiago = turtle.Turtle()
santiago.shape("turtle")
santiago.color("red")

largo = input("Ingrese el largo del cuadrado: ")
cuadrado(int(largo))

# # santiago.penup()
# # santiago.forward(100)
# # santiago.pendown()

# santiago.penup()
# santiago.goto(75, -30)
# santiago.pendown()

# santiago.forward(100)
# santiago.right(90)
# santiago.forward(100)
# santiago.right(90)
# santiago.forward(100)
# santiago.right(90)
# santiago.forward(100)
# santiago.right(90)

# print(santiago.position())


window.exitonclick()
