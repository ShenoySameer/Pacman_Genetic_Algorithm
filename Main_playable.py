import pygame
import sys
from graph import build_graph
from Ghosts import Ghost
from pacman import Pacman

pygame.init()
pygame.font.init()

#sprite dimensions
multiplier = 3
bg_dimensions = (224 * multiplier, 248 * multiplier)
hs_text_dimensions = (73 * multiplier, 7 * multiplier)
_1up_text_dimensions = (22 * multiplier, 7 * multiplier)
sc_width = 224 * multiplier
sc_height = 248 * multiplier + 100

#pygame screen
screen = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Pac Man")

#load images
bg_image = pygame.image.load("Assets/pacman_map.png").convert_alpha()
hs_text_image = pygame.image.load("Assets/pacman_HIGH_SCORE.png").convert_alpha()
_1up_text_image = pygame.image.load("Assets/pacman_1up_text.png").convert_alpha()
number_sprites = pygame.image.load("Assets/pacman_numbers.png").convert_alpha()
pellet = pygame.image.load("Assets/pacman_pellet.png").convert_alpha()
pacman_animation_sprites = pygame.image.load("Assets/pacman_animation.png").convert_alpha()

def draw_bg():
    #blits the background
    scaled_bg = pygame.transform.scale(bg_image, bg_dimensions)
    screen.blit(scaled_bg, (0, 55))

def draw_score_board():
    scaled_hs_text = pygame.transform.scale(hs_text_image, hs_text_dimensions)
    screen.blit(scaled_hs_text, ((sc_width- hs_text_dimensions[0])/2, 0))

    scaled_1up_text = pygame.transform.scale(_1up_text_image, _1up_text_dimensions)
    screen.blit(scaled_1up_text, ((sc_width- _1up_text_dimensions[0])/4 - _1up_text_dimensions[0], 0))

def split_number_sprite(sprite_sheet):
    number_image_list = []
    print(sprite_sheet)
    for i in range(0, 10):
        temp_image = sprite_sheet.subsurface(8*i, 0, 8, 7)
        number_image_list.append(pygame.transform.scale(temp_image, (8*multiplier, 7*multiplier)))

    return number_image_list

def number_to_image(number, number_image_list, highscore):
    #score_board False = 1up, True = highscore

    right = 0
    if highscore:
        right += 200

    counter = 0
    starting_position = 280 - (8 * len([*str(number)]))/2 + 8 + right
    for n in str(number):
        screen.blit(number_image_list[int(n)], (starting_position + counter * 8 * multiplier, 25))
        counter += 1

def pacman_animation_sheet(sprite_sheet):
    pacman_frame_list = []
    print(sprite_sheet)
    for i in range(14):
        temp_image = sprite_sheet.subsurface(16*i, 0, 16, 16)
        pacman_frame_list.append(pygame.transform.scale(temp_image, (16*multiplier, 16*multiplier)))

    return pacman_frame_list


number_sprite_list = split_number_sprite(number_sprites)
pacman_animation_frames = pacman_animation_sheet(pacman_animation_sprites)
G, pellet_coords = build_graph()
scaled_pellet = pygame.transform.scale(pellet, (2*multiplier, 2*multiplier))

#make player and ghost objects
player = Pacman("")
blinky = Ghost("Blinky")


clyde = Ghost("Clyde")

#Ghost timer initialize
clock = pygame.time.Clock()
blinky_timer = pygame.USEREVENT +1
pygame.time.set_timer(blinky_timer, 7000)

