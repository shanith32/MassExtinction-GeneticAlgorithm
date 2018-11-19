import random
import copy
# Genetic algorithm to deal with the Knapsack problem

done = False

while (done != True):
    print(
        "This is a cool Evolutionary Algorithm!\n(⌐■_■)--︻╦╤─ - - - - - - - - - - - -\n\nInput ^Z anytime and hit Enter to exit the program immediately!\n"
    )
    container = []  # the container to contain the objects in

    capacity = int(input("Specify the CAPACITY of the container: ")
                   )  # weight capacity of the container

    x = int(input("Specify the NUMBER OF OBJECTS you want: ")
            )  # How many object will be there in the dataset

    print("Set up each object's values accordingly Ex: [value, weight, id],")

    data = []  # object set with the properties - [value, weight, id]

    for i in range(x):
        obj = []  # An object
        obj.append(int(input("Enter VALUE: ")))
        obj.append(int(input("Enter WEIGHT: ")))
        obj.append(i)
        print("Object number ", i, " is ", obj)
        data.append(obj)
    print("- - - - - - - - - - - - - - - - - ")
    print("THE DATA SET IS => ", data)
    print("- - - - - - - - - - - - - - - - - ")

    POP_SIZE = int(
        input(
            "Specify the number of Chromosomes in a generation or the POPULATION SIZE: "
        ))  # population size

    GEN_AMOUNT = int(
        input("Specify the amount of GENERATIONS to run the algorithm: ")
    )  # how many generations to run

    probability = float(
        input(
            "Specify the MUTATION RATE/PROBABILITY(Enter a decimal in between 0 & 1): "
        ))  # mutation rate
    print("- - - - - - - - - - - - - - - - - ")

    repeat = True
    while (repeat != False):
        # Initial Population
        INITIAL_POPULATION = []  # The inital population array
        initCount = 0
        while (initCount != POP_SIZE):
            CHROMO = [] * 3  # [[binary soultion], fitness, total weight]
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
            CHROMO.append(solution)
            CHROMO.append(fitness)
            CHROMO.append(totalWeight)
            if (CHROMO[2] <= capacity):
                INITIAL_POPULATION.append(CHROMO)
                initCount += 1

        print("The Randomly Generated INITIAL POPULATION is ",
              INITIAL_POPULATION)
        print("- - - - - - - - - - - - - - - - - ")

        # Generation GA loop
        genCount = 0
        while (genCount != GEN_AMOUNT):
            print("Generation number => ", genCount)
            POPULATION_TWO = []  # Second population array
            popCount = 0
            # for i in range(2):
            while (popCount != POP_SIZE):
                # print("Initial pop of gen:", genCount, "is:", INITIAL_POPULATION)
                POPULATION_ONE = copy.deepcopy(
                    INITIAL_POPULATION)  # First population array
                sortedPop = sorted(
                    POPULATION_ONE, key=lambda x: x[1], reverse=True)
                # Find Parent Chromosome
                # print("sorted pop", sortedPop)
                parent = sortedPop[0]
                print("   Selected PARENT CHROMOSOME => ", parent)
                # mutation
                offspringSolution = parent[0]
                # print("offspring sol before:", offspringSolution)
                randomIndex = random.randint(0, len(data) - 1)
                # print("random index to mutate:", randomIndex)
                mutation = offspringSolution[randomIndex]
                # print("value in the random index: ", mutation)
                sortedPop = sorted(
                    POPULATION_ONE, key=lambda x: x[1], reverse=True)
                # Chance of mutation to happen based on mutaion rate
                chance = random.random() <= probability
                if (chance):
                    if (mutation == 0):
                        offspringSolution[randomIndex] = 1
                    else:
                        offspringSolution[randomIndex] = 0
                # print("offspring sol after mutation:", offspringSolution)
                # create offspring Chromosome
                CHROMO = [] * 3  # [[binary soultion], fitness, total weight]
                fitness = 0
                totalWeight = 0
                for j in range(len(offspringSolution)):
                    if (offspringSolution[j] == 1):
                        fitness += data[j][0]
                        totalWeight += data[j][1]
                CHROMO.append(offspringSolution)
                CHROMO.append(fitness)
                CHROMO.append(totalWeight)
                print("   OFFSPRING CHROMOSOME => ", CHROMO)
                if (CHROMO[2] <= capacity):
                    POPULATION_TWO.append(CHROMO)
                    # print("count increeeseddd+++++++")
                    popCount += 1
                print("   Population of Generation ", genCount, " => ",
                      POPULATION_TWO)
                # print("for is done-----------------")
            print("NEW POPULATION - ", POPULATION_TWO)
            INITIAL_POPULATION = copy.deepcopy(POPULATION_TWO)
            genCount += 1
        print("- - - - - - - - - - - - - - - - - ")
        print("-FINAL POPULATION- ", INITIAL_POPULATION)
        sortedFinalPop = sorted(
            INITIAL_POPULATION, key=lambda x: x[1], reverse=True)
        result = sortedFinalPop[0]
        print("- - - - - - - - - - - - - - - - - ")
        print("MOST FIT FINAL CHOROMOSOME => ", result)
        print("Total VALUE of the CHOROMOSOME => ", result[1],
              "Total WEIGHT of the CHOROMOSOME => ", result[2])

        repeatChoice = input(
            "Do you want to repeat the process with same variables? [y/n]: ")
        if repeatChoice == "n":
            repeat = False
        else:
            print("\n( ° ͜ʖ͡°)╭∩╮\n")
            input("Press Enter to Repeat!\n")

    restart = input("Do you want to restart the program? [y/n]: ")
    if restart == "n":
        done = True
        print("[{-_-}] ZZZzz zz z...")
    else:
        print("\n╭∩╮(Ο_Ο)╭∩╮")
        input("Press Enter to Start Over!\n")
