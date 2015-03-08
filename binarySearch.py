"""

Binary Array Search log(n)

"""

from performanceCalculator import PerformanceCalculator


def binarySearchContains(orderedList, target):
    low = 0
    high = len(orderedList) - 1
    while low <= high:
        mid = (high + low) // 2
        if target == orderedList[mid]:
            return mid
        elif target < orderedList[mid]:
            high = orderedList[mid] - 1
        else:
            low = orderedList[mid] + 1
    return -(low + 1)


def insertInPlace(orderedList, target):
    idx = binarySearchContains(orderedList, target)
    if idx < 0:
        orderedList.insert(-(idx + 1), target)
        return

    orderedList.insert(idx, target)

targetsToTest = {
    'insert': lambda x: x + 1,
    'search': lambda x: -1,
}


def doPerformanceTest(operation):
    calculator = PerformanceCalculator()
    calculator.calcPerformance(binarySearchContains, targetsToTest[operation])

print("Search Performance")
doPerformanceTest('search')

print()

"""

Results:
1024 0.00405311584473
2048 0.00309944152832
4096 0.00190734863281
8192 0.00286102294922
16384 0.00405311584473
32768 0.00405311584473
65536 0.00405311584473
131072 0.00500679016113
262144 0.00905990600586
524288 0.0109672546387
1048576 0.0121593475342
2097152 0.0121593475342
4194304 0.0121593475342
8388608 0.014066696167
16777216 0.0150203704834
33554432 0.0150203704834

"""
