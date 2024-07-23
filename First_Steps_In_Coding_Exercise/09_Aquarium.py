
length = int(input())
width = int(input())
height = int(input())
percent = float(input())

aquarium_volume = length * width * height
volume_in_litres = aquarium_volume * 0.001
needed_litres = volume_in_litres * (100 - percent) / 100

print(needed_litres)


