from ast import And
import numpy as np
import Board as bd
import Point as p
from PQ import PriorityQueue


class Search:

    def __init__(self, board):
        self.board = board

    # Breadth First Search || Busqueda en Anchura
    def BFS(self, start, goal):
        queue = []  # Cola
        found = False
        queue.append(start)

        while np.size(queue) != 0 and not found:
            n = queue.pop(0)
            # Encontramos el objetivo?
            if self.board.comparePoints(n, goal):
                found = True
                break
            # Por cada posible sucesor
            sucesors = self.board.Sucesors(n)
            for sucesor in sucesors:

                # No es un obstaculo, no ha sido visitado y no es el inicio
                if self.board.getValue(sucesor) != '#' and not self.board.isVisited(sucesor) and not self.board.comparePoints(sucesor, start):
                    # Marcalo como visitado
                    self.board.markVisited(sucesor)
                    # Marca quien es su padre
                    self.board.markParent(
                        n, sucesor, self.board.path[n.y][n.x].t)
                    # Encontramos el objetivo ?
                    if self.board.comparePoints(sucesor, goal):
                        found = True
                        break
                        # Agregalo a la Cola
                    queue.append(sucesor)
        return found

    # Depth First Search || Busqueda en Profundidad

    def DFS(self, start, goal):
        stack = []  # Pila
        found = False

        stack.append(start)

        while np.size(stack) != 0 and not found:
            n = stack.pop()

            # Si no es el inicio marcalo como visitado
            if not self.board.comparePoints(n, start):
                self.board.markVisited(n)
            # Encontramos el objetivo?
            if self.board.comparePoints(n, goal):
                found = True
                break
            # Por cada posible sucesor
            sucesors = self.board.Sucesors(n)
            for sucesor in sucesors:

                # No es un obstaculo, no ha sido visitado y no es el inicio
                if self.board.getValue(sucesor) != '#' and not self.board.isVisited(sucesor) and not self.board.comparePoints(sucesor, start) and sucesor not in stack:
                    # Marcalo como visitado
                    self.board.markVisited(sucesor)
                    # Marca quien es su padre
                    self.board.markParent(
                        n, sucesor, self.board.path[n.y][n.x].t)
                    # Encontramos el objetivo ?
                    if self.board.comparePoints(sucesor, goal):
                        found = True
                        break
                        # Agregalo a la Cola
                    stack.append(sucesor)

        return found
    # Hill Climbing Search || Busqueda de Escalada de Colina

    def Hill(self, start, goal):
        self.board.markVisited(start)
        min = start
        minW = self.board.n * self.board.m
        sucesors = self.board.Sucesors(start)

        while True:
            candidates = 0

            for i in sucesors:
                w = self.board.board[i.y][i.x].w

                if w == 0:
                    self.board.markVisited(i)
                    return True

                if w < minW and self.board.getValue(i) != "#" and not self.board.isVisited(i):
                    self.board.markVisited(i)
                    candidates = candidates + 1
                    min = i
                    minW = w

            sucesors = self.board.Sucesors(min)

            if candidates == 0:
                return False
            min.w = self.board.n * self.board.m
    # Best First Search || Busqueda del Mejor Primero

    def BestFS(self, start, goal):
        queue = PriorityQueue()
        found = False
        self.board.markVisited(start)
        queue.add(self.board.board[start.y][start.x].w, start)

        while not queue.isEmpty():
            n = queue.pop()
            self.board.markVisited(n)

            sucesors = self.board.Sucesors(n)
            for sucesor in sucesors:
                if self.board.getValue(sucesor) != '#' and not self.board.isVisited(sucesor) and not self.board.comparePoints(sucesor, start):
                    # Encontramos el objetivo ?
                    if self.board.comparePoints(sucesor, goal):
                        self.board.markVisited(goal)
                        return True
                    # Agregalo a la Cola
                    w = self.board.board[sucesor.y][sucesor.x].w
                    queue.add(w, sucesor)
        return found
    # A* Search || Busqueda en A*

    def A(self, start, goal):
        queue = PriorityQueue()
        found = False
        self.board.markVisited(start)
        queue.add(self.board.board[start.y][start.x].w, start)

        while not queue.isEmpty():
            n = queue.pop()
            self.board.markVisited(n)

            sucesors = self.board.Sucesors(n)
            for sucesor in sucesors:
                if self.board.getValue(sucesor) != '#' and not self.board.isVisited(sucesor) and not self.board.comparePoints(sucesor, start):

                    self.board.markParent(
                        n, sucesor, self.board.path[n.y][n.x].t)

                    # Encontramos el objetivo ?
                    if self.board.comparePoints(sucesor, goal):
                        self.board.markVisited(goal)
                        return True
                    # Agregalo a la Cola
                    w = self.board.board[sucesor.y][sucesor.x].w
                    print(w + self.board.path[n.y][n.x].t)
                    queue.add(w + self.board.path[n.y][n.x].t, sucesor)
        return found
