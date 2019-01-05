import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from world import World
from population import AsexualPopulation
from species import Bacteria
from model import ModelAsexualPopulation as md 

m = md(World, AsexualPopulation, 200, 50)
m.plot_pop()