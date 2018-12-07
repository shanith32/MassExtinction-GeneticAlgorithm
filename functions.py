import random
import copy


def main():
    print("Mass Extinction Genetic Algorithm")
    data = [[4, 2, 0], [5, 2, 1], [7, 11, 2],
            [7, 11, 3]]  # object set with the properties - [value, weight, id]
    container = []  # the container to contain the objects in
    capacity = 10  # weight capacity of the container
    popSize = 5  # population size
    GEN_AMOUNT = 10  # how many generations to run
    probability = 0.5

    initailPopulation = generateInitialPopulation(popSize, capacity, data)
    print("The Randomly Generated INITIAL POPULATION is ", initailPopulation)


def generateChromosome(data):
    chromosome = [] * 3  # [[binary soultion], fitness, total weight]
    solution = []

    for i in range(len(data)):
        select = random.randint(0, 1)
        solution.append(select)
    fitness = 0
    totalWeight = 0
    for k in range(len(solution)):
        if (solution[k] == 1):
            fitness += data[k][0]
            totalWeight += data[k][1]
    chromosome.append(solution)
    chromosome.append(fitness)
    chromosome.append(totalWeight)
    return chromosome


def generateInitialPopulation(popSize, capacity, data):
    # Initial Population
    initailPopulation = []  # The inital population array
    initCount = 0
    while (initCount != popSize):
        newChromosome = generateChromosome(data)
        if (newChromosome[2] <= capacity):
            initailPopulation.append(newChromosome)
            initCount += 1
    return initailPopulation


if __name__ == "__main__":
    main()
