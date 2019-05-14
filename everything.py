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
if points != 0:
    # Draw mountain range
    deviation_y = 100
    mean_y = 400
    previous_x = 0
    previous_y = random.gauss(mean_y, deviation_y)
    section_w = 1920 / points
    for i in range(points):
        w = random.gauss(section_w, section_w * .25)
        x = previous_x + w
        y = random.gauss(mean_y, deviation_y)
        draw.polygon([(previous_x, previous_y), (x, y), (x, 1080), (previous_x, 1080)], (r - 50, g - 50, b - 50))
        previous_x = x
        previous_y = y
    draw.polygon([(previous_x, previous_y), (1920, random.gauss(mean_y, deviation_y)), (1920, 1080), (previous_x, 1080)], (r - 50, g - 50, b - 50))


# Draw land
draw.rectangle([0, 720, 1920, 1080], (r + 50, g + 50, b + 50))

d = soup.find('div')
d = d.find('div')
d = d.find('div')
d = d.find('div')
print(d)

# Draw headings
def draw_heading(x1, y1, x2, y2):
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    w = random.randint()


# Draw li, ol, table

# Draw p

# Div Section
def div_parsing(html):
    if count_tag("div") > 0:
        return
    else:
        div_parsing(html)


# Cleanup
del draw
del soup

# Show image
#im.show()
# Save image
im.save('landscape.jpg')
