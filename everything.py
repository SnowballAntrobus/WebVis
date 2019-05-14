from bs4 import BeautifulSoup as BS
from PIL import Image, ImageDraw, ImageColor
import sys
import random

# Soup setup
with open("index.html") as fp:
    soup = BS(fp, 'html.parser')


# Tag Counter
def count_tag(tag_name):
    return len(soup.find_all(tag_name))


# Image setup
im = Image.open("index.jpg")
draw = ImageDraw.Draw(im)

# Base random number
r = random.randint(0, 225)
g = random.randint(0, 225)
b = random.randint(0, 225)

# Draw land
draw.rectangle([0, 0, 1920, 1080], (r + 50, g + 50, b + 50))
# Draw sky
draw.rectangle([0, 0, 1920, 720], (r, g, b))

# Stars setup
stars = count_tag("link")
print("Stars:", stars)
# Draw Stars
for i in range(stars):
    x = random.randint(0, 1920)
    y = random.randint(0, 720)
    w = random.randint(0, 5)
    draw.rectangle([x, y, x + w, y + w], (225, 225, 225))


# Mountain range setup
points = count_tag("script")
print("Points:", points)

del draw
im.show()
im.save('landscape.jpg')
