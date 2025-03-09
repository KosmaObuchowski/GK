import pygame as pg
import numpy as np

pg.init()
win = pg.display.set_mode((600, 600))
pg.display.set_caption("Zad1")

# kolory
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
purple = (128, 0, 128)
light_blue = (0, 255, 255)
orange = (255, 165, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)
black = (0, 0, 0)
white = (255, 255, 255)
empty = (0, 0, 0, 0)

x = 300
y = 300

radius = 150
size = radius*2
circle_surface = pg.Surface((size, size))
pg.draw.circle(circle_surface, red, (radius, radius), radius)

circle_rect = circle_surface.get_rect(center=(100, 100))

# Function to create a circle surface
def create_circle(size):
    surface = pg.Surface((size, size), pg.SRCALPHA)  # Preserve transparency
    pg.draw.circle(surface, red, (size // 2, size // 2), size // 2)
    return surface

# Function to Shear Surface
def shear_surface(surface, shear_x=0, shear_y=0):
    width, height = surface.get_size()
    array = pg.surfarray.pixels3d(surface)  # Access the surface pixels
    new_array = np.zeros((height + shear_y, width + shear_x, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            # Apply shear transformation
            new_x = x + int(shear_x * (y / height))  # Horizontal shear
            new_y = y + int(shear_y * (x / width))  # Vertical shear
            if 0 <= new_x < width + shear_x and 0 <= new_y < height + shear_y:
                new_array[new_y, new_x] = array[y, x]

    # Create new sheared surface
    sheared_surface = pg.surfarray.make_surface(new_array)
    return sheared_surface


run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        # change on button press
        if event.type == pg.KEYDOWN:
            # reset button
            win.fill(black)
            x = 300
            y = 300
            if event.key == pg.K_r: circle_surface = pg.Surface((size, size))
            if event.key == pg.K_r: pg.draw.circle(circle_surface, red, (radius, radius), radius)

            # scale down x2
            if event.key == pg.K_1:
                nsize = size / 2
                win.fill(black)
                circle_surface = pg.transform.scale(circle_surface, (nsize, nsize))

            # rotate
            if event.key == pg.K_2:
                win.fill(black)
                pg.draw.rect(circle_surface, yellow, (75, 75, 150, 150))
                circle_surface = pg.transform.rotate(circle_surface, 45)


            # flip and stretch
            if event.key == pg.K_3:
                win.fill(black)
                circle_surface = pg.transform.rotate(circle_surface, 90)
                circle_surface = pg.transform.scale(circle_surface, (size, size*1.5))

            # skew
            if event.key == pg.K_4:
                win.fill(black)
                circle_surface = create_circle(size)
                sheared_surface = shear_surface(circle_surface, shear_x=30)
                circle_surface = sheared_surface

            # move to the top and stretch
            if event.key == pg.K_5:
                win.fill(black)
                circle_surface = pg.transform.scale(circle_surface, (size, size / 2))
                y -= 225

            # skew and rotate
            if event.key == pg.K_6:
                win.fill(black)
                circle_surface = create_circle(size)
                sheared_surface = shear_surface(circle_surface, shear_y=30)
                circle_surface = sheared_surface
                circle_surface = pg.transform.rotate(circle_surface, 90)
                circle_surface = pg.transform.scale(circle_surface, (size, size * 1.5))

            # flip and stretch
            if event.key == pg.K_7:
                win.fill(black)
                pg.draw.polygon(circle_surface, yellow, ((150, 200), (250, 250), (50, 250)))
                circle_surface = pg.transform.rotate(circle_surface, 180)
                circle_surface = pg.transform.scale(circle_surface, (size / 3, size / 2))

            # move, stretch and rotate
            if event.key == pg.K_8:
                win.fill(black)
                circle_surface = pg.transform.scale(circle_surface, (size/2, size))
                circle_surface = pg.transform.rotate(circle_surface, 60)
                x -= 50
                y += 150

            # skew, move and flip
            if event.key == pg.K_9:
                win.fill(black)
                circle_surface = create_circle(size)
                sheared_surface = shear_surface(circle_surface, shear_x=50)
                circle_surface = sheared_surface
                circle_surface = pg.transform.rotate(circle_surface, 90)
                x += 150

            # ex 2
            if event.key == pg.K_0:
                win.fill(white)
                circle_surface.fill(white)
                pg.draw.circle(circle_surface, black, (radius, radius), radius)
                pg.draw.rect(circle_surface, yellow, (75,75,150,150))

    rect = circle_surface.get_rect(center=(x, y))
    win.blit(circle_surface, rect.topleft)



    # linia pozioma
    #pygame.draw.line(win, NIEBIESKI, (10, 325), (110, 325), 15)
    # linia pionowa
    #pygame.draw.line(win, SZARY, (210, 275), (210, 375), 5)
    # rysowanie plusa
    #pygame.draw.line(win, NIEBIESKI, (310, 325), (410, 325), 10)
    #pygame.draw.line(win, SZARY, (360, 275), (360, 375), 10)
    # wypisywanie tekstu
    #font = pygame.font.SysFont('comicsans', 30)
    #label = font.render('Tekst do wyświetlania ', 1, (255, 255, 255))
    #win.blit(label, (100, 425))

    pg.display.update()
pg.quit()
