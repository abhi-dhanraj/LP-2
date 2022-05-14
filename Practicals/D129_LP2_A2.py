import turtle
import time
import random
from PIL import Image

wn = turtle.Screen()
wn.title("Turtle and grass")
wn.setup(width=600, height=600)


class Cell:
    def __init__(self, x, y):
        self.parent = None
        self.x, self.y = x, y
        self.g_cost, self.h_cost, self.f_cost = 0, 0, 0
        self.neighbors = []
        for i in [-5, 0, 5]:
            for j in [-5, 0, 5]:
                if i == j == 0:
                    continue
                self.neighbors.append([x + i, y + j])

    def set_cost(self, prev, goal):
        self.g_cost = prev.g_cost + \
            int((((self.x - prev.x) ** 2 + (self.y - prev.y) ** 2) ** 0.5) * 10)
        self.h_cost = int(
            (((self.x - goal[0]) ** 2 + (self.y - goal[1]) ** 2) ** 0.5) * 10)
        self.f_cost = self.g_cost + self.h_cost


class Navigator:
    def __init__(self):
        self.mover = turtle.Turtle()
        self.mover.pencolor("brown")
        self.positions = []
        self.mover.shape('turtle')
        self.mover.fillcolor('brown')
        self.img = Image.open('bgpic.png')
        self.grass = Image.open('grass.png')

    def move(self, x, y):
        self.mover.goto(x, y)
        time.sleep(0.1)

    def reach(self):
        while self.positions:
            x, y = self.positions.pop()
            self.move(x, y)

    def a_star_nav(self, start, goal):
        self.positions = []
        if self.obstacles_bool(goal[0], goal[1]) or self.obstacles_bool(start.x, start.y):
            print("No way")
            return
        open = []
        closed = []
        open.append(start)

        while True:
            m = 0
            for i in range(len(open)):
                if open[i].f_cost < open[m].f_cost:
                    m = i
                elif open[i].f_cost == open[m].f_cost and open[i].h_cost < open[m].h_cost:
                    m = i
            curr = open.pop(m)
            closed.append(curr)

            if curr.x == goal[0] and curr.y == goal[1]:
                # print(curr.x, curr.y, curr.g_cost, curr.h_cost, curr.f_cost)
                self.positions.append([curr.x, curr.y])
                curr = curr.parent
                while curr.parent:
                    # print(curr.x, curr.y, curr.g_cost, curr.h_cost, curr.f_cost)
                    self.positions.append([curr.x, curr.y])
                    curr = curr.parent
                return self.reach()

            for pos in curr.neighbors:
                nbr = Cell(pos[0], pos[1])
                if self.obstacles_bool(pos[0], pos[1]):
                    continue
                for i in closed:
                    if nbr.x == i.x and nbr.y == i.y:
                        break
                else:
                    nbr.set_cost(curr, goal)

                    for i in open:
                        if nbr.x == i.x and nbr.y == i.y:
                            if nbr.g_cost < i.g_cost:
                                i.g_cost = nbr.g_cost
                                i.f_cost = nbr.f_cost
                                i.parent = curr
                            break
                    else:
                        nbr.parent = curr
                        open.append(nbr)

    def obstacles_bool(self, x, y):
        return self.img.getpixel((300+x, 300-y)) != (128, 255, 255)


img = Image.open('bgpic.png')
grass = Image.open('grass.png')
x, y = random.randint(-45, 45) * 5, random.randint(-45, 45) * 5
print(x, y)
img.paste(grass, (300+x, 300-y-15))
img.save("bgpic2.png")
time.sleep(1)
wn.bgpic('bgpic2.png')
jerry = Navigator()
jerry.a_star_nav(Cell(0, 0), [x, y])
while True:
    if input():
        break
'''
-200 -120
'''
