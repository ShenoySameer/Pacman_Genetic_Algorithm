import pygame
import sys
from graph import build_graph
from Ghosts import Ghost
from pacman import Pacman
import math

def main(movelist):

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
        for i in range(14):
            temp_image = sprite_sheet.subsurface(16*i, 0, 16, 16)
            pacman_frame_list.append(pygame.transform.scale(temp_image, (16*multiplier, 16*multiplier)))

        return pacman_frame_list

    number_sprite_list = split_number_sprite(number_sprites)
    pacman_animation_frames = pacman_animation_sheet(pacman_animation_sprites)
    G, pellet_coords = build_graph()
    scaled_pellet = pygame.transform.scale(pellet, (2*multiplier, 2*multiplier))
    blinky = Ghost("Blinky")

    #Ghost timer initialize
    clock = pygame.time.Clock()
    blinky_timer = pygame.USEREVENT +1
    pygame.time.set_timer(blinky_timer, 700)
    blinky_counter = 0
    blinky_alarm = 70
    pinky_counter = 0
    pinky_alarm = 70
    inky_counter = 0
    inky_alarm = 70
    clyde_counter = 0
    clyde_alarm = 70

    p = 1

    InkySpawned = False
    PinkySpawned = False
    ClydeSpawned = False

    my_font = pygame.font.SysFont('Comic Sans MS', 7)
    counter = 0
    delay = 50

    player = Pacman(movelist)


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
            player.alive = False
        if PinkySpawned:
            if pinky.loc == player.location:
                player.alive = False
        if InkySpawned:
            if inky.loc == player.location:
                player.alive = False
        if ClydeSpawned:
            if clyde.loc == player.location:
                player.alive = False

        #blinky moving
        blinky.draw_update(player.location, player.looking, screen, multiplier, G, (255, 0, 0))

        # #pinky moving
        if len(pellet_coords) == 238:
            pinky = Ghost("Pinky")
            PinkySpawned = True
            pinky_timer = pygame.USEREVENT + 2
            pygame.time.set_timer(pinky_timer, 1000)
        if PinkySpawned:
            pinky_counter += 1
            pinky.draw_update(player.location, player.looking, screen, multiplier, G, (255, 192, 203))


        #inky moving
        if len(pellet_coords) == 214:
            inky = Ghost("Inky")
            InkySpawned = True
            inky_timer = pygame.USEREVENT + 3
            pygame.time.set_timer(inky_timer, 700)
        if InkySpawned:
            inky_counter += 1
            inky.draw_update(player.location, player.looking, screen, multiplier, G, (0, 0, 255), blinky.loc)


        #clyde moving
        if len(pellet_coords) == 163:
            clyde = Ghost("Clyde")
            ClydeSpawned = True
            clyde_timer = pygame.USEREVENT + 4
            pygame.time.set_timer(clyde_timer, 700)
        if ClydeSpawned:
            clyde_counter += 1
            clyde.draw_update(player.location, player.looking, screen, multiplier, G,(255, 165, 0))


        #Second Death Tracker
        if blinky.loc == player.location:
            player.alive = False
        if PinkySpawned:
            if pinky.loc == player.location:
                player.alive = False
        if InkySpawned:
            if inky.loc == player.location:
                player.alive = False
        if ClydeSpawned:
            if clyde.loc == player.location:
                player.alive = False

        #player moving
        previous_looking = player.looking
        if len(G[player.location]) > 2:
            player.algomove()

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
            player.algomove()

            if current_move in G:
                player.location = current_move

        if player.location in pellet_coords:
            pellet_coords.remove(player.location)

        #Third Death Tracker
        if blinky.loc == player.location:
            player.alive = False
        if PinkySpawned:
            if pinky.loc == player.location:
                player.alive = False
        if InkySpawned:
            if inky.loc == player.location:
                player.alive = False
        if ClydeSpawned:
            if clyde.loc == player.location:
                player.alive = False

        if player.alive == False:
            #print(f'score {abs(244 - len(pellet_coords))}')
            return 244 - len(pellet_coords) + counter, player.moves_used[::-1][3:]
            #return 244 - len(pellet_coords) + round(counter/2), player.moves_used[::-1][3:]
            #return counter

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

        if delay:
            pygame.time.wait(delay)
        pygame.display.update()

        blinky_counter += 1


        if blinky_counter > blinky_alarm:
                if blinky.mode == "chase":
                    blinky_alarm = 70
                    blinky.mode = "scatter"
                    blinky_counter = 0
                elif blinky.mode == "scatter":
                    blinky_alarm = 200
                    blinky.mode = "chase"
                    blinky_counter = 0

        if PinkySpawned:
                if pinky_counter > pinky_alarm:
                    if pinky.mode == "chase":
                        pinky_alarm = 70
                        pinky.mode = "scatter"
                        pinky_counter = 0
                    elif pinky.mode == "scatter":
                        pinky_alarm = 200
                        pinky.mode = "chase"
                        pinky_counter = 0

        if InkySpawned:
                if inky_counter > inky_alarm:
                    if inky.mode == "chase":
                        inky_alarm = 70
                        inky.mode = "scatter"
                        inky_counter = 0
                    elif inky.mode == "scatter":
                        inky_alarm = 200
                        inky.mode = "chase"
                        inky_counter = 0

        if ClydeSpawned:
                if clyde_counter > clyde_alarm:
                    if clyde.mode == "chase":
                        clyde_alarm = 70
                        clyde.mode = "scatter"
                        clyde_counter = 0
                    elif clyde.mode == "scatter":
                        clyde_alarm = 200
                        clyde.mode = "chase"
                        clyde_counter = 0

        for event in pygame.event.get():
            #quit Game event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)

