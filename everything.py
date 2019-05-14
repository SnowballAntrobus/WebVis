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
def draw_heading(x1, y1, x2, y2, num):
    xh = random.randint(x1, x2)
    yh = random.randint(y1, y2)
    wh = 10
    if num == 1:
        wh = random.randint(-60, 60)
    elif num == 2:
        wh = random.randint(-40, 50)
    elif num == 3:
        wh = random.randint(-30, 40)
    elif num == 4:
        wh = random.randint(-20, 30)
    draw.ellipse([xh, yh, xh + wh, yh + wh], (r + 100, g, b))


# Draw a tag
def draw_a_tag(x1, y1, x2, y2):
    xa = random.randint(x1, x2)
    ya = random.randint(y1, y2)
    wa = random.randint(0, 2)
    draw.rectangle([xa, ya, xa + wa, ya + wa], (r, g, b + 100))


# Draw span tag
def draw_s_tag(x1, y1, x2, y2):
    xs = random.randint(x1, x2)
    ys = random.randint(y1, y2)
    ws = random.randint(0, 2)
    draw.rectangle([xs, ys, xs + ws, ys + ws], (r, g, b + 100))


# Draw headings and paragraphs no recursion
def run_draw_h_p_a_s(x1, y1, x2, y2, html):
    p_num = count_tag_no_rec('p', html)
    if p_num > 0:
        for p in range(p_num):
            draw_paragraph()
    h1_num = count_tag_no_rec('h1', html)
    if h1_num > 0:
        for h1 in range(h1_num):
            draw_heading(x1, y1, x2, y2, 1)
    h2_num = count_tag_no_rec('h2', html)
    if h2_num > 0:
        for h2 in range(h2_num):
            draw_heading(x1, y1, x2, y2, 2)
    h3_num = count_tag_no_rec('h3', html)
    if h3_num > 0:
        for h3 in range(h3_num):
            draw_heading(x1, y1, x2, y2, 3)
    h4_num = count_tag_no_rec('h4', html)
    if h4_num > 0:
        for h4 in range(h4_num):
            draw_heading(x1, y1, x2, y2, 4)
    a_num = count_tag_no_rec('a', html)
    if a_num > 0:
        for a in range(a_num):
            draw_a_tag(x1, y1, x2, y2)


# Draw headings and paragraphs no recursion
def run_draw_h_p_a_s_recursive(x1, y1, x2, y2, html):
    p_num = count_tag('p', html)
    if p_num > 0:
        for p in range(p_num):
            draw_paragraph()
    h1_num = count_tag('h1', html)
    if h1_num > 0:
        for h1 in range(h1_num):
            draw_heading(x1, y1, x2, y2, 1)
    h2_num = count_tag('h2', html)
    if h2_num > 0:
        for h2 in range(h2_num):
            draw_heading(x1, y1, x2, y2, 2)
    h3_num = count_tag('h3', html)
    if h3_num > 0:
        for h3 in range(h3_num):
            draw_heading(x1, y1, x2, y2, 3)
    h4_num = count_tag('h4', html)
    if h4_num > 0:
        for h4 in range(h4_num):
            draw_heading(x1, y1, x2, y2, 4)
    a_num = count_tag('a', html)
    if a_num > 0:
        for a in range(a_num):
            draw_a_tag(x1, y1, x2, y2)


# Draw u_list
def draw_u_list(x1, y1, x2, y2, sub):
    xl = random.randint(x1, x2)
    yl = random.randint(y1, y2)
    hl = random.randint(10, 20)
    for il in range(sub):
        wl = random.randint(10, 20)
        r_color = random.randint(80, 100)
        draw.rectangle([xl, yl, xl + wl, yl - hl], (r - r_color, g - r_color, b - r_color))
        xl = xl + wl


# Run draw u_list
def run_draw_u_list(x1, y1, x2, y2, html):
    ul_num = count_tag_no_rec('ul', html)
    if ul_num > 0:
        ul_next = html.find('ul')
        li_num = count_tag('li', ul_next)
        draw_u_list(x1, y1, x2, y2, li_num)
        run_draw_h_p_a_s_recursive(x1, y1, x2, y2, ul_next)
        for ul in range(ul_num - 1):
            ul_next = ul_next.find_next_sibling('ul')
            if ul_next is None:
                return
            li_num = count_tag('li', ul_next)
            draw_u_list(x1, y1, x2, y2, li_num)
            run_draw_h_p_a_s_recursive(x1, y1, x2, y2, ul_next)


# Draw o_list
def draw_o_list(x1, y1, x2, y2, sub):
    xl = random.randint(x1, x2)
    yl = random.randint(y1, y2)
    hl = random.randint(10, 20)
    for ol in range(sub):
        wl = random.randint(10, 20)
        r_color = random.randint(80, 100)
        draw.rectangle([xl, yl, xl - wl, yl + hl], (r + r_color, g + r_color, b + r_color))
        xl = xl + wl


# Run draw o_list
def run_draw_o_list(x1, y1, x2, y2, html):
    ol_num = count_tag_no_rec('ol', html)
    if ol_num > 0:
        ol_next = html.find('ol')
        li_num = count_tag('li', ol_next)
        draw_u_list(x1, y1, x2, y2, li_num)
        run_draw_h_p_a_s_recursive(x1, y1, x2, y2, ol_next)
        for ol in range(ol_num - 1):
            ol_next = ol_next.find_next_sibling('ol')
            if ol_next is None:
                return
            li_num = count_tag('li', ol_next)
            draw_u_list(x1, y1, x2, y2, li_num)
            run_draw_h_p_a_s_recursive(x1, y1, x2, y2, ol_next)


# Draw table
def draw_table(x1, y1, x2, y2, row, col):
    xt = random.randint(x1, x2)
    yt = random.randint(y1, y2)
    wt = random.randint(40, 50)
    ht = random.randint(5, 20)
    for row in range(row):
        for col in range(col):
            draw.rectangle([xt, yt, xt + wt, yt - ht], (r - 100, g - 100, b - 100))
            yt = yt - ht


# Run table draw function with given html
def run_draw_table(x1, y1, x2, y2, html):
    table_num = count_tag_no_rec('table', html)
    if table_num > 0:
        table_next = html.find('table')
        row = count_tag('tr', table_next)
        col = count_tag('th', table_next)
        draw_table(x1, y1, x2, y2, row, col)
        run_draw_h_p_a_s_recursive(x1, y1, x2, y2, table_next)
        for table in range(table_num - 1):
            table_next = table_next.find_next_sibling('table')
            row = count_tag('tr', table_next)
            col = count_tag('th', table_next)
            draw_table(x1, y1, x2, y2, row, col)
            run_draw_h_p_a_s_recursive(x1, y1, x2, y2, table_next)


# Div grouping function
def div_parsing_helper(x1, y1, x2, y2, html):
    run_draw_h_p_a_s(x1, y1, x2, y2, html)
    run_draw_table(x1, y1, x2, y2, html)
    run_draw_u_list(x1, y1, x2, y2, html)
    run_draw_o_list(x1, y1, x2, y2, html)
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

# Draw elements not in div
run_draw_table(0, 720, 1920, 1080, soup)
run_draw_u_list(0, 720, 1920, 1080, soup)
run_draw_o_list(0, 720, 1920, 1080, soup)
run_draw_h_p_a_s(0, 720, 1920, 1080, soup)

# Draw elements in div
s = soup.find('body')
div_parsing_helper(0, 720, 1920, 1080, s)

# Cleanup
del draw
del soup

# Show image
#im.show()
# Save image
im.save('landscape.jpg')
