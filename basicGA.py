# Basic Genetic algorithm to deal with the Knapsack problem
import random
import copy


def main():
    print("Mass Extinction Genetic Algorithm")
    print("- - - - - - - - - - - - - - - - - ")
    data = [[4, 2, 0], [5, 2, 1], [7, 11, 2],
            [7, 11, 3]]  # object set with the properties - [value, weight, id]
    capacity = 10  # weight capacity of the container
    popSize = 5  # population size
    genAmout = 10  # how many generations to run
    probability = 0.5
    # Randomly generate the initial population
    initailPopulation = generateInitialPopulation(popSize, capacity, data)
    print("The Randomly Generated initail population: ", initailPopulation)

    # Generation GA loop
    genCount = 0
    while (genCount != genAmout):
        populationTwo = []  # Second population array
        popCount = 0
        while (popCount != popSize):
            populationOne = copy.deepcopy(
                initailPopulation)  # First population array
            # parent selection
            parentOne = selection(populationOne)
            parentTwo = selection(populationOne)
            # crossover
            offSpringSolution = crossover(data, parentOne, parentTwo)
            # mutation
            mutatedOffSpring = mutation(data, offSpringSolution, probability)
            # encode soultion into a chromosome
            newOffSpringChomosome = encodeChromosome(data, mutatedOffSpring)
            # evaluation
            if(evaluation(newOffSpringChomosome, capacity)):
                populationTwo.append(newOffSpringChomosome)
                popCount += 1
        print("Generation number: ", genCount, " Population: ", populationTwo)
        initailPopulation = copy.deepcopy(populationTwo)
        genCount += 1

    print("- - - - - - - - - - - - - - - - - ")
    print("Final population: ", initailPopulation)
    sortedFinalPop = sorted(
        initailPopulation, key=lambda x: x[1], reverse=True)
    result = sortedFinalPop[0]
    print("- - - - - - - - - - - - - - - - - ")
    print("Most fit final chromosome: ", result)
    print("Total value: ", result[1],
          " Total weight: ", result[2])


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


# OffSpring Evaluaion
def evaluation(offSpringChromosome, capacity):
    if (offSpringChromosome[2] <= capacity):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
