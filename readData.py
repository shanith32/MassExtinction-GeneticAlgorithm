def main():
    f = open("dataset/low-dimensional/f10_l-d_kp_20_879", "r")
    capacity = 879
    data = f.readlines()
    count = len(data)-1
    objects = []  # Set of objects that we will used as the dataset for the programs
    for i in range(count):
        v, w = map(int, data[i].split())
        obj = [] * 3  # object set with the properties - [value, weight, id]
        obj.append(v)
        obj.append(w)
        obj.append(i)
        objects.append(obj)
    return objects, capacity


if __name__ == "__main__":
    main()
