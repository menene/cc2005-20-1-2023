# -*- coding: utf-8 -*-

# ==============================================================
# Universidad del Valle de Guatemala
# CC2005 semestre 1 2023
# Sección 20
#
# Erick Marroquin
# 123
#
# Programa que dibuja figuras utilizando ciclos
# 16/02/2023
# ==============================================================

import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.shape("turtle")
t.color("red")

opcion = "0"

while opcion != "4":
    print("")
    print("=== MENU ===")
    print("1. Dibujar cuadrado")
    print("2. Dibujar circulo")
    print("3. Limpiar pantalla")
    print("4. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        # window.reset()
        # t.color("red")

        largo = int(input("Ingrese el largo del cuadrado: "))
        for i in range(4):
            t.forward(largo)
            t.right(90)
    elif opcion == "2":
        # window.reset()
        # t.color("red")

        radio = int(input("Ingrese el radio del circulo: "))

        t.circle(radio)
    elif opcion == "3":
        window.reset()
        t.color("red")
    elif opcion == "4":
        print("Adios")
    else:
        print("Opcion invalida")
