#  File: ConvexHull.py

#  Description: Convex Hull formed from points inputted

#  Student Name: Isabella Joseph

#  Student UT EID: ij2799

#  Partner Name: Kaitlyn Ng

#  Partner UT EID: kn8685

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/26/2019

#  Date Last Modified: 9/26/2019

import math

class Point (object):
    # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y < other.y)
        return (self.x < other.x)

    def __le__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y > other.y)
        return (self.x > other.x)

    def __ge__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
        return (self.x >= other.x)

# compute and return the determinant of the coordinates of three points
# p, q, and r are Point objects
def det (p, q, r):
    return (((p.x * q.y) + (q.x * r.y) + (r.x * p.y)) - ((p.y * q.x) + (q.y * r.x) + (r.y * p.x)))


# computes and returns the convex hull of a sorted list of Points
# convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order

def convex_hull(sorted_points):
    upper_hull = []
    p1 = sorted_points[0]
    p2 = sorted_points[1]

    upper_hull.append(p1)
    upper_hull.append(p2)

    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])

        while (len(upper_hull) >= 3):

            determinant = det(upper_hull[-3], upper_hull[-2], upper_hull[-1])
            if (determinant > 0):
                upper_hull.pop(-2)
            else:
                break

    # Append points into the lower hull
    lower_hull = []
    pn = sorted_points[len(sorted_points) - 1]
    pn_1 = sorted_points[len(sorted_points) - 2]

    lower_hull.append(pn)
    lower_hull.append(pn_1)

    for i in range(len(sorted_points) - 3, -1, -1):
        lower_hull.append(sorted_points[i])

        while (len(lower_hull) >= 3):

            determinant = det(lower_hull[-3], lower_hull[-2], lower_hull[-1])
            if (determinant > 0):
                lower_hull.pop(-2)

            else:
                break

    # Remove first and last elements from lower hull to avoid duplication with upper hull
    lower_hull.pop(0)
    lower_hull.pop(-1)

    convex_poly = upper_hull + lower_hull

    return convex_poly

# compute and return the area of a convex polygon
# convex_poly is a list of Point objects that define the vertices
# of a convex polygon in order


def area_poly(convex_poly):

#Part 1

    det_part_1_sum = 0
    for i in range(0,len(convex_poly)):

        if i < (len(convex_poly)-1):
            xi = convex_poly[i].x
            yi = convex_poly[i + 1].y

            det_part_1_sum += xi*yi



        elif i==(len(convex_poly)-1):
            xi = convex_poly[i].x
            yi = convex_poly[0].y

            det_part_1_sum += xi*yi

#Part 2

    det_part_2_sum = 0
    for i in range(0,len(convex_poly)):

        if i < (len(convex_poly)-1):
            xi = convex_poly[i + 1].x
            yi = convex_poly[i].y

            det_part_2_sum += xi*yi


        elif i==(len(convex_poly)-1):
            xi = convex_poly[0].x
            yi = convex_poly[i].y

            det_part_2_sum += xi*yi

    det_sum = abs(det_part_1_sum - det_part_2_sum)

    area = 0.5*(det_sum)

    return area



def main():
    # create an empty list of Point objects
    point_objects = []
    # open file points.txt for reading
    with open('points.txt', 'r') as file:
        data = file.readlines()

    # read file line by line, create Point objects and store in a list
    for i in range(len(data)):
        data[i] = data[i].strip('\n')
        data[i] = data[i].split('\t')

        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])

    # Where n is the number of points
    n = data[0][0]

    for i in range(1, n + 1):
        point_x = data[i][0]
        point_y = data[i][1]

        point = Point(point_x, point_y)
        point_objects.append(point)

    # Sort the list according to x-coordinates
    sorted_points = sorted(point_objects)

    convex_poly = convex_hull(sorted_points)

    print("Convex Hull")

    for x in convex_poly:
        print(x)

    print(" ")
    print("Area of Convex Hull = ", area_poly(convex_poly))

if __name__ == "__main__":
  main()
