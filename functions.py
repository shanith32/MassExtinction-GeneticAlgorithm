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
    # parent selection
    parentOne = selection(initailPopulation)
    parentTwo = selection(initailPopulation)
    print("parentOne: ", parentOne, " parentTwo: ", parentTwo)
    # crossover
    offSpringSolution = crossover(data, parentOne, parentTwo)
    print("OffSpringSolution after crossover: ", offSpringSolution)
    mutatedOffSpring = mutation(data, offSpringSolution, probability)
    print("OffSpringSolution after mutation: ", mutatedOffSpring)
    newOffSpringChomosome = encodeChromosome(data, mutatedOffSpring)
    print("New OffSpring Chromosome: ", newOffSpringChomosome)
    # genCount = 0
    # while (genCount)


# Functions
# Generate a random solution
def generateRandomSolution(data):
    solution = []
    for i in range(len(data)):
        select = random.randint(0, 1)
        solution.append(select)
    return solution


# Encode a chromosome
def encodeChromosome(data, solution):
    chromosome = [] * 3  # [[binary soultion], fitness, total weight]
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


# Generate a population of random chromosomes
def generateInitialPopulation(popSize, capacity, data):
    # Initial Population
    initailPopulation = []  # The inital population array
    initCount = 0
    while (initCount != popSize):
        randSolution = generateRandomSolution(data)
        newChromosome = encodeChromosome(data, randSolution)
        if (newChromosome[2] <= capacity):
            initailPopulation.append(newChromosome)
            initCount += 1
    return initailPopulation


# Two Tournament Selection
def selection(population):
    chromoOne = random.choice(population)
    chromoTwo = random.choice(population)

    if(chromoOne[1] > chromoTwo[1]):
        return chromoOne
    else:
        return chromoTwo


# One point Crossover
def crossover(data, parentOne, parentTwo):
    cutPoint = len(parentOne[0])//2
    done = 0
    offSpringSolution = []
    while(done < cutPoint):
        offSpringSolution.append(parentOne[0][done])
        done += 1
    while(done < len(parentOne[0])):
        offSpringSolution.append(parentTwo[0][done])
        done += 1

    return offSpringSolution


# One index flip Mutation
def mutation(data, solution, probability):
    randomIndex = random.randint(0, len(data) - 1)
    mutation = solution[randomIndex]
    chance = random.random() <= probability
    if (chance):
        if (mutation == 0):
            solution[randomIndex] = 1
        else:
            solution[randomIndex] = 0
    return solution


if __name__ == "__main__":
    main()
