class Point:
    def __init__(self, x, y, t):
        self.sucesor = list()
        self.x = x
        self.y = y
        self.t = 0
        self.w = -1
        self.val = '.'

    def isDefinedUp(self):  # ¿Esta definido arriba?
        if self.y - 1 >= 0:
            return True
        return False

    def isDefinedDown(self, n):  # ¿Esta definido abajo?
        if self.y + 1 < n:
            return True
        return False

    def isDefinedLeft(self):  # ¿Esta definido a la izquierda?
        if self.x - 1 >= 0:
            return True
        return False

    def isDefinedRight(self, m):  # ¿Esta definido derecha?
        if self.x + 1 < m:
            return True
        return False

    def Up(self):
        if self.isDefinedUp():  # Si esta definido
            p = Point(self.x, self.y - 1, self.t)
            self.sucesor.append(p)

    def Down(self, n):  # Si esta definido
        if self.isDefinedDown(n):
            p = Point(self.x, self.y + 1, self.t)
            self.sucesor.append(p)

    def Left(self):
        if self.isDefinedLeft():  # Si esta definido
            p = Point(self.x-1, self.y, self.t)
            self.sucesor.append(p)

    def Right(self, n):
        if self.isDefinedRight(n):  # Si esta definido
            p = Point(self.x + 1, self.y, self.t)
            self.sucesor.append(p)

    def show(self):
        print("(" + str(self.x) + "," + str(self.y) + ")", end=" -> ")

    def toString(self):
        s = "(" + str(self.x) + "," + str(self.y) + ")"
        return s

    def updateVal(self, c):
        self.val = c

    def comparePoints(self, a, b):
        if a.x is b.x and a.y is b.y:
            return True
        return False

    def setW(self, d):
        self.w = d

    def getW(self):
        return self.w
    """
    def setW(self, u, w):
        found = False
        if self.sucesor is not None:
            for i in range(0, len(self.sucesor)):
                if self.comparePoints(self.sucesor[i], u):
                    self.sucesor[i].w = w
                    return self.sucesor
            if not found:
                p = Point(u.x, u.y, u.t)
                p.w = w
                self.sucesor.append(u)
    """
