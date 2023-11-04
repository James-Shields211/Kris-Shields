# Kris Shields ETGG1801 Lab11A

# import modules
import pygame
pygame.init()

# create list
values_sequence = [42, "apple", 3.14, True, "a/b", "value", 12, False, 99, "banana"]
index = 0

# print index using while loop
while index < len(values_sequence):
    print(values_sequence[index])
    index += 1

# print index using an index-based for loop
for index in range(len(values_sequence)):
    print(values_sequence[index])

# print index using a value based for loop
for findval in values_sequence:
    print(findval)

# backwards with while loop
index = len(values_sequence) - 1
while index >= 0:
    print(values_sequence[index])
    index -= 1

# backwards with index-based for loop
for index in range(len(values_sequence)-1, -1, -1):
    print(values_sequence[index])

# backwards with value based for loop
for findval in reversed(values_sequence):
    print(findval)

# print every other value in list
while index < len(values_sequence):
    print(values_sequence[index])
    index += 2

# quit pygame
pygame.quit()
