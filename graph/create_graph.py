class Vertex:
    """建立一个顶点"""

    def __init__(self, key):
        """自身属性为：键值，和相邻顶点构成的字典"""
        self.id = key
        self.connectedTo = {}
        self.distance = 0
        self.predecessor = None
        self.color = 'white'

    def addNeighbor(self, nbr, weight=0):
        """连接到的顶点和对应的权值构成值对，添加进字典"""
        self.connectedTo[nbr] = weight

    def __str__(self):
        """内置方法，可以让实例直接调用print"""
        return str(self.id) + 'connectedTo:' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """返回所有相邻的顶点"""
        return self.connectedTo.keys()

    def getId(self):
        """返回顶点自身键值"""
        return self.id

    def getWeight(self, nbr):
        """返回某个相邻顶点的权值"""
        return self.connectedTo[nbr]

    def setDistance(self,d):
        """设定该顶点距离某顶点的距离"""
        self.distance=d

    def getDistance(self):
        """返回当前距离"""
        return self.distance

    def setPred(self,n):
        """设定前驱结点"""
        self.predecessor=n

    def getPred(self):
        """返回前驱结点"""
        return self.predecessor

    def setColor(self,cl):
        """设定颜色"""
        self.color=cl

    def getColor(self):
        """返回颜色"""
        return self.color


class Graph:
    """建立一个图"""

    def __init__(self):
        """自身属性为：顶点数量，和所有顶点构成的字典"""
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        """赋予新顶点键值，并将键值与新顶点构成值对，添加进字典，并返回新顶点"""
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        """返回某键值对应的顶点"""
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        """内置方法，返回某键值是否存在"""
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        """添加f到t的一条边"""
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        """返回所有顶点的键值"""
        return self.vertList.keys()

    def __iter__(self):
        """将所有顶点生成为一个迭代器"""
        return iter(self.vertList.values())

