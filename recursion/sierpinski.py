import turtle


def drawTriangle(points, color, myTurtle):
    """根据三个点和颜色，画出填充颜色的三角形"""
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


def getMid(p1, p2):
    """求中点"""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow',
                'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0],getMid(points[0], points[1]),getMid(points[0], points[2])],degree - 1, myTurtle)
        sierpinski([getMid(points[0], points[1]), points[1],getMid(points[1], points[2])],degree - 1, myTurtle)
        sierpinski([getMid(points[0], points[2]),getMid(points[2], points[1]),points[2]],degree - 1, myTurtle)


def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-300, -150], [0, 300], [300, -150]]
    sierpinski(myPoints, 2, myTurtle)
    myWin.exitonclick()


main()
