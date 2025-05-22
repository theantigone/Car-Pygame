# Quang Hoang
# Personal Python project making a game utilising Pygame
# 5/16/2024
import random
import time

import pygame

pygame.init()  # initialises pygame

crash_sound = pygame.mixer.Sound('../data/external/music/crash.mp3')
pygame.mixer.music.load('../data/external/music/music.mp3')

# window dimensions
display_width = 800
display_height = 600

# RGB colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 255, 255)

dark_red = (200, 0, 0)
dark_green = (0, 200, 0)
dark_blue = (0, 200, 200)

# block_color = (53, 115, 255)
block_color = (102, 51, 0)

# car image dimensions
car_width = 80
car_height = 157

game_display = pygame.display.set_mode((display_width, display_height))  # sets the window dimensions
pygame.display.set_caption('Try Not To Crash!')  # sets the window title
clock = pygame.time.Clock()  # sets the frames per second (fps) of the game

# loads images from directory
car_img = pygame.image.load('../data/external/images/car.png')
game_icon = pygame.image.load('../data/external/images/car_icon.png')
background_img = pygame.image.load('../data/external/images/background.jpg')
instructions_img = pygame.image.load('../data/external/images/instructions_background.jpg')
main_menu_img = pygame.image.load('../data/external/images/main_menu_background.jpg')

pygame.display.set_icon(game_icon)

pause = False

speed_increment = 0
width_increment = 0


# displays a counter for how many objects the car has dodged
def things_dodged(count):
    font = pygame.font.SysFont('gabriola', 25)
    text = font.render("Dodged: " + str(count), True, black)
    game_display.blit(text, (700, 0))


# displays a square (obstacle) falling down from the sky
def things(thing_x, thing_y, thing_width, thing_height, color):
    pygame.draw.rect(game_display, color, [thing_x, thing_y, thing_width, thing_height])


# displays car image
def car(x, y):
    game_display.blit(car_img, (x, y))  # displays car at (x, y) coordinates


# displays the color and antialiasing of text
def text_objects(text, font, color):
    text_surface = font.render(text, True, color)  # renders font
    return text_surface, text_surface.get_rect()


