import random
import math
import matplotlib.pyplot as plt
from statistics import mean


class GeneticAlgorithm:
    def __init__(self, size, a, b, precision, r, m, generations):
        self.n = self.getN(a, b, precision)
        self.size = size
        self.selectN = int((1 - r) * self.size)
        self.crossN = int((r * self.size) / 2)
        self.mutationN = int(m*self.size)
        self.generations = generations
        self.a = a
        self.b = b

    def getN(self, a, b, precision):
        n = b - a
        return int(math.ceil(math.log((n * pow(10, precision)) + 1, 2)))

    def generateInitialPopulation(self, n):
        self.P = list()
        for i in range(n):
            self.P.append(self.generateRandomNumber())

    def generateRandomNumber(self):
        s = ""
        for i in range(self.n):
            s += str(random.randint(0, 1))
        return s

    def fitness(self, x):
        return x * math.sin(10 * math.pi * x) + 1

    def to_binary(self, n):
        return str(bin(n))[2:]

    def to_int(self, h):
        v = ((self.b - self.a)/(pow(2, self.n) - 1))
        return self.a + (self.decimal(h) * v)

    def decimal(self, h):
        x = 0
        n = self.n - 1
        index = 0
        while n >= 0:
            v = int(h[index]) * pow(2, n)
            x = x + v
            index = index + 1
            n = n - 1
        return x

    def normalize(self):
        P = list()
        for x in self.P:
            P.append(self.to_int(x))
        return P

    def roullete(self):
        P = self.normalize()
        self.Roulette = list()
        sum = 0
        for x in P:
            sum = sum + self.fitness(x)
        prev = 0
        for x in P:
            y = (self.fitness(x)/sum)
            prev = prev + y
            self.Roulette.append(prev)

    def randomNumber(self):
        return random.uniform(0, 1)

    def spinRoulette(self):
        value = self.randomNumber()
        index = 0
        for x in self.Roulette:
            if value < x:
                return index
            index = index + 1

    def select(self):
        return self.P[self.spinRoulette()]

    def cross(self):
        a = self.select()
        b = self.select()
        crossPoint = random.randint(0, self.n - 1)
        return [self.joinString(a, b, crossPoint), self.joinString(b, a, crossPoint)]

    def joinString(self, a, b, n):
        return a[0:n] + b[n:self.n]

    def mutation(self, index):
        mutationPoint = int(random.randint(0, self.n - 1))
        s = list(self.P[index])

        if (s[mutationPoint] == '0'):
            s[mutationPoint] = '1'
        else:
            s[mutationPoint] = '0'

        self.P[index] = "".join(s)

    def list_to_int(self, lst):
        l = list()
        for x in lst:
            l.append(self.to_int(x))
        return l

    def run(self):
        self.mean = list()
        self.generateInitialPopulation(self.size)
        for i in range(self.generations):
            newP = list()
            ge.roullete()
            for j in range(self.selectN):
                newP.append(self.select())
            for j in range(self.crossN):
                newP.extend(self.cross())
            self.P = newP
            for j in range(self.mutationN):
                self.mutation(int(random.randint(0, self.size - 1)))

            self.mean.append(mean(self.list_to_int(self.P)))


ge = GeneticAlgorithm(5, -1, 2, 6, 0.4, 0.2, 1000)

ge.run()
plt.plot(ge.mean)
plt.ylabel("Maximum Number")
plt.xlabel("Generation")
plt.show()
