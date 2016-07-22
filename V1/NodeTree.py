class Tree:
    identity = None
    children = []

    def nChildren(self):
        len(children)

    def addChild(self, child):
        self.children.append(child)

    # Find the parent node and add the child.
    def addChildToNode(self, parent, child):
        found = False

        for chld in self.children:
            # If we found the child that is the parent being added to.
            if chld.identity == parent.identity:
                chld.addChild(child)
                found = True
                break

        if not found:
            # None of our children are the parent. Search our childrent's
            # children for the parent of this orphan child.
            for chld in children:
                self.addChildToNode(chld, child)

    def __init__(self,ident):
        self.setI(ident)

    def setI(self, ident):
        self.identity = ident

class Node:

    def __init__(self,ident):
        self.identity = None
        self.setI(ident)
        self.children = []

    def setI(self, ident):
        self.identity = ident

    def addChild(self, child):
        self.children.append(Node(child))

    def append( self , child):
        self.children.append(child)