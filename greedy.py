# Heuristic Greedy algorithm to deal with the Knapsack problem

data = [[4, 2, 0], [5, 2, 1], [7, 11, 2],
        [7, 11, 3]]  # object set with the properties - [value, weight, id]

container = []  # the container to contain the objects in
capacity = 10  # weight capacity of the container
solution = [0] * len(data)  # binary representation of the soultion

ratios = []  # an array to store the ratios of each object
count = 0  # a count to track the weights of objects before adding them to the container

# For loop to get the ratios of value/weight and add the ratios of each object to the container
for i in range(len(data)):
    ratio = data[i][0] / data[i][1]
    ratios.append([ratio, data[i][2]])

print(data)
print(ratios)
# Sort the resulting ratios in decending order
decreasing = sorted(ratios, key=lambda x: x[0], reverse=True)
print(decreasing)

# For loop to add the objects to the container without exceeding the capacity of the container
for i in range(len(decreasing)):
    for j in range(len(data)):
        if (decreasing[i][1] == data[j][2]):
            if (data[j][1] <= capacity):
                if (count + data[j][1] <= capacity):
                    count = count + data[j][1]
                    container.append(data[j])
                    index = data[j][2]
                    solution[index] = 1

print("\nWeights", count)
print("Here's the resulting container: ", container)
print("\nBinary string representation of the soultion: ", solution)

CHROMO = [] * 3  # [[binary soultion], fitness, total weight]
fitness = 0
totalWeight = 0
for j in range(len(solution)):
    if (solution[j] == 1):
        fitness += data[j][0]
        totalWeight += data[j][1]
CHROMO.append(solution)
CHROMO.append(fitness)
CHROMO.append(totalWeight)
print("!!result!!:", CHROMO)
print("Total value of the soultion:", CHROMO[1],
      "Total weight of the soultion:", CHROMO[2])
