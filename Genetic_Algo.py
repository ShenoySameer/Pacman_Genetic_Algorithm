from MainAlgoVisual import main
import numpy
import random

num_players = 30
GENERATIONS = 50000
mutation_rate = 0.1

def random_move():
    return [random.choice(['up', 'down', 'left', 'right']) for _ in range(10000)]


# Function for genetic mutation
def mutate(strategy):
    mutation_rate = 0.1
    for i in range(len(strategy)):
        if random.random() < mutation_rate:
            strategy[i] = random.choice(['up', 'down', 'left', 'right'])
            if mutation_rate < 0.5:
                mutation_rate += 0.05

    return strategy


def genetic_algorithm():
    imp_counter = 1
    fail_counter = 0

    #move saves
    #227 generations ['right', 'right', 'right', 'down', 'left', 'up', 'left', 'down', 'left', 'down', 'down', 'right', 'down', 'down', 'up', 'up', 'down', 'left', 'up', 'left', 'left', 'right', 'up', 'up', 'down', 'down', 'down', 'down', 'down', 'left', 'up', 'left', 'down', 'down', 'left', 'down', 'left', 'left', 'left', 'right', 'up', 'up', 'right', 'left', 'left', 'up', 'up', 'left', 'down', 'down', 'down', 'left', 'up', 'right', 'down', 'down', 'right', 'up', 'left', 'up', 'down', 'right', 'up', 'right', 'up', 'down', 'right', 'left', 'up', 'right', 'right', 'up', 'right', 'left', 'up', 'left', 'left', 'down', 'right', 'up', 'right', 'right', 'down', 'right', 'left', 'up', 'right', 'right', 'up', 'down', 'down', 'left', 'right', 'down', 'right', 'up', 'left', 'up', 'up', 'up', 'left', 'left', 'down', 'left', 'down', 'left', 'up', 'left', 'down', 'down', 'right', 'up', 'right', 'down', 'right', 'up', 'up', 'left', 'left', 'down', 'right', 'up', 'down', 'up', 'down', 'right', 'up', 'down', 'left', 'left', 'left', 'left', 'left', 'up', 'down', 'right', 'down', 'up', 'left', 'down', 'down', 'down', 'left', 'left', 'down', 'up', 'right', 'down', 'left', 'down', 'right', 'left', 'up', 'down', 'up', 'left', 'down', 'down', 'down', 'right', 'right', 'right', 'right', 'up', 'right', 'up', 'up', 'up', 'right', 'up', 'left', 'up', 'right', 'up', 'left', 'down', 'left', 'down', 'down', 'down', 'left', 'down', 'right', 'up', 'down', 'down', 'right', 'down', 'left', 'left', 'down', 'up', 'down', 'down', 'up', 'left', 'right', 'left', 'right', 'down', 'left', 'down', 'right', 'right', 'up', 'up', 'right', 'right', 'left', 'down', 'up', 'down', 'up', 'right']
    #302 generation, 936 score ['left', 'up', 'left', 'down', 'left', 'up', 'right', 'left', 'down', 'down', 'right', 'down', 'right', 'up', 'right', 'up', 'left', 'up', 'up', 'down', 'down', 'right', 'right', 'down', 'down', 'up', 'up', 'down', 'left', 'up', 'left', 'left', 'right', 'up', 'up', 'down', 'down', 'down', 'down', 'down', 'left', 'up', 'left', 'down', 'down', 'left', 'down', 'left', 'left', 'left', 'right', 'up', 'up', 'right', 'left', 'left', 'up', 'up', 'left', 'down', 'down', 'down', 'left', 'up', 'right', 'down', 'down', 'right', 'up', 'left', 'up', 'down', 'right', 'up', 'right', 'up', 'down', 'right', 'left', 'up', 'right', 'right', 'up', 'right', 'left', 'up', 'left', 'left', 'down', 'right', 'up', 'right', 'right', 'down', 'right', 'left', 'up', 'right', 'right', 'up', 'down', 'down', 'left', 'right', 'down', 'right', 'up', 'left', 'up', 'up', 'up', 'left', 'left', 'down', 'left', 'down', 'left', 'up', 'left', 'down', 'down', 'right', 'up', 'right', 'down', 'right', 'up', 'up', 'left', 'left', 'down', 'right', 'up', 'down', 'up', 'down', 'right', 'up', 'down', 'left', 'left', 'left', 'left', 'left', 'up', 'down', 'right', 'down', 'up', 'left', 'down', 'down', 'down', 'left', 'left', 'down', 'up', 'right', 'down', 'left', 'down', 'right', 'left', 'up', 'down', 'up', 'left', 'down', 'down', 'down', 'right', 'right', 'right', 'right', 'up', 'right', 'up', 'up', 'up', 'right', 'up', 'left', 'up', 'right', 'up', 'left', 'down', 'left', 'down', 'down', 'down', 'left', 'down', 'right', 'up', 'down', 'down', 'right', 'down', 'left', 'left', 'down', 'up', 'down', 'down', 'up', 'left', 'right', 'left', 'right', 'down', 'left', 'down', 'right', 'right', 'up', 'up', 'right', 'right', 'left', 'down', 'up', 'down', 'up', 'right']
    #generation 353 1044
    #premove = ['down', 'down', 'down', 'left', 'down', 'down', 'right', 'left', 'up', 'up', 'up', 'up', 'right', 'right', 'right', 'right', 'right', 'up', 'right', 'right', 'right', 'down', 'down', 'down', 'left', 'down', 'right', 'down', 'left', 'left', 'left', 'up', 'left', 'right', 'right', 'right', 'up', 'down', 'left', 'up', 'left', 'up', 'up', 'left', 'up', 'left', 'down', 'left', 'up', 'right', 'left', 'down', 'down', 'right', 'down', 'right', 'up', 'right', 'up', 'left', 'up', 'up', 'down', 'down', 'right', 'right', 'down', 'down', 'up', 'up', 'down', 'left', 'up', 'left', 'left', 'right', 'up', 'up', 'down', 'down', 'down', 'down', 'down', 'left', 'up', 'left', 'down', 'down', 'left', 'down', 'left', 'left', 'left', 'right', 'up', 'up', 'right', 'left', 'left', 'up', 'up', 'left', 'down', 'down', 'down', 'left', 'up', 'right', 'down', 'down', 'right', 'up', 'left', 'up', 'down', 'right', 'up', 'right', 'up', 'down', 'right', 'left', 'up', 'right', 'right', 'up', 'right', 'left', 'up', 'left', 'left', 'down', 'right', 'up', 'right', 'right', 'down', 'right', 'left', 'up', 'right', 'right', 'up', 'down', 'down', 'left', 'right', 'down', 'right', 'up', 'left', 'up', 'up', 'up', 'left', 'left', 'down', 'left', 'down', 'left', 'up', 'left', 'down', 'down', 'right', 'up', 'right', 'down', 'right', 'up', 'up', 'left', 'left', 'down', 'right', 'up', 'down', 'up', 'down', 'right', 'up', 'down', 'left', 'left', 'left', 'left', 'left', 'up', 'down', 'right', 'down', 'up', 'left', 'down', 'down', 'down', 'left', 'left', 'down', 'up', 'right', 'down', 'left', 'down', 'right', 'left', 'up', 'down', 'up', 'left', 'down', 'down', 'down', 'right', 'right', 'right', 'right', 'up', 'right', 'up', 'up', 'up', 'right', 'up', 'left', 'up', 'right', 'up', 'left', 'down', 'left', 'down', 'down', 'down', 'left', 'down', 'right', 'up', 'down', 'down', 'right', 'down', 'left', 'left', 'down', 'up', 'down', 'down', 'up', 'left', 'right', 'left', 'right', 'down', 'left', 'down', 'right', 'right', 'up', 'up', 'right', 'right', 'left', 'down', 'up', 'down', 'up', 'right']
    #premove = ['left', 'down', 'left', 'left', 'right', 'down', 'down', 'right', 'right', 'down', 'right', 'up', 'right', 'down', 'right', 'right', 'left', 'down', 'up', 'up', 'up', 'left', 'left', 'right', 'up', 'up', 'right', 'left', 'up', 'down', 'up', 'left', 'down', 'down', 'down', 'right', 'left', 'left', 'up', 'down', 'left', 'right', 'down', 'down', 'down', 'left', 'right', 'down', 'down', 'down', 'right', 'up', 'right', 'down', 'right', 'down', 'right', 'right', 'up', 'right', 'up', 'up', 'up', 'left', 'up', 'left', 'left', 'down', 'left', 'left', 'down', 'down', 'right', 'up', 'right', 'up', 'right', 'down', 'left', 'up', 'left', 'down', 'left', 'down', 'down', 'right', 'right', 'down', 'left', 'up', 'right', 'right', 'down', 'right', 'right', 'right', 'right', 'up', 'down', 'left', 'up', 'up', 'left', 'left', 'right', 'down', 'up', 'left', 'down', 'right', 'up', 'left', 'down', 'left', 'up', 'down', 'up', 'left', 'left', 'up', 'down', 'right', 'left', 'up', 'left', 'right', 'up', 'right', 'down', 'right', 'down', 'left', 'left', 'right', 'down', 'left', 'down']
    #all ghosts 579
    #premove = ['right', 'right', 'down', 'down', 'down', 'down', 'left', 'left', 'left', 'left', 'left', 'up', 'left', 'up', 'right', 'up', 'right', 'up', 'right', 'up', 'left', 'left', 'up', 'down', 'down', 'right', 'up', 'down', 'down', 'down', 'up', 'left', 'left', 'up', 'up', 'right', 'up', 'right', 'down', 'up', 'up', 'left', 'right', 'down', 'left', 'down', 'down', 'down', 'down', 'up', 'right', 'left', 'right', 'left', 'left', 'left', 'left', 'left', 'left', 'up', 'left', 'down', 'right', 'right', 'down', 'down', 'down', 'right', 'up', 'right', 'right', 'right', 'up', 'right', 'up', 'right', 'up', 'up', 'up', 'left', 'left', 'left', 'down', 'left', 'left', 'down', 'down', 'down', 'left', 'down', 'right', 'right', 'right', 'right', 'right', 'up', 'up', 'left', 'up', 'left', 'down', 'left', 'up', 'up', 'right', 'up', 'right', 'up', 'down', 'down', 'down', 'up', 'up', 'down', 'left', 'up', 'right', 'right', 'left', 'left', 'down', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'down', 'up', 'down', 'right', 'down', 'down', 'right', 'up', 'up', 'up', 'left', 'down', 'up', 'down', 'up', 'down', 'down', 'left', 'left', 'left', 'down', 'up', 'right', 'right', 'left', 'left', 'right', 'up', 'right', 'down', 'down', 'left', 'left', 'right', 'down']
    #premove = ['down', 'left', 'up', 'down', 'left', 'right', 'right', 'down', 'right', 'down', 'up', 'left', 'right', 'down', 'down', 'down', 'down', 'up', 'up', 'up', 'right', 'right', 'down', 'left', 'left', 'right', 'left', 'down', 'down', 'down', 'right', 'right', 'up', 'right', 'right', 'up', 'up', 'right', 'right', 'left', 'right', 'down', 'up', 'left', 'up', 'left', 'down', 'left', 'left', 'up', 'left', 'up', 'right', 'up', 'right', 'up', 'left', 'left', 'left', 'left', 'left', 'down', 'down', 'right', 'up', 'right', 'up', 'right', 'up', 'left', 'left', 'left', 'left', 'left', 'down', 'right', 'down', 'right', 'down', 'right', 'down', 'down', 'right', 'up', 'down', 'left', 'up', 'up', 'up', 'left', 'up', 'down', 'right', 'down', 'up', 'right', 'left', 'down', 'down', 'down', 'left', 'down', 'right', 'left', 'left', 'down', 'left', 'down', 'down', 'left', 'left', 'down', 'up', 'right', 'up', 'down', 'left', 'right', 'down', 'down', 'up', 'down', 'up', 'up', 'up', 'up', 'right', 'up', 'right', 'right', 'left', 'up', 'up', 'up', 'up', 'left', 'up', 'left', 'down', 'left', 'up', 'up', 'right', 'right', 'down', 'right', 'right', 'right', 'down', 'down', 'down', 'right', 'down', 'left', 'left', 'left', 'down', 'left', 'up', 'left', 'up', 'up', 'up', 'right', 'down', 'right', 'down', 'right', 'up', 'up', 'left', 'up', 'left', 'left', 'left', 'left', 'down', 'right', 'right', 'up', 'right', 'down', 'right', 'right', 'up', 'down', 'down', 'left', 'left', 'up', 'right', 'right', 'left', 'left', 'down', 'right', 'left', 'down', 'left', 'left', 'up', 'left', 'right', 'left', 'left', 'right', 'left', 'up', 'up', 'left', 'left', 'right', 'up', 'right', 'up', 'right', 'down', 'left', 'right', 'left', 'down', 'up', 'down', 'left', 'right', 'right', 'right', 'down', 'down', 'left', 'up', 'up', 'right', 'down', 'down', 'down', 'left', 'left', 'left', 'left', 'left', 'up', 'up', 'right', 'up', 'right', 'down', 'right', 'down', 'down', 'left', 'left', 'left', 'left', 'left', 'up', 'up', 'up', 'up', 'right', 'up', 'right', 'right', 'down', 'right', 'right', 'down', 'down', 'down', 'down', 'left', 'up', 'left', 'left', 'left', 'up', 'right', 'up', 'right', 'down', 'right', 'down', 'down', 'right', 'down', 'left', 'up', 'left', 'up', 'down', 'down', 'up', 'up', 'left', 'up', 'left', 'right', 'up', 'up', 'left', 'right', 'down', 'down', 'down', 'down', 'down', 'left', 'up', 'left', 'up', 'right', 'up', 'right', 'up', 'right', 'up', 'right', 'down', 'down', 'down', 'left', 'left', 'left', 'left', 'left', 'up', 'up', 'up', 'right', 'down', 'right', 'up', 'right', 'down', 'left', 'up', 'left', 'up', 'right', 'up', 'left', 'left', 'up', 'up', 'down', 'left', 'up', 'down', 'left', 'down', 'up', 'up', 'right', 'down', 'right', 'right', 'left', 'up', 'left', 'up', 'left', 'up', 'right', 'down', 'right', 'down', 'left', 'left', 'down', 'right', 'down', 'right', 'left', 'right', 'left', 'left', 'left', 'left', 'down', 'right', 'right', 'right', 'right', 'left', 'up', 'right', 'right', 'up', 'up', 'right', 'up', 'left', 'up', 'left', 'down', 'left', 'right', 'left', 'down', 'down', 'up', 'up', 'right', 'down', 'right', 'down', 'down', 'down', 'left', 'left', 'up', 'up', 'right', 'down', 'left']

    #winning strategy
    premove = ['right', 'up', 'left', 'left', 'left', 'down', 'right', 'down', 'up', 'up', 'up', 'up', 'up', 'up', 'left', 'up', 'left', 'left', 'up', 'left', 'up', 'down', 'down', 'left', 'down', 'left', 'up', 'right', 'right', 'left', 'up', 'up', 'down', 'right', 'up', 'up', 'down', 'up', 'up', 'right', 'down', 'down', 'left', 'up', 'up', 'down', 'right', 'left', 'right', 'right', 'down', 'down', 'down', 'left', 'right', 'right', 'left', 'right', 'up', 'down', 'up', 'right', 'left', 'up', 'up', 'left', 'up', 'left', 'up', 'left', 'up', 'right', 'right', 'down', 'right', 'down', 'right', 'up', 'right', 'down', 'down', 'down', 'down', 'left', 'up', 'left', 'left', 'left', 'left', 'up', 'left', 'up', 'up', 'up', 'right', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'down', 'left', 'left', 'down', 'left', 'left', 'left', 'up', 'up', 'right', 'up', 'up', 'left', 'up', 'up', 'down', 'left', 'down', 'left', 'left', 'left', 'down', 'right', 'right', 'down', 'up', 'right', 'left', 'right', 'down', 'down', 'down', 'down', 'right', 'right', 'down', 'down', 'up', 'up', 'down', 'right', 'left', 'left', 'right', 'up', 'left', 'left', 'left', 'left', 'up', 'down', 'right', 'left', 'right', 'up', 'up', 'up', 'right', 'right', 'up', 'right', 'up', 'right', 'down', 'down', 'down', 'left', 'left', 'left', 'left', 'left', 'up', 'up', 'right', 'up', 'right', 'down', 'right', 'down', 'down', 'left', 'left', 'left', 'left', 'left', 'left', 'down', 'right', 'up', 'up', 'up', 'up', 'up', 'up', 'left', 'down', 'left', 'left', 'up', 'up', 'right', 'right', 'down', 'left', 'left', 'right', 'right', 'down', 'right', 'down', 'up', 'left', 'right', 'down', 'down', 'down', 'down', 'up', 'up', 'up', 'right', 'right', 'down', 'left', 'left', 'right', 'left', 'down', 'down', 'down', 'right', 'right', 'up', 'right', 'right', 'up', 'up', 'right', 'right', 'left', 'right', 'down', 'up', 'left', 'up', 'left', 'down', 'left', 'left', 'up', 'left', 'up', 'right', 'up', 'right', 'up', 'left', 'left', 'left', 'left', 'left', 'down', 'down', 'right', 'up', 'right', 'up', 'right', 'up', 'left', 'left', 'left', 'left', 'left', 'down', 'right', 'down', 'right', 'down', 'right', 'down', 'down', 'right', 'up', 'down', 'left', 'up', 'up', 'up', 'left', 'up', 'down', 'right', 'down', 'up', 'right', 'left', 'down', 'down', 'down', 'left', 'down', 'right', 'left', 'left', 'down', 'left', 'down', 'down', 'left', 'left', 'down', 'up', 'right', 'up', 'down', 'left', 'right', 'down', 'down', 'up', 'down', 'up', 'up', 'up', 'up', 'right', 'up', 'right', 'right', 'left', 'up', 'up', 'up', 'up', 'left', 'up', 'left', 'down', 'left', 'up', 'up', 'right', 'right', 'down', 'right', 'right', 'right', 'down', 'down', 'down', 'right', 'down', 'left', 'left', 'left', 'down', 'left', 'up', 'left', 'up', 'up', 'up', 'right', 'down', 'right', 'down', 'right', 'up', 'up', 'left', 'up', 'left', 'left', 'left', 'left', 'down', 'right', 'right', 'up', 'right', 'down', 'right', 'right', 'up', 'down', 'down', 'left', 'left', 'up', 'right', 'right', 'left', 'left', 'down', 'right', 'left', 'down', 'left', 'left', 'up', 'left', 'right', 'left', 'left', 'right', 'left', 'up', 'up', 'left', 'left', 'right', 'up', 'right', 'up', 'right', 'down', 'left', 'right', 'left', 'down', 'up', 'down', 'left', 'right', 'right', 'right', 'down', 'down', 'left', 'up', 'up', 'right', 'down', 'down', 'down', 'left', 'left', 'left', 'left', 'left', 'up', 'up', 'right', 'up', 'right', 'down', 'right', 'down', 'down', 'left', 'left', 'left', 'left', 'left', 'up', 'up', 'up', 'up', 'right', 'up', 'right', 'right', 'down', 'right', 'right', 'down', 'down', 'down', 'down', 'left', 'up', 'left', 'left', 'left', 'up', 'right', 'up', 'right', 'down', 'right', 'down', 'down', 'right', 'down', 'left', 'up', 'left', 'up', 'down', 'down', 'up', 'up', 'left', 'up', 'left', 'right', 'up', 'up', 'left', 'right', 'down', 'down', 'down', 'down', 'down', 'left', 'up', 'left', 'up', 'right', 'up', 'right', 'up', 'right', 'up', 'right', 'down', 'down', 'down', 'left', 'left', 'left', 'left', 'left', 'up', 'up', 'up', 'right', 'down', 'right', 'up', 'right', 'down', 'left', 'up', 'left', 'up', 'right', 'up', 'left', 'left', 'up', 'up', 'down', 'left', 'up', 'down', 'left', 'down', 'up', 'up', 'right', 'down', 'right', 'right', 'left', 'up', 'left', 'up', 'left', 'up', 'right', 'down', 'right', 'down', 'left', 'left', 'down', 'right', 'down', 'right', 'left', 'right', 'left', 'left', 'left', 'left', 'down', 'right', 'right', 'right', 'right', 'left', 'up', 'right', 'right', 'up', 'up', 'right', 'up', 'left', 'up', 'left', 'down', 'left', 'right', 'left', 'down', 'down', 'up', 'up', 'right', 'down', 'right', 'down', 'down', 'down', 'left', 'left', 'up', 'up', 'right', 'down', 'left']



    population = [random_move() for _ in range(num_players)]
    parent_dice = [0, 1, 2, 3]
    parent_weight = (1, 0, 0, 0)
    #parent_weight = (0.65, 0.2, 0.1, 0.05)

    for generation in range(GENERATIONS):
        fitness_scores = []
        for strategy in population:
            current_score, current_moves_used = main(strategy + premove)
            fitness_scores.append((current_score, current_moves_used))

        #fitness_scores = [main(strategy) for strategy in population]
        generation_average = numpy.mean([x for x, y in fitness_scores])
        print(f'{generation} mean: {generation_average}')

        population_score_list = []
        for i, score in enumerate(fitness_scores):
            population_score_list.append((score[0], i, score[1]))

        population_score_list.sort(reverse=True)

        parent_score = population_score_list[[random.choices(parent_dice, parent_weight, k=1)][0][0]][0]
        baseline = 5*imp_counter+100
        # parent = population[population_score_list[random.choices(parent_dice, weights=parent_weight, k=1)[0]][1]]
        # print(population_score_list[random.choices(parent_dice, weights=parent_weight, k=1)[0]][0])
        parent = population[population_score_list[0][1]]
        print("parent score", parent_score)
        print("baseline", baseline)
        print(premove)



        if generation == 0:
            premove = population_score_list[0][2]
            imp_counter += 1
            fail_counter = 0

        if parent_score > baseline:
            premove = population_score_list[0][2]
            imp_counter += 1
            fail_counter = 0
            if parent_score > baseline + 100:
                imp_counter + 19
        else:
            fail_counter += 1

        if fail_counter > 2:
            premove = premove[3:]
            fail_counter = 0
            imp_counter -= 1

        # if population_score_list[0][0] > 5*imp_counter+20:
        #     imp_counter = (population_score_list[0][0])/5
        #     imp_counter -= 2

        # population = [random_move() for _ in range(num_players)]
        population = [mutate(parent[:-len(premove)]+ random_move()) for _ in range(num_players)]

    # Return the best strategy found
    population_score_list = []
    for i, score in enumerate(fitness_scores):
        population_score_list.append((score, i))

    population_score_list.sort(reverse=True)
    return population[population_score_list[0][1]], population_score_list[0][0]

# Run the genetic algorithm
best_strategy = genetic_algorithm()
print("Best Pac-Man Strategy:", best_strategy)
