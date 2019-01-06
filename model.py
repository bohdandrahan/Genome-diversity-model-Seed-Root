import pygal
from pygal.style import DarkStyle
import numpy as np

class Model():
    '''Abstract class'''
    def __init__(self, world_type, population_type, iterations = 100, initial_pop_size = 200):
        self.world = world_type()
        self.population = population_type(self.world, initial_pop_size = initial_pop_size)
        self.iterations = iterations

class ModelAsexualPopulation(Model):
    '''Concrete class'''
    def get_population_data(self):

        pop_size =list()
        pop_size.append(len(self.population.get_pop()))

        original_genes = list()
        original_genes.append(len(self.population.get_original_genes()))

        genes = list()
        genes.append(tuple(self.population.get_genes_matrix()))

        for i in range(self.iterations):
            self.population.kill_wave()
            self.population.birth_wave()
            self.population.update_genes_matrix()

            pop_size.append(len(self.population.get_pop()))
            original_genes.append(len(self.population.get_original_genes()))
            genes.append(tuple(self.population.get_genes_matrix()))
        return pop_size, original_genes, genes

    def plot_pop(self):
        pop_size, original_genes, genes = self.get_population_data()
        x = range(len(pop_size))
        chart = pygal.XY(style = DarkStyle, legend_at_bottom=True)
        chart.title = str('Genome diversity in asexual population over ' + str(len(pop_size) - 1) + ' generation')
        chart.add('Population size', list(zip(x, pop_size)))
        chart.add('Diversity', list(zip(x, original_genes)))
        chart.render_to_file('pop_chart.svg')

        genes = np.array(genes).T

        x2 = map(str, range(len(genes)))
        bar_chart = pygal.StackedLine(fill = True, show_dots = False, style = DarkStyle, legend_at_bottom=True)
        bar_chart.title = 'Genome diversity in asexual population over ' + str(len(pop_size) - 1) + ' generations (Autogamy)'

        for x2_, genes_ in zip(x2, genes):
            bar_chart.add(x2_, genes_)
        bar_chart.render_to_file('gen_bar_chart.svg')

