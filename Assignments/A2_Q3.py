def find_triplets(X, Y, Z, target):
    for i in X:
        for j in Y:
            for k in Z:
                if i + j + k == target:
                    print(f"Triplet is {i}, {j}, {k}")

X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70

find_triplets(X, Y, Z, target)