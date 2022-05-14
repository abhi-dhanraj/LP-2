import copy


class Node:
    def __init__(self, data, level, f_score):
        self.data = data
        self.level = level
        self.f_score = f_score

    def shuffle(self, puzzle, x0, y0, x1, y1):
        if x1 >= 0 and x1 < len(self.data) and y1 >= 0 and y1 < len(self.data):
            new_puzzle = copy.deepcopy(puzzle)
            new_puzzle[x0][y0], new_puzzle[x1][y1] = new_puzzle[x1][y1], new_puzzle[x0][y0]
            return new_puzzle
        return None

    def find_tile(self, puzzle, tile):
        for x in range(len(self.data)):
            for y in range(len(self.data)):
                if puzzle[x][y] == tile:
                    return x, y

    def create_child(self):
        x, y = self.find_tile(self.data, '_')
        pos_list = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
        children = []
        for pos in pos_list:
            child = self.shuffle(self.data, x, y, pos[0], pos[1])
            if child is not None:
                child_node = Node(child, self.level+1, 0)
                children.append(child_node)
        return children


class Puzzle:
    def __init__(self, size):
        self.size = size
        self.open = []
        self.closed = []

    def read_puzzle(self):
        puzzle = []
        for i in range(self.size):
            row = input().split(" ")
            puzzle.append(row)
        return puzzle

    def is_solvable(self, puzzle):
        lst = [j for row in puzzle for j in row]
        inv_cnt = 0
        for i in range(self.size):
            for j in range(i+1, self.size):
                if lst[j] != '_' and lst[i] != '_' and lst[i] > lst[j]:
                    inv_cnt += 1
        if inv_cnt % 2 == 0:
            return True
        return False

    def find_pos(self, val, goal):
        for x in range(self.size):
            for y in range(self.size):
                if goal[x][y] == val:
                    return x, y

    def calc_h_score(self, start, goal):
        h_score = 0
        for i in range(self.size):
            for j in range(self.size):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    x, y = self.find_pos(start[i][j], goal)
                    h_score += abs(i-x) + abs(j-y)
        return h_score

    def calc_f_score(self, start, goal):
        f_score = self.calc_h_score(start.data, goal) + start.level
        return f_score

    def process(self):
        print("Enter the Initial State Puzzle :")
        start = self.read_puzzle()
        print("\nEnter the Goal State Puzzle :")
        goal = self.read_puzzle()

        start = Node(start, 0, 0)
        start.f_score = self.calc_f_score(start, goal)
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

            if(self.calc_h_score(curr.data, goal) == 0):
                break

            for child in curr.create_child():
                child.f_score = self.calc_f_score(child, goal)
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
P.process()
print("Execution Over!!")

'''
1 8 7
_ 2 3
5 4 6
1 2 3
4 5 6
7 8 _
'''
