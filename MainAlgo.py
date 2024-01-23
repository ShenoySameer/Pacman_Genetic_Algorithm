import sys
from graph import build_graph
from Ghosts import Ghost
from pacman import Pacman
import math

def main(movelist):

    G, pellet_coords = build_graph()
    blinky = Ghost("Blinky")

    #Ghost timer initialize
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

    counter = 0
    delay = 0

    player = Pacman(movelist)


    while True:

        counter += 1

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
        blinky.draw_update_nv(player.location, player.looking, G)

        # #pinky moving
        if len(pellet_coords) == 238:
            pinky = Ghost("Pinky")
            PinkySpawned = True
        if PinkySpawned:
            pinky_counter += 1
            pinky.draw_update_nv(player.location, player.looking, G)


        #inky moving
        if len(pellet_coords) == 214:
            inky = Ghost("Inky")
            InkySpawned = True
        if InkySpawned:
            inky_counter += 1
            inky.draw_update_nv(player.location, player.looking, G, blinky.loc)


        #clyde moving
        if len(pellet_coords) == 163:
            clyde = Ghost("Clyde")
            ClydeSpawned = True
        if ClydeSpawned:
            clyde_counter += 1
            clyde.draw_update_nv(player.location, player.looking, G)


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


