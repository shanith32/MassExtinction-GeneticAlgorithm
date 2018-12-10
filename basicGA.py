# Basic Genetic algorithm to deal with the Knapsack problem
import random
import copy
import matplotlib.pyplot as plt
import readData


def main():
    print("Basic Genetic Algorithm")
    print("- - - - - - - - - - - - - - - - - ")
    # object set with the properties - [value, weight, id]
    data, capacity = readData.main()
    popSize = 10  # population size
    genAmout = 900  # how many generations to run
    probability = 0.5
    highestFitnessList = []  # Track the highest fitness in each generation
    # Randomly generate the initial population
    initailPopulation = generateInitialPopulation(popSize, capacity, data)
    # Highest fitness of the random initail population
    hFitness = highestFitness(initailPopulation)
    highestFitnessList.append(hFitness)
    print("The Randomly Generated initail population: ", initailPopulation)
    print("Highest Fitness: ", hFitness)

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
            offSpringSolution = crossover(
                data, parentOne, parentTwo, probability)
            # mutation
            mutatedOffSpring = mutation(data, offSpringSolution, probability)
            # encode soultion into a chromosome
            newOffSpringChomosome = encodeChromosome(data, mutatedOffSpring)
            # evaluation
            if(evaluation(newOffSpringChomosome, capacity)):
                populationTwo.append(newOffSpringChomosome)
                popCount += 1
        hFitness = highestFitness(populationTwo)
        highestFitnessList.append(hFitness)
        print("Generation number: ", genCount, " Population: ", populationTwo)
        initailPopulation = copy.deepcopy(populationTwo)
        genCount += 1

    print("- - - - - - - - - - - - - - - - - ")
    print("Highest fitness list: ", highestFitnessList)
    print("Final population: ", initailPopulation)
    sortedFinalPop = sorted(
        initailPopulation, key=lambda x: x[1], reverse=True)
    result = sortedFinalPop[0]
    print("- - - - - - - - - - - - - - - - - ")
    print("Most fit final chromosome: ", result)
    print("Total value: ", result[1],
          " Total weight: ", result[2])
    plt.plot(highestFitnessList)
    plt.ylabel('Highest Fitness')
    plt.xlabel('Generation Count')
    plt.show()


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
def crossover(data, parentOne, parentTwo, probability):
    chance = random.random() <= probability
    if (chance):
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
    else:
        return parentOne[0]


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


# Take the higest fitness of the population
def highestFitness(population):
    # sumforave = 0
    # for i in range(len(population)):
    #     sumforave += population[i][1]
    # return sumforave/len(population)
    sortedFinalPop = sorted(
        population, key=lambda x: x[1], reverse=True)
    result = sortedFinalPop[0][1]
    return result


if __name__ == "__main__":
    main()
