from create_queue import Queue


def hotPotato(namelist, num):
    """烫手的山芋问题"""
    queue = Queue()

    for name in namelist:
        queue.enqueue(name)

    # 从队首开始传递，队首传递后去队尾，传递num次后队首死亡，游戏继续
    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())

        print(queue.dequeue())

    # 返回最后剩下的人
    return queue.dequeue()


print(hotPotato(['A', 'B', 'C', 'D', 'E'], 2))
