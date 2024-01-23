import math
import pygame

G = {(0, 0): [(1, 0), (0, 1)], (0, 1): [(0, 0), (0, 2)], (0, 2): [(0, 1), (0, 3)], (0, 3): [(0, 2), (0, 4)], (0, 4): [(1, 4), (0, 3), (0, 5)], (0, 5): [(0, 4), (0, 6)], (0, 6): [(0, 5), (0, 7)], (0, 7): [(1, 7), (0, 6)], (0, 19): [(1, 19), (0, 20)], (0, 20): [(0, 19), (0, 21)], (0, 21): [(0, 20), (0, 22)], (0, 22): [(1, 22), (0, 21)], (0, 25): [(1, 25), (0, 26)], (0, 26): [(0, 25), (0, 27)], (0, 27): [(0, 26), (0, 28)], (0, 28): [(1, 28), (0, 27)], (1, 0): [(0, 0), (2, 0)], (1, 4): [(0, 4), (2, 4)], (1, 7): [(0, 7), (2, 7)], (1, 19): [(0, 19), (2, 19)], (1, 22): [(0, 22), (2, 22)], (1, 25): [(0, 25), (2, 25)], (1, 28): [(0, 28), (2, 28)], (2, 0): [(1, 0), (3, 0)], (2, 4): [(1, 4), (3, 4)], (2, 7): [(1, 7), (3, 7)], (2, 19): [(1, 19), (3, 19)], (2, 22): [(1, 22), (2, 23)], (2, 23): [(2, 22), (2, 24)], (2, 24): [(2, 23), (2, 25)], (2, 25): [(1, 25), (3, 25), (2, 24)], (2, 28): [(1, 28), (3, 28)], (3, 0): [(2, 0), (4, 0)], (3, 4): [(2, 4), (4, 4)], (3, 7): [(2, 7), (4, 7)], (3, 19): [(2, 19), (4, 19)], (3, 25): [(2, 25), (4, 25)], (3, 28): [(2, 28), (4, 28)], (4, 0): [(3, 0), (5, 0)], (4, 4): [(3, 4), (5, 4)], (4, 7): [(3, 7), (5, 7)], (4, 19): [(3, 19), (5, 19)], (4, 25): [(3, 25), (5, 25)], (4, 28): [(3, 28), (5, 28)], (5, 0): [(4, 0), (6, 0), (5, 1)], (5, 1): [(5, 0), (5, 2)], (5, 2): [(5, 1), (5, 3)], (5, 3): [(5, 2), (5, 4)], (5, 4): [(4, 4), (6, 4), (5, 3), (5, 5)], (5, 5): [(5, 4), (5, 6)], (5, 6): [(5, 5), (5, 7)], (5, 7): [(4, 7), (5, 6), (5, 8)], (5, 8): [(5, 7), (5, 9)], (5, 9): [(5, 8), (5, 10)], (5, 10): [(5, 9), (5, 11)], (5, 11): [(5, 10), (5, 12)], (5, 12): [(5, 11), (5, 13)], (5, 13): [(5, 12), (5, 14)], (5, 14): [(5, 13), (5, 15)], (5, 15): [(5, 14), (5, 16)], (5, 16): [(5, 15), (5, 17)], (5, 17): [(5, 16), (5, 18)], (5, 18): [(5, 17), (5, 19)], (5, 19): [(4, 19), (6, 19), (5, 18), (5, 20)], (5, 20): [(5, 19), (5, 21)], (5, 21): [(5, 20), (5, 22)], (5, 22): [(6, 22), (5, 21), (5, 23)], (5, 23): [(5, 22), (5, 24)], (5, 24): [(5, 23), (5, 25)], (5, 25): [(4, 25), (5, 24)], (5, 28): [(4, 28), (6, 28)], (6, 0): [(5, 0), (7, 0)], (6, 4): [(5, 4), (7, 4)], (6, 19): [(5, 19), (7, 19)], (6, 22): [(5, 22), (7, 22)], (6, 28): [(5, 28), (7, 28)], (7, 0): [(6, 0), (8, 0)], (7, 4): [(6, 4), (8, 4)], (7, 19): [(6, 19), (8, 19)], (7, 22): [(6, 22), (8, 22)], (7, 28): [(6, 28), (8, 28)], (8, 0): [(7, 0), (9, 0)], (8, 4): [(7, 4), (9, 4), (8, 5)], (8, 5): [(8, 4), (8, 6)], (8, 6): [(8, 5), (8, 7)], (8, 7): [(9, 7), (8, 6)], (8, 19): [(7, 19), (9, 19)], (8, 22): [(7, 22), (9, 22), (8, 23)], (8, 23): [(8, 22), (8, 24)], (8, 24): [(8, 23), (8, 25)], (8, 25): [(9, 25), (8, 24)], (8, 28): [(7, 28), (9, 28)], (9, 0): [(8, 0), (10, 0)], (9, 4): [(8, 4), (10, 4)], (9, 7): [(8, 7), (10, 7)], (9, 19): [(8, 19), (10, 19)], (9, 22): [(8, 22), (10, 22)], (9, 25): [(8, 25), (10, 25)], (9, 28): [(8, 28), (10, 28)], (10, 0): [(9, 0), (11, 0)], (10, 4): [(9, 4), (11, 4)], (10, 7): [(9, 7), (11, 7)], (10, 19): [(9, 19), (11, 19)], (10, 22): [(9, 22), (11, 22)], (10, 25): [(9, 25), (11, 25)], (10, 28): [(9, 28), (11, 28)], (11, 0): [(10, 0), (11, 1)], (11, 1): [(11, 0), (11, 2)], (11, 2): [(11, 1), (11, 3)], (11, 3): [(11, 2), (11, 4)], (11, 4): [(10, 4), (12, 4), (11, 3)], (11, 7): [(10, 7)], (11, 19): [(10, 19), (11, 20)], (11, 20): [(11, 19), (11, 21)], (11, 21): [(11, 20), (11, 22)], (11, 22): [(10, 22), (11, 21)], (11, 25): [(10, 25), (11, 26)], (11, 26): [(11, 25), (11, 27)], (11, 27): [(11, 26), (11, 28)], (11, 28): [(10, 28), (12, 28), (11, 27)], (12, 4): [(11, 4), (13, 4)], (12, 28): [(11, 28), (13, 28)], (13, 4): [(12, 4), (14, 4)], (13, 28): [(12, 28), (14, 28)], (14, 0): [(15, 0), (14, 1)], (14, 1): [(14, 0), (14, 2)], (14, 2): [(14, 1), (14, 3)], (14, 3): [(14, 2), (14, 4)], (14, 4): [(13, 4), (15, 4), (14, 3)], (14, 7): [(15, 7)], (14, 19): [(15, 19), (14, 20)], (14, 20): [(14, 19), (14, 21)], (14, 21): [(14, 20), (14, 22)], (14, 22): [(15, 22), (14, 21)], (14, 25): [(15, 25), (14, 26)], (14, 26): [(14, 25), (14, 27)], (14, 27): [(14, 26), (14, 28)], (14, 28): [(13, 28), (15, 28), (14, 27)], (15, 0): [(14, 0), (16, 0)], (15, 4): [(14, 4), (16, 4)], (15, 7): [(14, 7), (16, 7)], (15, 19): [(14, 19), (16, 19)], (15, 22): [(14, 22), (16, 22)], (15, 25): [(14, 25), (16, 25)], (15, 28): [(14, 28), (16, 28)], (16, 0): [(15, 0), (17, 0)], (16, 4): [(15, 4), (17, 4)], (16, 7): [(15, 7), (17, 7)], (16, 19): [(15, 19), (17, 19)], (16, 22): [(15, 22), (17, 22)], (16, 25): [(15, 25), (17, 25)], (16, 28): [(15, 28), (17, 28)], (17, 0): [(16, 0), (18, 0)], (17, 4): [(16, 4), (18, 4), (17, 5)], (17, 5): [(17, 4), (17, 6)], (17, 6): [(17, 5), (17, 7)], (17, 7): [(16, 7), (17, 6)], (17, 19): [(16, 19), (18, 19)], (17, 22): [(16, 22), (18, 22), (17, 23)], (17, 23): [(17, 22), (17, 24)], (17, 24): [(17, 23), (17, 25)], (17, 25): [(16, 25), (17, 24)], (17, 28): [(16, 28), (18, 28)], (18, 0): [(17, 0), (19, 0)], (18, 4): [(17, 4), (19, 4)], (18, 19): [(17, 19), (19, 19)], (18, 22): [(17, 22), (19, 22)], (18, 28): [(17, 28), (19, 28)], (19, 0): [(18, 0), (20, 0)], (19, 4): [(18, 4), (20, 4)], (19, 19): [(18, 19), (20, 19)], (19, 22): [(18, 22), (20, 22)], (19, 28): [(18, 28), (20, 28)], (20, 0): [(19, 0), (21, 0), (20, 1)], (20, 1): [(20, 0), (20, 2)], (20, 2): [(20, 1), (20, 3)], (20, 3): [(20, 2), (20, 4)], (20, 4): [(19, 4), (21, 4), (20, 3), (20, 5)], (20, 5): [(20, 4), (20, 6)], (20, 6): [(20, 5), (20, 7)], (20, 7): [(21, 7), (20, 6), (20, 8)], (20, 8): [(20, 7), (20, 9)], (20, 9): [(20, 8), (20, 10)], (20, 10): [(20, 9), (20, 11)], (20, 11): [(20, 10), (20, 12)], (20, 12): [(20, 11), (20, 13)], (20, 13): [(20, 12), (20, 14)], (20, 14): [(20, 13), (20, 15)], (20, 15): [(20, 14), (20, 16)], (20, 16): [(20, 15), (20, 17)], (20, 17): [(20, 16), (20, 18)], (20, 18): [(20, 17), (20, 19)], (20, 19): [(19, 19), (21, 19), (20, 18), (20, 20)], (20, 20): [(20, 19), (20, 21)], (20, 21): [(20, 20), (20, 22)], (20, 22): [(19, 22), (20, 21), (20, 23)], (20, 23): [(20, 22), (20, 24)], (20, 24): [(20, 23), (20, 25)], (20, 25): [(21, 25), (20, 24)], (20, 28): [(19, 28), (21, 28)], (21, 0): [(20, 0), (22, 0)], (21, 4): [(20, 4), (22, 4)], (21, 7): [(20, 7), (22, 7)], (21, 19): [(20, 19), (22, 19)], (21, 25): [(20, 25), (22, 25)], (21, 28): [(20, 28), (22, 28)], (22, 0): [(21, 0), (23, 0)], (22, 4): [(21, 4), (23, 4)], (22, 7): [(21, 7), (23, 7)], (22, 19): [(21, 19), (23, 19)], (22, 25): [(21, 25), (23, 25)], (22, 28): [(21, 28), (23, 28)], (23, 0): [(22, 0), (24, 0)], (23, 4): [(22, 4), (24, 4)], (23, 7): [(22, 7), (24, 7)], (23, 19): [(22, 19), (24, 19)], (23, 22): [(24, 22), (23, 23)], (23, 23): [(23, 22), (23, 24)], (23, 24): [(23, 23), (23, 25)], (23, 25): [(22, 25), (24, 25), (23, 24)], (23, 28): [(22, 28), (24, 28)], (24, 0): [(23, 0), (25, 0)], (24, 4): [(23, 4), (25, 4)], (24, 7): [(23, 7), (25, 7)], (24, 19): [(23, 19), (25, 19)], (24, 22): [(23, 22), (25, 22)], (24, 25): [(23, 25), (25, 25)], (24, 28): [(23, 28), (25, 28)], (25, 0): [(24, 0), (25, 1)], (25, 1): [(25, 0), (25, 2)], (25, 2): [(25, 1), (25, 3)], (25, 3): [(25, 2), (25, 4)], (25, 4): [(24, 4), (25, 3), (25, 5)], (25, 5): [(25, 4), (25, 6)], (25, 6): [(25, 5), (25, 7)], (25, 7): [(24, 7), (25, 6)], (25, 19): [(24, 19), (25, 20)], (25, 20): [(25, 19), (25, 21)], (25, 21): [(25, 20), (25, 22)], (25, 22): [(24, 22), (25, 21)], (25, 25): [(24, 25), (25, 26)], (25, 26): [(25, 25), (25, 27)], (25, 27): [(25, 26), (25, 28)], (25, 28): [(24, 28), (25, 27)]}
class Ghost():
    def __init__(self, name):
        self.loc = (12, 10)
        self.name = name
        self.mode = "scatter"
        self.looking = "left"
        self.scatter_loc2 = False

    def move(self, pacman_loc, blinky_loc, G, player_looking):

        if self.mode == "scatter":
            if self.name == "Clyde":
                pacman_loc = (0, 28)
            if self.name == "Pinky":
                pacman_loc = (0, 0)
            if self.name == "Blinky":
                pacman_loc = (25, 0)
            if self.name == "Inky":
                pacman_loc = (25, 28)

        E = []

        gh_dict = {}
        for node in G:
            gh_dict[node] = [float('-inf'), float('-inf')]

        #Ghost cannot switch directions
        start_loc = self.loc
        start_path = [self.loc]
        while start_loc in G.keys():
            if len(G[start_loc]) > 2:
                start_loc = (start_loc[0] + 1, start_loc[1])
                start_path.append(start_loc)
                break
            if self.looking == "right":
                start_loc = (start_loc[0] + 1, start_loc[1])
            elif self.looking == "left":
                start_loc = (start_loc[0] - 1, start_loc[1])
            elif self.looking == "up":
                start_loc = (start_loc[0], start_loc[1] - 1)
            elif self.looking == "down":
                start_loc = (start_loc[0], start_loc[1] + 1)
            start_path.append(start_loc)


        if len(start_path) == 2:
            start_loc = self.loc
            start_path = []
        else:
            start_loc = start_path[-2]


        #if Pinky
        if self.name == "Pinky" and self.mode == "chase":
            pacman_loc = self.pinky_target(player_looking, pacman_loc, G)

        if self.name == "Inky" and self.mode == "chase":
            pacman_loc = self.inky_target(player_looking, pacman_loc, G, blinky_loc)

        #set up for forloop
        gh_dict[start_loc][1] = abs(start_loc[0] - pacman_loc[0]) + abs(start_loc[1] - pacman_loc[1])
        gh_dict[start_loc][0] = 0

        E.append(start_loc)

        queue = [start_loc]

        path_dict = {start_loc: [start_loc]}


        #While loop
        while len(queue) > 0 and pacman_loc not in E:
            current_node = queue.pop()
            current_g = gh_dict[current_node][0]

            for node in G[current_node]:
                addNode = False

                if node not in E:
                    addNode = True

                if addNode:
                    queue.append(node)
                    E.append(node)
                    path_dict[node] = path_dict[current_node][:] + [node]

                    gh_dict[node][1] = abs(node[0] - pacman_loc[0]) + abs(node[1] - pacman_loc[1])
                    gh_dict[node][0] = current_g + 1

            queue = self.blinky_path(queue, gh_dict)

        if self.name == "Clyde":
            if len(path_dict[pacman_loc]) < 9 and path_dict[pacman_loc][-1] != (0, 28):
                return self.move((0, 28), blinky_loc, G, player_looking)

        return start_path[:-1] + path_dict[pacman_loc]

    def blinky_path(self, unsorted_list, gh_dict):
        temp_list = []

        for node in unsorted_list:
            gh = gh_dict[node][0] + gh_dict[node][1]
            h = gh_dict[node][1]

            temp_list.append((gh, h, node))

        temp_list.sort(reverse = True)

        sorted_list = []

        for node in temp_list:
            sorted_list.append(node[-1])

        return sorted_list

    def pinky_target(self, player_looking, pacman_loc, G):

        if player_looking == "right":
            pacman_loc = (pacman_loc[0] + 4, pacman_loc[1])
            while pacman_loc not in G:
                pacman_loc = (pacman_loc[0] - 1, pacman_loc[1])
        elif player_looking == "left":
            pacman_loc = (pacman_loc[0] - 4, pacman_loc[1])
            while pacman_loc not in G:
                pacman_loc = (pacman_loc[0] + 1, pacman_loc[1])
        elif player_looking == "up":
            pacman_loc = (pacman_loc[0], pacman_loc[1]-4)
            while pacman_loc not in G:
                pacman_loc = (pacman_loc[0], pacman_loc[1]+1)
        elif player_looking == "up":
            pacman_loc = (pacman_loc[0], pacman_loc[1]+4)
            while pacman_loc not in G:
                pacman_loc = (pacman_loc[0], pacman_loc[1]-1)

        return pacman_loc

    def inky_target(self, player_looking, pacman_loc, G, blinky_loc):
        pacman_loc = self.pinky_target(player_looking, pacman_loc, G)

        temp_pacman_loc = (pacman_loc[0] + round((pacman_loc[0] - blinky_loc[0])), pacman_loc[1] + round((pacman_loc[1] - blinky_loc[1])))

        new_pacman_loc = temp_pacman_loc

        counter = 0


        while new_pacman_loc not in G and counter < 8:
            if counter == 0:
                new_pacman_loc = (temp_pacman_loc[0]+1, temp_pacman_loc[1])
            elif counter == 1:
                new_pacman_loc = (temp_pacman_loc[0]-1, temp_pacman_loc[1])
            elif counter == 2:
                new_pacman_loc = (temp_pacman_loc[0], temp_pacman_loc[1]-1)
            elif counter == 3:
                new_pacman_loc = (temp_pacman_loc[0], temp_pacman_loc[1]+1)
            elif counter == 4:
                new_pacman_loc = (temp_pacman_loc[0]+2, temp_pacman_loc[1])
            elif counter == 5:
                new_pacman_loc = (temp_pacman_loc[0]-2, temp_pacman_loc[1])
            elif counter == 6:
                new_pacman_loc = (temp_pacman_loc[0], temp_pacman_loc[1]-2)
            elif counter == 7:
                new_pacman_loc = (temp_pacman_loc[0], temp_pacman_loc[1]+2)
            counter += 1

        if new_pacman_loc[0] < 0 or new_pacman_loc[1] < 0 or new_pacman_loc[0] > 25 or new_pacman_loc[1] > 28 or new_pacman_loc not in G:
            distance_list = []

            top_left = math.dist(new_pacman_loc, (0,0))
            distance_list.append((top_left, (0,0)))
            top_right = math.dist(new_pacman_loc, (25,0))
            distance_list.append((top_right, (25,0)))
            bottom_left = math.dist(new_pacman_loc, (0,28))
            distance_list.append((bottom_left, (0,28)))
            bottom_right = math.dist(new_pacman_loc, (25,28))
            distance_list.append((bottom_right, (25, 28)))

            distance_list.sort()

            new_pacman_loc = distance_list[0][1]

        return new_pacman_loc

    def facing_direction(self, next_node):
        coord_dif = (next_node[0] - self.loc[0], next_node[1] - self.loc[1])
        if coord_dif == (1, 0):
            self.looking = "right"
        elif coord_dif == (-1, 0):
            self.looking = "left"
        elif coord_dif == (0, 1):
            self.looking = "down"
        elif coord_dif == (0, -1):
            self.looking = "up"

    def draw_update(self, player_loc, player_looking, screen, multiplier, G, color, blinky_loc=(0,0)):
        path = self.move(player_loc, blinky_loc, G, player_looking)

        if len(path) > 1:
            self.facing_direction(path[1])
            self.loc = path[1]

        # for node in path:
        #     pygame.draw.rect(screen, color, pygame.Rect(node[0]*multiplier*8 + 35, node[1]*multiplier*8+87, 20, 20))

        pygame.draw.rect(screen, color, pygame.Rect(self.loc[0]*multiplier*8 + 35, self.loc[1]*multiplier*8+87, 20, 20))

    def draw_update_nv(self, player_loc, player_looking, G, blinky_loc=(0,0)):
        path = self.move(player_loc, blinky_loc, G, player_looking)

        if len(path) > 1:
            self.facing_direction(path[1])
            self.loc = path[1]
