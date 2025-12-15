import bombusters as bb
from utils import *

NUMBER_OF_PLAYERS = 4
AVAILABLE_NUMBERS = 4 
NUMBER_INSTANCES = 4
NUMBER_OF_SAMPLES = 10000

if True:
    distrib = bb.sample_distribution(NUMBER_OF_PLAYERS, AVAILABLE_NUMBERS, NUMBER_INSTANCES, NUMBER_OF_SAMPLES)
    print_distribution(distrib)
    plot_distribution(distrib)

if False:

    for _ in range(10):
        print(bb.sample_game(NUMBER_OF_PLAYERS, AVAILABLE_NUMBERS, NUMBER_INSTANCES))
