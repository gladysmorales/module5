# Gladys Morales
# February 11th, 2020
# This program asks the user for the number of sides, the length of the side, the color of the line, and the fill color of a regular polygon.

import turtle

polygon = turtle.Turtle()

# Ask the user for the number of sides
number_sides = int(input("How many sides would you like your polygon to have? "))

# Ask the user for the length of the sides
length_sides = int(input("What do you want the length of the sides to be? "))

# Ask the user for the color
color = input("What do you want the color to be? ")

# Ask the user for the fill
fill = input("What do you want the fill to be? ")

for i in range(number_sides+1):
    polygon.forward(length_sides)
    polygon.left(360/number_sides)
    polygon.color(color)