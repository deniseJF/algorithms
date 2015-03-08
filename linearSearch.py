"""

Linear Search (n)
When we double the size of the array,
also doubles the time to search in the array

"""

from performanceCalculator import PerformanceCalculator


# 'in' has linear performance in python 2.x,
# it searches through each element of the array
def contains(collection, target):
    return target in collection


def insertInPlace(collection, target):
    for i in range(len(collection)):
        if target < collection[i]:
            collection.insert(i, target)
            return i


targetsToTest = {
    'insert': {
        'target': lambda x: x + 1,
        'operation': insertInPlace
    },
    'search': {
        'target': lambda x: -1,
        'operation': contains
    }
}


def doPerformanceTest(operation):
    calculator = PerformanceCalculator()
    calculator.calcPerformance(targetsToTest[operation]['operation'],
                               targetsToTest[operation]['target'])

print("Search Performance")
doPerformanceTest('search')

print()

print("Insert Performance")
doPerformanceTest('insert')


"""

Results:

Search Performance
0.01049041748046875
0.026941299438476562
0.06341934204101562
0.12612342834472656
0.15306472778320312
0.31256675720214844
0.6253719329833984
1.2521743774414062
2.4437904357910156
5.123138427734375
10.074615478515625
19.748926162719727
39.861202239990234
80.1076889038086
162.6894474029541
322.68786430358887

Insert Performance
0.013828277587890625
0.02384185791015625
0.047206878662109375
0.0934600830078125
0.1862049102783203
0.37217140197753906
0.7429122924804688
1.508474349975586
3.0803680419921875
6.144285202026367
12.254714965820312
25.007247924804688
48.69532585144043
97.20396995544434
195.61338424682617
392.6997184753418

"""
