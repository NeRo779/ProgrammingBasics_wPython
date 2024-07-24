from math import pi

figure_type = str(input())
area = 0

if figure_type == "square":
    length_side = float(input())
    area = length_side * length_side

elif figure_type == "rectangle":
    length_side_one = float(input())
    length_side_two = float(input())
    area = length_side_one * length_side_two

elif figure_type == "circle":
    radius = float(input())
    area = pi * (radius ** 2)

elif figure_type == "triangle":
    length = float(input())
    height = float(input())
    area = length * height / 2

print(f"{area:.3f}")

