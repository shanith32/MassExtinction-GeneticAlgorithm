def main():
    f = open("dataset/low-dimensional/f1_l-d_kp_10_269", "r")
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
    return objects


if __name__ == "__main__":
    main()