def main():
    InkySpawned = False
    PinkySpawned = False
    ClydeSpawned = False

    counter = 0
    delay = 75

    while True:
        screen.fill((0,0,0))
        draw_bg()
        draw_score_board()

        counter += 1

        for i, node in enumerate(pellet_coords):
            # text_surface = my_font.render(str(node), False, (255, 255, 255))
            # screen.blit(text_surface, (node[0]*multiplier*8 + 35, node[1]*multiplier*8+87))
            #
            # screen.blit(number_sprite_list[i % 10], (node[0]*multiplier*8 + 35, node[1]*multiplier*8+87))

            screen.blit(scaled_pellet, (node[0]*multiplier*8 + 35, node[1]*multiplier*8+87))

        #First Death Tracker
        if blinky.loc == player.location:
            pygame.quit()
            sys.exit()
        if PinkySpawned:
            if pinky.loc == player.location:
                pygame.quit()
                sys.exit()
        if InkySpawned:
            if inky.loc == player.location:
                pygame.quit()
                sys.exit()
        if ClydeSpawned:
            if clyde.loc == player.location:
                pygame.quit()
                sys.exit()

        #blinky moving
        blinky.draw_update(player.location, player.looking, screen, multiplier, G, (255, 0, 0))

        # #pinky moving
        if len(pellet_coords) == 238:
            pinky = Ghost("Pinky")
            PinkySpawned = True
            pinky_timer = pygame.USEREVENT + 2
            pygame.time.set_timer(pinky_timer, 10000)
        if PinkySpawned:
            pinky.draw_update(player.location, player.looking, screen, multiplier, G, (255, 192, 203))


        #inky moving
        if len(pellet_coords) == 214:
            inky = Ghost("Inky")
            InkySpawned = True
            inky_timer = pygame.USEREVENT + 3
            pygame.time.set_timer(inky_timer, 7000)
        if InkySpawned:
            inky.draw_update(player.location, player.looking, screen, multiplier, G, (0, 0, 255), blinky.loc)


        #clyde moving
        if len(pellet_coords) == 163:
            clyde = Ghost("Clyde")
            ClydeSpawned = True
            clyde_timer = pygame.USEREVENT + 4
            pygame.time.set_timer(clyde_timer, 7000)
        if ClydeSpawned:
            clyde.draw_update(player.location, player.looking, screen, multiplier, G,(255, 165, 0))


        #Second Death Tracker
        if blinky.loc == player.location:
            pygame.quit()
            sys.exit()
        if PinkySpawned:
            if pinky.loc == player.location:
                pygame.quit()
                sys.exit()
        if InkySpawned:
            if inky.loc == player.location:
                pygame.quit()
                sys.exit()
        if ClydeSpawned:
            if clyde.loc == player.location:
                pygame.quit()
                sys.exit()

        #player moving
        previous_looking = player.looking
        player.move()

        if player.looking == "up":
            current_move = (player.location[0], player.location[1] - 1)
        elif player.looking == "left":
            current_move = (player.location[0] - 1, player.location[1])
        elif player.looking == "down":
            current_move = (player.location[0], player.location[1] + 1)
        elif player.looking == "right":
            current_move = (player.location[0] + 1, player.location[1])

        if current_move in G:
            player.location = current_move
        else:
            player.looking = previous_looking
            if player.looking == "up":
                current_move = (player.location[0], player.location[1] - 1)
            elif player.looking == "left":
                current_move = (player.location[0] - 1, player.location[1])
            elif player.looking == "down":
                current_move = (player.location[0], player.location[1] + 1)
            elif player.looking == "right":
                current_move = (player.location[0] + 1, player.location[1])

            if current_move in G:
                player.location = current_move

        if player.location in pellet_coords:
            pellet_coords.remove(player.location)

        #Third Death Tracker
        if blinky.loc == player.location:
            pygame.quit()
            sys.exit()
        if PinkySpawned:
            if pinky.loc == player.location:
                pygame.quit()
                sys.exit()
        if InkySpawned:
            if inky.loc == player.location:
                pygame.quit()
                sys.exit()
        if ClydeSpawned:
            if clyde.loc == player.location:
                pygame.quit()
                sys.exit()

        #draw player
        if player.looking == 'right':
            current_pacman_frame = pacman_animation_frames[counter % 3]
        if player.looking == "left":
            current_pacman_frame = pygame.transform.rotate(pacman_animation_frames[counter % 3], 180)
        if player.looking == "up":
            current_pacman_frame = pygame.transform.rotate(pacman_animation_frames[counter % 3], 90)
        if player.looking == "down":
            current_pacman_frame = pygame.transform.rotate(pacman_animation_frames[counter % 3], 270)

        screen.blit(current_pacman_frame, (player.location[0]*multiplier*8 + 14, player.location[1]*multiplier*8+70))

        #score board
        number_to_image(abs(244 - len(pellet_coords)), number_sprite_list, False)


        pygame.time.wait(delay)
        pygame.display.update()


        for event in pygame.event.get():

            #Ghost mode timer
            if event.type == blinky_timer:
                if blinky.mode == "chase":
                    pygame.time.set_timer(blinky_timer, 7000)
                    blinky.mode = "scatter"
                elif blinky.mode == "scatter":
                    pygame.time.set_timer(blinky_timer, 20000)
                    blinky.mode = "chase"

            if PinkySpawned:
                if event.type == pinky_timer:
                    if pinky.mode == "chase":
                        pygame.time.set_timer(pinky_timer, 7000)
                        pinky.mode = "scatter"
                    elif pinky.mode == "scatter":
                        pygame.time.set_timer(pinky_timer, 20000)
                        pinky.mode = "chase"

            if InkySpawned:
                if event.type == inky_timer:
                    if inky.mode == "chase":
                        pygame.time.set_timer(inky_timer, 7000)
                        inky.mode = "scatter"
                    elif inky.mode == "scatter":
                        pygame.time.set_timer(inky_timer, 20000)
                        inky.mode = "chase"

            if ClydeSpawned:
                if event.type == clyde_timer:
                    if clyde.mode == "chase":
                        pygame.time.set_timer(clyde_timer, 7000)
                        clyde.mode = "scatter"
                    elif clyde.mode == "scatter":
                        pygame.time.set_timer(clyde_timer, 20000)
                        clyde.mode = "chase"



            #quit Game event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)

main()
