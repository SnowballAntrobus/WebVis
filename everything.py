from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageColor
import sys
import random

im = Image.open("index.jpg")
draw = ImageDraw.Draw(im)

r = random.randint(0, 225)
g = random.randint(0, 225)
b = random.randint(0, 225)

draw.rectangle([0, 0, 1920, 1080], (r, g, b))
draw.rectangle([0, 0, 1920, 720], (r+50, g+50, b+50))


del draw
im.show()
