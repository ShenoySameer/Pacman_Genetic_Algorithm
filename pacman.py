import pygame

class Pacman():
    def __init__(self, movelist):
        self.looking = "right"
        self.location = (12,22)
        self.movelist = movelist
        self.alive = True
        self.move_counter = 0
        self.moves_used = []

    def move(self):
        key = pygame.key.get_pressed()

        if  key[pygame.K_w]:
            self.looking = "up"
        elif  key[pygame.K_a]:
            self.looking = "left"
        elif  key[pygame.K_s]:
            self.looking = "down"
        elif  key[pygame.K_d]:
            self.looking = "right"

    def algomove(self):
        if len(self.movelist) != 0:
            # current_move = self.movelist[self.move_counter]
            # self.move_counter += 1
            current_move = self.movelist.pop()
            self.moves_used.append(current_move)
            self.looking = current_move
        else:
            self.alive = False


