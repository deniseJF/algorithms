from time import time


class PerformanceCalculator():

    def calcPerformance(self, functionToTest, targetOperation):
        n = 1024
        while n < 50000000:
            exampleList = list(range(n))

            now = time()

            functionToTest(exampleList, targetOperation(n))
            done = time()
            self.printPerformance(now, done)
            n *= 2

    def printPerformance(self, now, done):
        print((done - now) * 1000)
