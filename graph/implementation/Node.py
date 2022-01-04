class Node:

    def __init__(self, id, x, y, z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.in_ = dict()
        self.out_ = dict()

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getx(self):
        if (self.x == None):
            return -1
        return self.x

    def setx(self, x):
        self.x = x

    def gety(self):
        if (self.y == None):
            return -1
        return self.y

    def sety(self, y):
        self.y = y

    def getz(self):
        if (self.z == None):
            return -1
        return self.z

    def setz(self, z):
        self.z = z

    def getIn(self):
        return self.in_

    def getOut(self):
        return self.out_

    def __repr__(self):
        return f"{self.id}: |edges_out| {len(self.out_)} |edges in| {len(self.in_)}"
