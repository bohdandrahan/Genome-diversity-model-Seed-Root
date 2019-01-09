import pygal
from pygal.style import DarkStyle
import numpy as np
import random

class Model():
    '''Abstract class'''
    def __init__(self, world_type, population_type, species, iterations = 100, initial_pop_size = 200, birth_prob = 0.05):
        self.world = world_type()
        self.species = species
        self.population = population_type(self.world, species, initial_pop_size, birth_prob)
        self.iterations = iterations

    def get_x_lables(self, some_data):
        x_labels = list()
        for each in range(len(some_data)):
            if each // 50 * 50 == each:
                x_labels.append(each)
            else: x_labels.append(None)
        return x_labels

class ModelAsexualPopulation(Model):
    '''Concrete class'''
    def get_population_data(self):
        pop_size =list()
        original_genes = list()
        genes = list()

        for i in range(self.iterations):
            pop_size.append(len(self.population.get_pop()))
            original_genes.append(len(self.population.get_original_genes()))
            genes.append(tuple(self.population.get_genes_matrix()))

            self.population.kill_wave()
            self.population.birth_wave()
            self.population.update_genes_matrix()
        return pop_size, original_genes, genes

    def plot_pop(self):
        pop_size, original_genes, genes = self.get_population_data()
        x = range(len(pop_size))
        chart1 = pygal.XY(style = DarkStyle, legend_at_bottom=True, show_dots = False, fill=True)
        chart1.title = str('Genome diversity in population with asexual reproduction over ' + str(len(pop_size) - 1) +
                         ' generations. \n Quantity of original genes from the first generation in population ')
        chart1.add('Population size', list(zip(x, pop_size)))
        chart1.add('Diversity', list(zip(x, original_genes)))
        chart1.render_to_file('charts/Autogamy_1.svg')

        genes = np.array(genes).T

        x2 = map(str, range(len(genes)))
        chart2 = pygal.StackedLine(fill = True, show_dots = False, style = DarkStyle, legend_at_bottom=True, truncate_label=-1)
        chart2.title = 'Genome diversity in population with asexual reproduction \n over ' + str(len(pop_size) - 1) + ' generations'
        chart2.x_labels = self.get_x_lables(pop_size)

        for x2_, genes_ in zip(x2, genes):
            chart2.add('"'+str(x2_)+'"', genes_)
        chart2.render_to_file('charts/Autogamy_2.svg')


class ModelSexualPopulaiton(Model):
    def get_population_data(self):
        pop_size =list()
        rdm_individuals = list()
        populations = list()
        
        for i in range(self.iterations):
            pop_size.append(len(self.population.get_pop()))
            rdm_individuals.append(random.choice(self.population.get_pop()))
            populations.append(self.population.get_pop())

            self.population.kill_wave()
            self.population.update_couples()
            self.population.birth_wave()
            self.population.update_genes()

        return pop_size, rdm_individuals, populations

    def plot_pop(self):
        pop_size, rdm_individuals, populations = self.get_population_data()

        #CHART 1
        x = range(len(pop_size))
        chart1 = pygal.XY(style = DarkStyle, legend_at_bottom=True, show_dots = False, fill=True, include_x_axis=True)
        chart1.title = str('Population size over  ' + str(len(pop_size)) +
                         ' generations.')
        chart1.add('Population size', list(zip(x, pop_size)))
        chart1.render_to_file('charts/Sexual_reproduction_1.svg')

        #CHART 2
        rdm_ind_data = sorted(self.get_genes_data(rdm_individuals))
        genes = rdm_ind_data

        x2 = map(str, range(len(genes)))
        chart2 = pygal.StackedBar(style = DarkStyle, legend_at_bottom=True, truncate_label=-1)
        chart2.title = ('Genome of a random individual from the population over \n ' +
                        str(len(pop_size)) + ' generations. \n Monogamy: ' + str(self.population.monogamy) +
                        ',    Long term: ' + str(self.population.long_term))
        chart2.x_labels = self.get_x_lables(pop_size)

        for x2_, genes_ in genes:
            chart2.add(x2_, genes_)
        chart2.render_to_file('charts/Sexual_reproduction_2.svg')

        #CHART 3

        for population in populations:
            if populations.index(population) % 50 == 0:
                genes = sorted(self.get_genes_data(population))

                x2 = map(str, range(len(genes)))
                chart2 = pygal.StackedBar(style = DarkStyle, legend_at_bottom=True, truncate_label=-1)
                chart2.title = ('Gentoype of each individual of generation #' +
                                str(populations.index(population)) + '. \n Monogamy: ' + str(self.population.monogamy) +
                                ',    Long term: ' + str(self.population.long_term))

                for x2_, genes_ in genes:
                    chart2.add(x2_, genes_)
                chart2.render_to_file('charts/Genes_' +str(populations.index(population))+ '.svg')

    def get_genes_data(self, individuals):
        #Refactor this
        genotypes = list()
        for individual in individuals:
            genotypes.append(individual.get_genotype())

        result = dict()

        counter = 1
        for genotype in genotypes:
            dna = genotype.get_genotype()
            current = list()
            for each in dna:
                if each[0] not in result:
                    result[each[0]] = [each[1]]
                else:
                    result[each[0]].append(each[1])
                current.append(each[0])
            for dna_name in result:
                if dna_name not in current:
                    result[dna_name].append(0)

            sub_genotypes = genotypes[counter:]
            for genotype in sub_genotypes:
                sub_dna = genotype.get_genotype()

                for each in sub_dna:
                    if each[0] not in current:
                        if each[0] in result:
                            pass
                        else:
                            result[each[0]] = [0]
            counter +=1

        genes_matrix = list()
        for each in result:
            genes_matrix.append(('"'+str(each)+'"',result[each]))
        return genes_matrix
