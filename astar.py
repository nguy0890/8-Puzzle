import heapq

from puzzle import Puzzle


class Astar:

    def __init__(self, puzzle, g):
        self.puzzle = puzzle
        self.parent = None
        self.g = g
        self.f = 0
        self.f1 = self.puzzle.h1 + self.g
        self.f2 = self.puzzle.h2 + self.g
        self.f3 = self.puzzle.h3 + self.g

    def set_f(self):
        """
        return estimated total cost
        of cheapest solution for h1
        """
        self.f1 = self.puzzle.h1 + self.g
        self.f2 = self.puzzle.h2 + self.g
        self.f3 = self.puzzle.h3 + self.g
        return

    def set_f2(self):
        self.f2 = self.puzzle.h2 + self.g
        self.f = self.f2
        return

    def set_f1(self):
        self.f1 = self.puzzle.h1 + self.g
        self.f = self.f1
        return

    def set_f3(self):
        self.f3 = self.puzzle.h3 + self.g
        self.f = self.f3
        return

    def findzero(self, puzzle):
        for i in range(puzzle.size):
            for j in range(puzzle.size):
                if (puzzle.board[i][j] == 0):
                    return i, j

    def solve1(self):
        pqueue = []
        seen = set()
        nodecount = 0
        g = 0
        self.f = self.puzzle.h1 + self.g
        heapq.heappush(pqueue, self)
        seen.add(hash(str(self.puzzle.board)))
        while True:
            # evaluates node in priority queue with smallest f case
            node = heapq.heappop(pqueue)
            g = node.g + 1
            x, y = self.findzero(node.puzzle)
            coords = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
            for i in coords:
                new_puzzle = Puzzle.moves(node.puzzle, x, y, i[0], i[1])
                if new_puzzle:
                    new_puzzle.set_h1()
                    if new_puzzle.h1 == 0:
                        child = Astar(new_puzzle, g)
                        child.parent = node
                        node = child
                        break
                    puz = hash(str(new_puzzle.board))
                    if (puz not in seen):  # fix, NEVER NOT IN SEEN
                        nodecount += 1
                        seen.add(puz)
                        child = Astar(new_puzzle, g)  # create child
                        child.parent = node
                        child.set_f1()
                        heapq.heappush(pqueue, child)  # add to queue

            # sort queue
            if (node.puzzle.h1 == 0):
                route = []
                # print("\n")
                # print("ROUTE:\n")
                steps = 0
                while node is not None:
                    route.append(node)
                    node = node.parent
                    steps += 1
                # route.reverse()
                # print("Number of steps: ")
                # print(steps)
                # for state in route:
                    # print(state.puzzle)
                break
        return steps, nodecount

    def solve2(self):
        pqueue = []
        seen = set()
        nodecount = 0
        g = 0
        self.f = self.puzzle.h2 + self.g
        heapq.heappush(pqueue, self)
        seen.add(hash(str(self.puzzle.board)))
        while True:
            # evaluates node in priority queue with smallest f case
            node = heapq.heappop(pqueue)
            g = node.g + 1
            x, y = self.findzero(node.puzzle)
            coords = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
            for i in coords:
                new_puzzle = Puzzle.moves(node.puzzle, x, y, i[0], i[1])
                if new_puzzle:
                    new_puzzle.set_h2()
                    if new_puzzle.h2 == 0:
                        child = Astar(new_puzzle, g)
                        child.parent = node
                        node = child
                        break
                    puz = hash(str(new_puzzle.board))
                    if (puz not in seen):  # fix, NEVER NOT IN SEEN
                        nodecount += 1
                        seen.add(puz)
                        child = Astar(new_puzzle, g)  # create child
                        child.parent = node
                        child.set_f2()
                        heapq.heappush(pqueue, child)  # add to queue

            # sort queue
            if (node.puzzle.h2 == 0):
                route = []
                # print("\n")
                # print("ROUTE:\n")
                steps = 0
                while node is not None:
                    route.append(node)
                    node = node.parent
                    steps += 1
                # route.reverse()
                # print("Number of steps: ")
                # print(steps)
                # for state in route:
                    # print(state.puzzle)
                break
        return steps, nodecount

    def solve3(self):
        pqueue = []
        seen = set()
        nodecount = 0
        g = 0
        self.f = self.puzzle.h3 + self.g
        heapq.heappush(pqueue, self)
        seen.add(hash(str(self.puzzle.board)))
        while True:
            # evaluates node in priority queue with smallest f case
            node = heapq.heappop(pqueue)
            g = node.g + 1
            x, y = self.findzero(node.puzzle)
            coords = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
            for i in coords:
                new_puzzle = Puzzle.moves(node.puzzle, x, y, i[0], i[1])
                if new_puzzle:
                    new_puzzle.set_h3()
                    if new_puzzle.h3 == 0:
                        child = Astar(new_puzzle, g)
                        child.parent = node
                        node = child
                        break
                    puz = hash(str(new_puzzle.board))
                    if (puz not in seen):  # fix, NEVER NOT IN SEEN
                        nodecount += 1
                        seen.add(puz)
                        child = Astar(new_puzzle, g)  # create child
                        child.parent = node
                        child.set_f3()
                        heapq.heappush(pqueue, child)  # add to queue

            # sort queue
            if (node.puzzle.h3 == 0):
                route = []
                # print("\n")
                # print("ROUTE:\n")
                steps = 0
                while node is not None:
                    route.append(node)
                    node = node.parent
                    steps += 1
                # route.reverse()
                # print("Number of steps: ")
                # print(steps)
                # for state in route:
                    # print(state.puzzle)
                break
        return steps, nodecount

    def __lt__(self, other):
        return self.f < other.f
