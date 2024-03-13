def isSorted(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True

numProblems = int(input())
difficulties = [int(input()) for i in range(numProblems)]
smthPrinted = False

for i in range(2, numProblems + 1):
    if numProblems % i == 0:
        groupSize = int(numProblems / i)
        arr = []

        for x in range(0, numProblems, groupSize):
            arr.append(min(difficulties[x:x + groupSize]))
            arr.append(max(difficulties[x:x + groupSize]))

        if isSorted(arr):
            smthPrinted = True
            print(i)

if not smthPrinted:
    print(-1)