import turtle

def tree(brachLen,t):
    if brachLen>5:
        t.color("blue")
        t.forward(brachLen)
        t.right(30)
        tree(brachLen-15,t)
        t.left(60)
        t.color("red")
        tree(brachLen-15,t)
        t.right(30)
        t.color("green")
        t.backward(brachLen)


def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    # 笔的颜色
    myTurtle.pensize(1)
    # 笔的速度
    myTurtle.speed(1)
    # 调初始位置
    myTurtle.left(90)
    myTurtle.up()
    myTurtle.backward(100)
    myTurtle.down()
    # 画树
    tree(100,myTurtle)
    myWin.exitonclick()


main()
