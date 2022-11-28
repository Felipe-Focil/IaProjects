from collections import deque
from heapq import heappop, heappush

# ...


class Q:
    def __init__(self, d):
        self.data = d

    def getData(self):
        return self.data


class PriorityQueue:
    def __init__(self):
        self.elements = []
        self.priority = dict()

    def PisDefined(self, v):
        if v in self.priority:
            self.priority[v] = self.priority[v]+1
            return(v + (self.priority[v] * 0.0001))
        else:
            self.priority[v] = 1
            return v

    def add(self, priority, value):
        priority = self.PisDefined(priority)
        heappush(self.elements, (priority, value))

    def pop(self):
        n = heappop(self.elements)

        return n[1]

    def show(self):
        print(self.elements)

    def getSize(self):
        return len(self.elements)

    def isEmpty(self):
        if self.getSize() == 0:
            return True
        return False

    def showPriority(self):
        print(self.priority)
