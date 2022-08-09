import sys

input = lambda: sys.stdin.readline().rstrip()
print = lambda x: sys.stdout.write(str(x) + "\n")


def getTable(pattern: str):
    patternSize = len(pattern)
    table = [0] * patternSize
    j = 0
    for i in range(1, patternSize):
        while (j > 0 and pattern[i] != pattern[j]):
            j = table[j - 1]

        if (pattern[i] == pattern[j]):
            j += 1
            table[i] = j
    return table


def kmp(parent: str, pattern: str):
    global cnt
    patternTable = getTable(pattern)
    parentSize = len(parent)
    patternSize = len(pattern)
    if (parentSize < patternSize): return

    j = 0
    for i in range(parentSize):
        while (j > 0 and parent[i] != pattern[j]):
            j = patternTable[j - 1]

        if (parent[i] == pattern[j]):
            if (j == patternSize - 1):
                cnt += 1
                subStringIndexTable.append(i - patternSize + 2)
                j = patternTable[j]
            else:
                j += 1



cnt = 0
subStringIndexTable = []
kmp(input(), input())
print(cnt)
for idx in subStringIndexTable:
    print(idx)