# crashes the game
def crash():
    # stops the background music and queues the game over music
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    # displays crash screen
    large_text = pygame.font.SysFont('gabriola', 100)  # defines the font type and size
    text_surf, text_rect = text_objects('You crashed...', large_text, black)
    text_rect.center = ((display_width / 2), (display_height / 2))  # defines text coordinates
    game_display.blit(text_surf, text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        # displays buttons
        button('Play Again?', 150, 450, 100, 50, dark_green, green, game_loop)
        button('Quit..?', 550, 450, 100, 50, dark_red, red, quit_game)

        pygame.display.update()
        clock.tick(15)


# makes the rectangular buttons in buttons() have rounded edges
def draw_rounded_rect(surface, rect, color, corner_radius):
    # surface: the surface to draw on
    # rect: a pygame.Rect object representing the rectangle to draw
    # color: the color of the rectangle
    # corner_radius: the radius of the corners of the rectangle

    # Draw four circles for the corners
    pygame.draw.ellipse(surface, color, pygame.Rect(rect.left, rect.top, corner_radius * 2, corner_radius * 2))
    pygame.draw.ellipse(surface, color,
                        pygame.Rect(rect.right - corner_radius * 2, rect.top, corner_radius * 2, corner_radius * 2))
    pygame.draw.ellipse(surface, color,
                        pygame.Rect(rect.left, rect.bottom - corner_radius * 2, corner_radius * 2, corner_radius * 2))
    pygame.draw.ellipse(surface, color,
                        pygame.Rect(rect.right - corner_radius * 2, rect.bottom - corner_radius * 2, corner_radius * 2,
                                    corner_radius * 2))

    # Draw two rectangles to fill in the rest
    pygame.draw.rect(surface, color,
                     pygame.Rect(rect.left, rect.top + corner_radius, rect.width, rect.height - corner_radius * 2))
    pygame.draw.rect(surface, color,
                     pygame.Rect(rect.left + corner_radius, rect.top, rect.width - corner_radius * 2, rect.height))


# Helper function to create text inside the rectangle
def create_text_in_button(message, x, y, width, height):
    small_text = pygame.font.SysFont('gabriola', 20)
    text_surf, text_rect = text_objects(message, small_text, black)
    text_rect.center = ((x + (width / 2)), y + (height / 2))
    game_display.blit(text_surf, text_rect)


# displays a button with text and interactive functionality
def button(message, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()  # gets mouse position stored in a tuple (x, y)
    click = pygame.mouse.get_pressed()  # checks whether mouse clicks something, stored in a tuple (x,y,z),
    # where x is left click, y is middle click, z is right click

    # creates a rectangle shape and gets mouse position (mouse[0] is x, mouse[1] is y),
    # and if mouse hovers over the button, turn the rectangle shape into a lighter shade
    if x + width > mouse[0] > x and y + height > mouse[1] > y:  # checks to see if mouse is hovering over coordinates
        # pygame.draw.rect(game_display, active_color, (x, y, width, height))  # displays rectangle in lighter hue
        draw_rounded_rect(game_display, pygame.Rect(x, y, width, height), active_color,
                          10)  # displays button in lighter hue

        # checks for mouse clicks and performs a corresponding action
        if click[0] == 1 and action is not None:  # checks if left click is pressed and action is defined
            time.sleep(0.2)
            action()

    else:
        # pygame.draw.rect(game_display, inactive_color, (x, y, width, height))
        draw_rounded_rect(game_display, pygame.Rect(x, y, width, height), inactive_color, 20)

    # creates text inside the rectangle
    create_text_in_button(message, x, y, width, height)


# un-initialises pygame and exits the window
def quit_game():
    pygame.quit()
    quit()


# unpause function
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


# pause function
def paused():
    # pauses the music
    pygame.mixer.music.pause()

    # displays pause screen
    large_text = pygame.font.SysFont('gabriola', 100)  # defines the font type and size
    text_surf, text_rect = text_objects('Paused', large_text, black)
    text_rect.center = ((display_width / 2), (display_height / 2))  # defines text coordinates
    game_display.blit(text_surf, text_rect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        # displays buttons
        button('Continue?', 150, 450, 100, 50, dark_green, green, unpause)
        button('Quit..?', 550, 450, 100, 50, dark_red, red, quit_game)

        pygame.display.update()
        clock.tick(15)


# faster block game mode
def faster_block():
    global speed_increment
    global width_increment
    speed_increment = 0.5
    width_increment = 0
    game_loop()


# wider block game mode
def wider_block():
    global speed_increment
    global width_increment
    speed_increment = 0
    width_increment = 10
    game_loop()


# game mode menu
def display_game_mode(show_resume_button):
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        game_display.blit(instructions_img, (0, 0))

        # displays game mode header
        large_text = pygame.font.SysFont('gabriola', 75)  # defines the font type and size
        text_surf, text_rect = text_objects('Game Mode', large_text, white)
        text_rect.center = ((display_width / 2), (display_height / 3))  # defines text coordinates
        game_display.blit(text_surf, text_rect)

        small_text = pygame.font.SysFont('gabriola', 20)  # defines the font type and size
        text_surf, text_rect = text_objects('Faster = blocks get progressively faster', small_text, white)
        text_rect.center = ((display_width / 2), (display_height / 2))  # defines text coordinates
        game_display.blit(text_surf, text_rect)

        text_surf, text_rect = text_objects('Wider = blocks get progressively wider', small_text, white)
        text_rect.center = ((display_width / 2), (display_height / 1.8))  # defines text coordinates
        game_display.blit(text_surf, text_rect)

        # displays buttons
        if show_resume_button:
            button('Resume', 350, 450, 100, 50, dark_green, green, unpause)

            small_text = pygame.font.SysFont('gabriola', 20)  # defines the font type and size
            text_surf, text_rect = text_objects('Clicking either game mode will reset your progress.', small_text,
                                                white)
            text_rect.center = ((display_width / 2), (display_height / 1.6))  # defines text coordinates
            game_display.blit(text_surf, text_rect)

        button('Faster blocks', 150, 450, 100, 50, dark_blue, blue, faster_block)
        button('Wider blocks', 550, 450, 100, 50, dark_blue, blue, wider_block)

        pygame.display.update()
        clock.tick(15)


def game_mode():
    global pause
    pause = True
    display_game_mode(False)


def game_mode_menu():
    # pauses the music
    pygame.mixer.music.pause()
    global pause
    pause = True
    display_game_mode(True)


# Helper function to display instructions
def display_instruction(text, y_position, small_text, color):
    text_surf, text_rect = text_objects(text, small_text, color)
    text_rect.center = ((display_width / 2), y_position)
    game_display.blit(text_surf, text_rect)


def display_instructions(show_resume_button):
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        game_display.blit(instructions_img, (0, 0))
        # displays the color and antialiasing of text

        # displays main title
        large_text = pygame.font.SysFont('gabriola', 75)  # defines the font type and size
        text_surf, text_rect = text_objects('Instructions', large_text, white)
        text_rect.center = ((display_width / 2), (display_height / 3))  # defines text coordinates
        game_display.blit(text_surf, text_rect)

        # displays instructions
        small_text = pygame.font.SysFont('gabriola', 20)
        display_instruction('Use left and right arrow keys to move the car; avoid hitting the wall.', (display_height / 2), small_text, white)
        display_instruction('Avoid the brown blocks falling down from the sky.', (display_height / 1.85), small_text,
                            white)
        display_instruction('Press the escape key to pause the game.', (display_height / 1.725), small_text, white)
        display_instruction('Try to survive the longest!', (display_height / 1.6125), small_text, white)

        # displays buttons
        if show_resume_button:
            button('Resume', 350, 450, 100, 50, dark_green, green, unpause)
        else:
            button('GO!', 350, 450, 100, 50, dark_green, green, game_mode)

        pygame.display.update()
        clock.tick(15)


# instructions screen
def instructions():
    global pause
    pause = True
    display_instructions(False)


# instructions from menu bar screen
def instructions_menu():
    # pauses the music
    pygame.mixer.music.pause()
    global pause
    pause = True
    display_instructions(True)


# starting page of the game
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        game_display.blit(main_menu_img, (0, 0))

        # displays main title
        large_text = pygame.font.SysFont('gabriola', 75)  # defines the font type and size
        text_surf, text_rect = text_objects('Try Not To Crash!', large_text, black)
        text_rect.center = ((display_width / 2), (display_height / 4))  # defines text coordinates
        game_display.blit(text_surf, text_rect)

        # displays buttons
        button('Start!', 150, 450, 100, 50, dark_green, green, instructions)
        button('Quit..?', 550, 450, 100, 50, dark_red, red, quit_game)

        pygame.display.update()
        clock.tick(15)


def draw_menu():
    menu_font = pygame.font.SysFont('gabriola', 20)
    menu_items = ['Game Mode', 'Instructions', 'Quit']
    menu_width = 100
    menu_height = 30
    for i, item in enumerate(menu_items):
        pygame.draw.rect(game_display, white, [i * menu_width, 0, menu_width, menu_height])
        text_surf, text_rect = text_objects(item, menu_font, black)
        text_rect.center = ((i * menu_width + menu_width / 2), menu_height / 2)
        game_display.blit(text_surf, text_rect)


def handle_menu_click(pos):
    global pause
    x, y = pos
    if y < 30:  # if click is within the menu bar area
        if 0 <= x < 100:
            pause = True
            game_mode_menu()
        elif 100 <= x < 200:
            pause = True
            instructions_menu()
        elif 200 <= x < 300:
            pygame.quit()
            quit()


def game_loop():
    global pause
    global speed_increment
    global width_increment

    # plays the background music
    pygame.mixer.music.play(-1)

    # sets the car at (x, y) coordinates
    x = (display_width * 0.45)
    y = (display_height * 0.7)

    x_change = 0

    thing_start_x = random.randrange(0, display_width)
    thing_speed = 4
    thing_width = 100
    thing_start_y = -600
    thing_height = 100

    dodged = 0

    # initialises key states (creates a list)
    keys_down = []

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():  # tracks user input such as moving the mouse or clicking
            if event.type == pygame.QUIT:  # checks if user exits the window
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_menu_click(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN:  # checks if key is pressed
                if event.key == pygame.K_LEFT:  # checks if left arrow key is pressed
                    if pygame.K_LEFT not in keys_down:
                        keys_down.append(pygame.K_LEFT)  # adds to the list
                if event.key == pygame.K_RIGHT:  # checks if right arrow key is pressed
                    if pygame.K_RIGHT not in keys_down:
                        keys_down.append(pygame.K_RIGHT)  # adds to the list
                if event.key == pygame.K_ESCAPE:  # checks if escape key is pressed
                    pause = True  # prepares pause function
                    paused()  # pauses the game
                    if pygame.K_LEFT in keys_down:
                        keys_down.remove(pygame.K_LEFT)  # removes from the list
                    if pygame.K_RIGHT in keys_down:
                        keys_down.remove(pygame.K_RIGHT)  # removes from the list

            if event.type == pygame.KEYUP:  # checks if key is released
                if event.key == pygame.K_LEFT:  # checks if left arrow key is released
                    if pygame.K_LEFT in keys_down:
                        keys_down.remove(pygame.K_LEFT)  # removes from the list
                if event.key == pygame.K_RIGHT:  # checks if right arrow key is released
                    if pygame.K_RIGHT in keys_down:
                        keys_down.remove(pygame.K_RIGHT)  # removes from the list

        # determine direction based on key states
        # the index -1 represents the last index of the list
        if keys_down:
            if keys_down[-1] == pygame.K_LEFT:
                x_change = -5
            elif keys_down[-1] == pygame.K_RIGHT:
                x_change = 5
        else:
            x_change = 0

        x += x_change  # changes the location of the car

        game_display.blit(background_img, (0, 0))  # fills the screen with a color

        things(thing_start_x, thing_start_y, thing_width, thing_height, block_color)
        thing_start_y += thing_speed

        car(x, y)  # displays car image

        things_dodged(dodged)  # displays dodge counter

        if x > display_width - car_width or x < 0:
            crash()

        if thing_start_y > display_height:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, display_width)
            dodged += 1
            thing_speed += speed_increment
            thing_width += width_increment

        if y < thing_start_y + thing_height:
            if (thing_start_x < x < thing_start_x + thing_width or thing_start_x < x + car_width < thing_start_x
                    + thing_width):
                crash()

        draw_menu()
        pygame.display.update()  # updates the screen
        clock.tick(60)


game_intro()
game_loop()
quit_game()
