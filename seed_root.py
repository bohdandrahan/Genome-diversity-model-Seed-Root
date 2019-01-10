import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from world import World
from population import AsexualPopulation
from population import SexualPopulation
from species import Bacteria
from species import Giraffe
from model import ModelAsexualPopulation
from model import ModelSexualPopulaiton 

# model = ModelAsexualPopulation(World, AsexualPopulation, Bacteria, 500, 50)
# model.plot_pop()

species = Giraffe
population = SexualPopulation
iterations = 250
initial_pop = 10
birth_prob = 0.1
model = ModelSexualPopulaiton(World, population, species, iterations, initial_pop, birth_prob)
model.plot_pop()