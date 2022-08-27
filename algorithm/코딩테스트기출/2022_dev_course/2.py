import sys
from collections import defaultdict


# 같은 숫자가 중복해서 들어있지 않음
def solution(cardList: list, wordList: list):
    answer = []
    for word in wordList:
        if (isPromising(cardList, word)):
            if (isPossible(cardList, word)):
                answer.append(word)
    if (not answer): return ["-1"]
    return answer


def isPromising(cardList: list, word: str):
    mDict = defaultdict(int)
    # O(24)
    for card in cardList:
        for chr in card:
            mDict[chr] += 1

    for chr in word:
        if (not mDict[chr]):
            return False
        mDict[chr] -= 1

    return True


def isPossible(cardList: list, word: str):
    flag1 = False
    flag2 = False
    flag3 = False
    mDict1 = defaultdict(int)
    mDict2 = defaultdict(int)
    mDict3 = defaultdict(int)

    for chr in cardList[0]:
        mDict1[chr] += 1
    for chr in cardList[1]:
        mDict2[chr] += 1
    for chr in cardList[2]:
        mDict3[chr] += 1

    for chr in word:
        if (mDict1[chr]):
            flag1 = True
        elif (mDict2[chr]):
            flag2 = True
        elif (mDict3[chr]):
            flag3 = True

    if (flag1 and flag2 and flag3):
        return True
    return False