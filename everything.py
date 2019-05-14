from bs4 import BeautifulSoup as BS
from PIL import Image, ImageDraw
import random

# Soup setup
with open("index.html") as fp:
    soup = BS(fp, 'html.parser')


# Tag Counter
def count_tag(tag_name, html):
    return len(html.find_all(tag_name))


# Tag Counter no recursion
def count_tag_no_rec(tag_name, html):
    return len(html.find_all(tag_name, recursive=False))


# Draw paragraph
def draw_paragraph():
    xp = random.randint(0, 1920)
    yp = random.randint(720, 1080)
    wp = random.randint(-10, 50)
    draw.polygon([(xp, yp), (xp - wp, yp), (xp - wp * .5, yp - wp)], (r + 100, g + 100, b))


# Draw heading
def draw_heading_helper(x1, y1, x2, y2, num):
    xh = random.randint(x1, x2)
    yh = random.randint(y1, y2)
    wh = 10
    print("H1:", xh, yh)
    if num == 1:
        wh = random.randint(-60, 60)
    elif num == 2:
        wh = random.randint(-40, 50)
    elif num == 3:
        wh = random.randint(-30, 40)
    elif num == 4:
        wh = random.randint(-20, 30)
    draw.ellipse([xh, yh, xh + wh, yh + wh], (r + 100, g, b))


# Draw li
def draw_list(x1, y1, x2, y2, sub, num):
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    for i in range(sub + 1):
        # Table
        if num == 1:
            w = random.randint(40, 50)
        # Unordered list
        if num == 3:
            w = random.randint(20, 30)
        draw.rectangle([x - w * i, y - w * i, x - w * (i + 1), y - w * (i + 1)], (r - 100, g - 100, b - 100))


# Draw headings
def draw_heading(x1, y1, x2, y2, html):
    h1_num = count_tag_no_rec('h1', html)
    if h1_num > 0:
        for h1 in range(h1_num):
            print("h1")
            draw_heading(x1, y1, x2, y2, 1)
    h2_num = count_tag_no_rec('h2', html)
    if h2_num > 0:
        for h2 in range(h2_num):
            print("h2")
            draw_heading(x1, y1, x2, y2, 2)
    h3_num = count_tag_no_rec('h3', html)
    if h3_num > 0:
        for h3 in range(h3_num):
            print("h3")
            draw_heading(x1, y1, x2, y2, 3)
    h4_num = count_tag_no_rec('h4', html)
    if h4_num > 0:
        for h4 in range(h4_num):
            print("h4")
            draw_heading(x1, y1, x2, y2, 4)


# Div grouping function
def div_parsing_helper(x1, y1, x2, y2, html):
    ul_num = count_tag_no_rec('ul', html)
    if ul_num > 0:
        next_ul = html.find('ul')
        draw_list(x1, y1, x2, y2, count_tag('li', next_ul), 3)
        draw_heading(x1, y1, x2, y2, next_ul)
        for ul in range(ul_num - 1):
            next_ul = next_ul.find_next_sibling('ul')
            draw_list(x1, y1, x2, y2, count_tag('li', next_ul), 3)
            draw_heading(x1, y1, x2, y2, next_ul)
    table_num = count_tag_no_rec('table', html)
    if ul_num > 0:
        next_ul = html.find('ul')
        draw_list(x1, y1, x2, y2, count_tag('li', next_ul), 3)
        draw_heading(x1, y1, x2, y2, next_ul)
        for ul in range(ul_num - 1):
            next_ul = next_ul.find_next_sibling('ul')
            draw_list(x1, y1, x2, y2, count_tag('li', next_ul), 3)
            draw_heading(x1, y1, x2, y2, next_ul)
    draw_heading(x1, y1, x2, y2, html)
    div_num = count_tag_no_rec("div", html)
    if div_num < 1:
        return
    else:
        c = 300
        x_div = int(random.gauss(960, 500))
        y_div = int(random.gauss(800, 50))
        next_div = html.find("div")
        div_parsing_helper(x_div, y_div, x_div + c, y_div + c, next_div)
        for div in range(div_num - 1):
            x_div = int(random.gauss(960, 500))
            y_div = int(random.gauss(800, 50))
            next_div = next_div.find_next_sibling("div")
            div_parsing_helper(x_div, y_div, x_div + c, y_div + c, next_div)


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
stars = count_tag("link", soup)
print("Stars:", stars)
# Draw Stars
for i in range(stars):
    x = random.randint(0, 1920)
    y = random.randint(0, 720)
    w = random.randint(0, 5)
    draw.rectangle([x, y, x + w, y + w], (225, 225, 225))


# Mountain range setup
points = count_tag("script", soup)
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

# Draw the paragraphs
for p in range(count_tag('p', soup)):
    draw_paragraph()

s = soup.find('body')
div_parsing_helper(0, 720, 1920, 1080, s)

# Cleanup
del draw
del soup

# Show image
im.show()
# Save image
im.save('landscape.jpg')
