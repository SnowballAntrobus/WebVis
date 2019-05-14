from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageColor
import sys
import random

im = Image.open("index.jpg")
draw = ImageDraw.Draw(im)

draw.rectangle([0, 0, 1920, 1080], (255, 0, 0))


del draw
im.show()
