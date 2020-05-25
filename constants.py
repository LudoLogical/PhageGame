import pygame

pygame.font.init()

# GENERAL VARIABLES
gameW, gameH = 900, 600

# COLORS
black = (0, 0, 0)
grey = (128, 128, 128)
miniGrey = (178, 178, 178)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
lightPurple = (86, 95, 120)

# FONTS
source, sizes = "fonts/muli.ttf", [15, 20, 30, 70]
muli = {}
for s in sizes:
    muli[str(s)] = pygame.font.Font(source, s)

# WASD
W, A, S, D = 0, 1, 2, 3
