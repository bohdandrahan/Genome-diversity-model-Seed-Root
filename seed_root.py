import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from world import World
from population import AsexualPopulation
from species import Bacteria
from model import ModelAsexualPopulation as md 

model = md(World, AsexualPopulation, Bacteria, 500, 50)
model.plot_pop()