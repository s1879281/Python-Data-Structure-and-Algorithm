def movedisk(from_tower, to_tower):
    # 移盘子
    print("move disk from " + from_tower + " to " + to_tower)

def movetower(number_disk, tower_1, tower_2, tower_3):
    """汉诺塔递归程序"""
    if number_disk >=1:
        movetower(number_disk - 1, tower_1, tower_3, tower_2)
        movedisk(tower_1,tower_3)
        movetower(number_disk - 1, tower_2, tower_1, tower_3)


movetower(3, "tower_1", "tower_2", "tower_3")
