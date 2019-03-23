from create_graph import Graph
from create_queue import Queue


def bfs(start):
    """广度优先算法"""
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)

    while (vertQueue.size() > 0):
        # 队列不为空时，继续循环
        currentVert = vertQueue.dequeue()

        # 遍历每一个连接的顶点，未遍历的白色顶点标记为灰色并进队列
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)

        # 所有连接的结点遍历完后，结点变为黑色
        currentVert.setColor('black')
        print(currentVert.getId())


g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)

g.addEdge(2, 3, 10)
g.addEdge(2, 5, 10)
g.addEdge(5, 9, 10)
g.addEdge(9, 6, 10)
g.addEdge(6, 4, 10)

bfs(g.getVertex(2))

