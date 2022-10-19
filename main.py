from astar import Astar
from puzzle import Puzzle


def main():
    """
    Main function
    """
    # Determines usable puzzle size by user input
    puzzleSize = 0
    puzzleSizeList = [8, 15, 24]
    while puzzleSize not in puzzleSizeList:
        puzzleSize = int(
            input("Enter puzzle size (8-puzzle, 15 puzzle, 24 puzzle): "))

    result_steps3 = []
    result_nodecount3 = []
    # Test h3
    
    """puzzle = Puzzle(puzzleSize, True)
    a = Astar(puzzle, 0)
    print(puzzle)
    steps, nc = a.solve3()
    result_steps3.append(steps-1)
    result_nodecount3.append(nc)"""

    # test h1,h2,h3
    result_steps2 = []
    result_nodecount2 = []
    result_steps1 = []
    result_nodecount1 = []
    for x in range(100):
        print("Progress: {}%".format(int((x / 100) * 100)))
        puzzle = Puzzle(puzzleSize, True)
        print(puzzle)
        a = Astar(puzzle, 0)
        steps, nc = a.solve1()
        result_steps1.append(steps - 1)
        result_nodecount1.append(nc)
        steps, nc = a.solve2()
        result_steps2.append(steps - 1)
        result_nodecount2.append(nc)
        steps, nc = a.solve3()
        result_steps3.append(steps - 1)
        result_nodecount3.append(nc)
    
    print("h1: steps, nodes")
    print(result_steps1)
    print(result_nodecount1)
    print("h2: steps, nodes")
    print(result_steps2)
    print(result_nodecount2)
    print("h3: steps, nodes")
    print(result_steps3)
    print(result_nodecount3)


main()
