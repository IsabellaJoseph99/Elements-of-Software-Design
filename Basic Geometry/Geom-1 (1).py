#!/usr/bin/env python
# coding: utf-8

# In[59]:


#  File: Geom.py

#  Description: A program that looks at different points, circles and rectangles

#  Student Name: Isabella Joseph

#  Student UT EID: ij2799

#  Partner Name: Kaitlyn Ng

#  Partner UT EID: kn8685

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/20/2019

#  Date Last Modified: 9/20/2019

import math

class Point(object):
    # constructor
    # x and y are floats
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance
    # other is a Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    # takes no arguments
    # returns a string
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Circle(object):
    # constructor
    # x, y, and radius are floats
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        self.center = Point(x, y)

    # compute cirumference
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area(self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside(self, p):
        return (self.center.dist(p) < self.radius)

    # determine if a circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c overlaps this circle (non-zero area of overlap)
    # but neither is completely inside the other
    # the only argument c is a Circle object
    # returns a boolean
    def circle_overlap(self, c):
        sum_of_radii = c.radius + self.radius
        distance = self.center.dist(c.center)
        return distance < sum_of_radii

    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object
    def circle_circumscribe(self, r):
        rectangle_diagonal = math.hypot(r.ul.x - r.lr.x, r.ul.y - r.lr.y)
        circle_radius = 0.5*rectangle_diagonal
        center_rectangle = Point((r.ul.x + r.lr.x)/2,(r.ul.y - r.lr.y)/2)
        center_circle = center_rectangle
        return Circle(center_circle, circle_radius)

    # string representation of a circle
    # takes no arguments and returns a string
    def __str__(self):
        return "Radius: " + str(self.radius) + ", Center: " + str(self.center)

    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__(self, other):
        tol = 1.0e-8
        return (abs(self.radius - other.radius))<tol


class Rectangle(object):
    # constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length(self):
        return float(abs(self.lr.x - self.ul.x))

    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def width(self):
        return float(abs(self.lr.y - self.ul.y))

    # determine the perimeter
    # takes no arguments, returns a float
    def perimeter(self):
        perimeter = 2*(Rectangle(self.ul.x, self.ul.y, self.lr.x, self.lr.y).length() + Rectangle(self.ul.x, self.ul.y, self.lr.x, self.lr.y).width())
        return perimeter

    # determine the area
    # takes no arguments, returns a float
    def area(self):
        area = Rectangle(self.ul.x, self.ul.y, self.lr.x, self.lr.y).length() * Rectangle(self.ul.x, self.ul.y, self.lr.x, self.lr.y).width()
        return area

    # determine if a point is strictly inside the Rectangle
    # takes a point object p as an argument, returns a boolean
    def point_inside(self, p):
        return self.ul.x < p.x < self.lr.x and self.lr.y < p.y < self.ul.y

    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal
    def rectangle_inside(self, r):
        return self.ul.x < r.ul.x and self.lr.x > r.lr.x and self.ul.y > r.ul.y and self.lr.y < r.lr.y

    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def rectangle_overlap(self, r):    
        def intersect(int_a = (0,0), int_b=(0,0)):
            left_end = max(min(int_a), min(int_b))
            right_end = min(max(int_a), max(int_b))
            return left_end < right_end
        
        if self.rectangle_inside(r) or r.rectangle_inside(self):
            return False
        
        elif intersect((self.ul.x, self.lr.x), (r.ul.x,r.lr.x)) and intersect((self.ul.y, self.lr.y), (r.ul.y,r.lr.y)):
            return True

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object
    def rectangle_circumscribe(self, c):
        circle_radius = c.radius
        circle_center = c.center
        rectangle_horizontal = circle_radius
        rectangle_vertical = circle_radius
        rectangle_ul_x = circle_center.x-rectangle_horizontal
        rectangle_ul_y = circle_center.y+rectangle_vertical
        rectangle_lr_x = circle_center.x+rectangle_horizontal
        rectangle_lr_y = circle_center.y - rectangle_vertical
        return Rectangle(rectangle_ul_x, rectangle_ul_y, rectangle_lr_x, rectangle_lr_y)

    # give string representation of a rectangle
    # takes no arguments, returns a string
    def __str__(self):
        return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__(self, other):
        tol = 1.0e-8
        return (abs(self.ul.x - other.ul.x)) < tol and (abs(self.ul.y - other.ul.y)) < tol and (abs(self.lr.x - other.lr.x)) < tol and (abs(self.lr.y - other.lr.y)) < tol

# Print all statements in main
def main():
    with open('geom.txt', 'r') as file:
        all_points = file.readlines()

    P = all_points[0].split()
    P_x = float(P[0])
    P_y = float(P[1])

    Point_P = Point(P_x, P_y)
    print("Coordinates of P:", Point(P_x, P_y).__str__())

    Q = all_points[1].split()
    Q_x = float(Q[0])
    Q_y = float(Q[1])

    Point_Q = Point(Q_x, Q_y)
    print("Coordinates of Q:", Point(Q_x, Q_y).__str__())

    distance = Point.dist(Point_Q, Point_P)
    print("Distance between P and Q:", distance)

    C = all_points[2].split()
    C_radius = float(C[0])
    C_center_x = float(C[1])
    C_center_y = float(C[2])

    print("Circle C:", Circle(C_radius, C_center_x, C_center_y).__str__())

    D = all_points[3].split()
    D_radius = float(D[0])
    D_center_x = float(D[1])
    D_center_y = float(D[2])

    print("Circle D:", Circle(D_radius, D_center_x, D_center_y).__str__())
    print("Circumference of C:", Circle(C_radius, C_center_x, C_center_y).circumference())
    print("Area of D:",Circle(D_radius, D_center_x, D_center_y).area())


    if Circle(C_radius, C_center_x, C_center_y).point_inside(Point_P) == True:
        print("P is inside C")
    else:
        print("P is not inside C")

    if Circle(D_radius, D_center_x, D_center_y).circle_inside(Circle(C_radius, C_center_x, C_center_y)) == True:
        print("C is inside D")
    else:
        print("C is not inside D")

    if Circle(D_radius, D_center_x, D_center_y).circle_overlap(Circle(C_radius, C_center_x, C_center_y)) == True:
        print("C does intersect D")
    else:
        print("C does not intersect D")

    if Circle(D_radius, D_center_x, D_center_y).__eq__(Circle(C_radius, C_center_x, C_center_y)) == True:
        print("C is equal to D")
    else:
        print("C is not equal to D")

    G = all_points[4].split()
    G_ul_x = float(G[0])
    G_ul_y = float(G[1])
    G_lr_x = float(G[2])
    G_lr_y = float(G[3])

    print("Rectangle G:", Rectangle(G_ul_x, G_ul_y, G_lr_x, G_lr_y).__str__())


    H = all_points[5].split()
    H_ul_x = float(H[0])
    H_ul_y = float(H[1])
    H_lr_x = float(H[2])
    H_lr_y = float(H[3])

    print("Rectangle H:", Rectangle(H_ul_x, H_ul_y, H_lr_x, H_lr_y).__str__())

    print("Length of G:", Rectangle(G_ul_x, G_ul_y, G_lr_x, G_lr_y).length())

    print("Width of H:", Rectangle(H_ul_x, H_ul_y, H_lr_x, H_lr_y).width())

    print("Perimeter of G:", Rectangle(G_ul_x, G_ul_y, G_lr_x, G_lr_y).perimeter())

    print("Area of H:", Rectangle(H_ul_x, H_ul_y, H_lr_x, H_lr_y).area())

    if Rectangle(G_ul_x, G_ul_y, G_lr_x, G_lr_y).point_inside(Point(P_x, P_y)) == True:
        print("P is inside G")
    else:
        print("P is not inside G")

    if Rectangle(H_ul_x, H_ul_y, H_lr_x, H_lr_y).rectangle_inside(Rectangle(G_ul_x, G_ul_y, G_lr_x, G_lr_y)) == True:
        print("G is inside H")
    else:
        print("G is not inside H")

    if Rectangle(H_ul_x, H_ul_y, H_lr_x, H_lr_y).rectangle_overlap(Rectangle(G_ul_x, G_ul_y, G_lr_x, G_lr_y)) == True:
        print("G does overlap H")
    else:
        print("G does not overlap H")

    print("Circle that circumscribes G:", Circle.circle_circumscribe(None, Rectangle(G_ul_x, G_ul_y, G_lr_x, G_lr_y)))

    print("Rectangle that circumscribes D:", Rectangle.rectangle_circumscribe(None, Circle(D_radius, D_center_x, D_center_y)))

    if Rectangle(G_ul_x, G_ul_y, G_lr_x, G_lr_y).__eq__(Rectangle(H_ul_x, H_ul_y, H_lr_x, H_lr_y)) == True:
        print("Rectangle G is equal to H")
    else:
        print("Rectangle G is not equal to H")

if __name__ == "__main__":
    main()

