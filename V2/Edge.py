

EdgeWeights = set(["LT", "LM","LB","MT","MB","RT","RM","RB"])

class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight

