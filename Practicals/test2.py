import copy


class Node:

    def __init__(self, data, level, f_score):
        self.data = data
        self.level = level
        self.f_score = f_score

    def shuffle(self, puzzle, x0, x1, y0, y1):
        if x1 >= 0 and x1 < len(self.data) and y1 >= 0 and y1 < len(self.data):
            new_puzzle = copy.deepcopy(puzzle)
            new_puzzle[x0][y0], new_puzzle[x1][y1] = new_puzzle[x1][y1], new_puzzle[x0][y0]
            return new_puzzle
        return None

    def find_tile(self, puzzle, tile):
        for x in range(len(self.data)):
            for y in range(len(self.data)):
                if puzzle[x][y] == tile:
                    return [x, y]

    def create_childrens(self):
        x, y = self.find_tile(self.data, '_')
        pos_lst = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
        childrens = []
        for pos in pos_lst:
            child = self.shuffle(self.data, x, y, pos[0], pos[1])
            if child is not None:
                child_node = Node(child, self.level+1, 0)
                childrens.append(child_node)
        return childrens


class Puzzle:

    def __init__(self, sz):
        self.size = sz
        self.open = []
        self.closed = []

    def read_input(self):
        puzzle = []
        for i in range(self.size):
            puzzle.append(input().split(" "))
        return puzzle

    def find_pos(self, val, goal):
        for i in range(self.size):
            for j in range(self.size):
                if goal[i][j] == val:
                    return [i, j]

    def cal_hscore(self, start, goal):
        hscore = 0
        for i in range(self.size):
            for j in range(self.size):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    x, y = self.find_pos(start[i][j], goal)
                    hscore += abs(i-x)+abs(j-y)
        return hscore

    def cal_fscore(self, start, goal):
        fscore = self.cal_hscore(start.data, goal)
        return fscore

    def astar(self):
        print("Enter the Initial State Puzzle :")
        start = self.read_input()
        print("\nEnter the Goal State Puzzle :")
        goal = self.read_input()

        start = Node(start, 0, 0)
        start.f_score = self.cal_fscore(start, goal)
        self.open.append(start)

        print("\nExecution Started")
        print()

        while self.open:
            curr = self.open[0]
            for row in curr.data:
                for tile in row:
                    print(tile, end=' ')
                print()

            print("   |   ")
            print("   V   ")

            if self.cal_hscore(curr.data, goal) == 0:
                break

            for child in curr.create_childrens():
                child.fscore = self.cal_fscore(child, goal)
                include_child = True
                for c in self.open:
                    if c.data == child.data and c.f_score < child.f_score:
                        include_child = False
                        break
                for c in self.closed:
                    if c.data == child.data and c.f_score < child.f_score:
                        include_child = False
                        break

                if include_child:
                    self.open.append(child)

            self.closed.append(curr)
            del self.open[0]
            self.open.sort(key=lambda x: x.f_score)


P = Puzzle(3)
P.astar()
print("Execution Over!!")
