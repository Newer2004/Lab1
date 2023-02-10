import math


class Point(object):
    """Class to handle point in a 2 dimensions space"""

    def __init__(self, x, y):
        """
        :param x: the value on the X-axis
        :type x: float
        :param y: the value on the Y-axis
        :type y: float
        """
        self.x = x
        self.y = y


    def show(self):
        """
        :return: the coordinate of this point
        :rtype: a tuple of 2 elements (float, float)
        """
        return self.x, self.y


    def move(self, x, y):
        """
        :param x: the value to move on the X-axis
        :type x: float
        :param y: the value to move on the Y-axis
        :type y: float
        """
        self.x += x
        self.y += y


    def dist(self, pt):
        """
        :param pt: the point to compute the distance with
        :type pt: :class:`Point` object
        :return: the distance between this point ant pt
        :rtype: int
        """
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
p1 = Point(x1, y1)
p2 = Point(x2, y2)
print(p1.show())
print(p2.show())
a1=float(input())
b1=float(input())
p1.move(a1, b1)
print(p1.show())
print(p2.show())
print(p1.dist(p2))
