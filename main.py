import numpy as np


def lettersLoad(file_name):
    f = open(file_name + ".txt", "r")
    lines = f.readlines()
    numbers = [[]]
    for line in lines:
        if line == "\n":
            numbers.append([])
        else:
            numbers[-1].append(line)
    patterns = []
    for array in numbers:
        result = []
        for item in array:
            temp = [int(num) for num in item.replace("\n", "").split(" ")]
            result += temp
        patterns.append(np.array([result]))
    return patterns


def distortedModuleRecognition():
    patterns = lettersLoad("letterList")
    M = N = len(patterns[0][0])
    resultWeight = np.array([[0 for y in range(M)] for x in range(N)])
    for pattern in patterns:
        resultWeight += np.matmul(pattern.T, pattern)
    for i in range(len(resultWeight)):
        resultWeight[i][i] = 0
    garbledPatterns = lettersLoad("garbledLetter")
    for pattern in garbledPatterns:
        prev = np.array(pattern).T
        next = np.matmul(resultWeight, prev)
        for i in range(len(next)):
            for j in range(len(next[0])):
                if next[i][j] > 1:
                    next[i][j] = 1
                if next[i][j] < -1:
                    next[i][j] = -1
        while not (next == prev).all():
            prev = next
            next = np.matmul(resultWeight, prev)
            for i in range(len(next)):
                for j in range(len(next[0])):
                    if next[i][j] > 1:
                        next[i][j] = 1
                    if next[i][j] < -1:
                        next[i][j] = -1
        print(next.reshape(5, 5))
        print("Pattern has been recognized")


distortedModuleRecognition()
