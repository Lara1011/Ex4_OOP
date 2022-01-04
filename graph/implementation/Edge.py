class Edge:

    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def getSrc(self):
        return self.src

    def setSrc(self, src):
        self.src = src

    def getDest(self):
        return self.dest

    def setDest(self, dest):
        self.dest = dest

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight
