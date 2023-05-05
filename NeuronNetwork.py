import numpy as np
import Bird as Bird_Class
from settings import *
import sys
import random


class NeurolNetwork:
    def __init__(self, genome=None):
        self.fitness = 0
        self.weight1 = np.random.uniform(-1, 1, (HIDDEN_LAYER, INPUT_LAYER + 1))
        self.weight2 = np.random.uniform(-1, 1, (OUTPUT_LAYER, HIDDEN_LAYER + 1))

        if genome is not None:
            self.decode(genome)

    def __relu(self, np_array):
        return np.maximum(0, np_array)

    def __leaky_relu(self, np_array):
        return np.maximum(0.01 * np_array, np_array)

    def __regularize_input(self, list_input):
        if np.shape(list_input) != (INPUT_LAYER, 1):
            sys.exit('INPUT to Neural Nets doesnt match')

        return list_input / np.linalg.norm(list_input)

    def feed_forward(self, list_input):
        if np.shape(list_input) != (INPUT_LAYER, 1):
            sys.exit('INPUT to Neural Nets doesnt match')

        regularized_input = self.__regularize_input(list_input)

        nodes_hidden_layer = np.dot(self.weight1, np.concatenate((np.array([[1]]), regularized_input), axis=0))

        activation_hidden_layer = self.__relu(nodes_hidden_layer)

        node_output_layer = np.dot(self.weight2, np.concatenate((np.array([[1]]), activation_hidden_layer), axis=0))

        return self.__relu(node_output_layer)

    def encode(self):

        genome = []

        for row in range(self.weight1.shape[0]):
            for row_element in range(self.weight1.shape[1]):
                genome.append(self.weight1[row][row_element])

        for row in range(self.weight2.shape[0]):
            for row_element in range(self.weight2.shape[1]):
                genome.append(self.weight2[row][row_element])

        return genome

    def decode(self, genome):
        for i in range(HIDDEN_LAYER):
            for j in range(INPUT_LAYER + 1):
                self.weight1[i][j] = genome[i * (INPUT_LAYER + 1) + j]

        for i in range(OUTPUT_LAYER):
            for j in range(HIDDEN_LAYER + 1):
                self.weight2[i][j] = genome[(i * OUTPUT_LAYER) + j + HIDDEN_LAYER * (INPUT_LAYER + 1)]

    @classmethod
    def selection(cls, bird_list):
        elite_birds_copy = []

        for _ in range(round(SELECTION_PERCENTAGE * POPULATION)):
            # Select k random birds
            k = 4
            contenders = random.sample(bird_list, k)
            # Choose the bird with the highest fitness
            winner = max(contenders, key=lambda bird: bird.NeurolNetwork.fitness)
            gen = winner.NeurolNetwork.encode()
            elite_birds_copy.append(Bird_Class.Bird(gen))

        return elite_birds_copy

    @classmethod
    def mutation(cls, bird):
        gen = bird.NeurolNetwork.encode()
        bird_fitness = bird.NeurolNetwork.fitness
        max_fitness = max([bird.NeurolNetwork.fitness for bird in bird_list])

        # Calculate adaptive mutation rate
        adaptive_mutation_rate = MUTATION_RATE * (1 - bird_fitness / max_fitness)

        for i in range(TOTAL_WEIGHT):
            if np.random.rand(0, 100) < adaptive_mutation_rate * 100:
                gen[i] = np.random.uniform(-1, 1)

        new_bird = Bird_Class.Bird(gen)
        return new_bird

    @classmethod
    def crossover(cls, bird1, bird2):
        gen_bird1 = bird1.NeurolNetwork.encode()
        gen_bird2 = bird2.NeurolNetwork.encode()

        for i in gen_bird1:
            if (np.random.rand(0, 100) < CROSSOVER_RATE * 100):
                gen_bird1[i], gen_bird2[i] = gen_bird2[i], gen_bird1[1]

        return [Bird_Class.Bird(gen_bird1), Bird_Class.Bird(gen_bird2)]

    @classmethod
    def save_weight(cls):
        pass

    @classmethod
    def create_new_generation(cls, bird_list):
        new_generation = []

        # selection
        elite_birds = NeurolNetwork.selection(bird_list)
        new_generation.extend(elite_birds)

        # mutation
        for i in range(0, round(MUTATION_PERCENTAGE * 100 / POPULATION)):
            new_generation.append(NeurolNetwork.mutation(bird_list[i]))

        # crossover with the elite birds
        for i in range(round((MUTATION_PERCENTAGE * 100 / POPULATION)),
                       round(((MUTATION_PERCENTAGE * 100 / POPULATION) + (CROSSOVER_PERCENTAGE * 100 / POPULATION)))):
            new_generation.append(
                NeurolNetwork.crossover(bird_list[i], elite_birds[random.randint(0, len(elite_birds) - 1)])[0])

        # random bird to increase diversity
        for i in range(POPULATION - len(new_generation)):
            new_generation.append(Bird_Class.Bird())

        return new_generation
