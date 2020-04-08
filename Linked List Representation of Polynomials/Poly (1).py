#  File: Poly.py

#  Description: A program that uses linked lists to calculate the sum and product of two linked lists

#  Student Name: Kaitlyn Ng

#  Student UT EID: kn8685

#  Partner Name: Isabella Joseph

#  Partner UT EID: ij2799

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11/9/19

#  Date Last Modified: 11/11/19

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
    def __init__ (self):
        self.first = None
        self.numLinks = 0

    # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        newLink = Link(coeff, exp)
        self.numLinks += 1
        current = self.first

        # if linked list is empty
        if current == None:
            self.first = newLink
            return

        elif exp > self.first.exp:
            newLink.next = self.first
            self.first = newLink
            return

        while current.next != None and exp < current.next.exp:
            current = current.next

        newLink.next = current.next
        current.next = newLink

    # function that reduces polynomials with the same exponents
    def reduce(self):
        curr = self.first
        if curr.next == None:
            return

        if curr != None:
            next = curr.next

        while curr != None and  next.next != None:

            # check if polynomial after is same exponent
            if next != None and curr.exp == next.exp:
                curr.coeff = curr.coeff + next.coeff
                curr.next = next.next

                next = curr.next

            else:
                curr = next
                next = next.next
        return

    # helper function that deletes any terms in polynomial with a coefficient of zero
    def delete_zero(self):
        previous = self.first
        current = self.first

        if current == None:
            return
        elif current.coeff == 0:
            self.first = current.next

        while current != None and current.coeff != 0:
            if current.next == None:
                return
            previous = current
            current = current.next

        previous.next = current.next
        return

    # helper function that counts the number of times a zero appears
    def count_zeroes(self):
        current = self.first
        zeroes = 0
        while current != None:
            if current.coeff == 0:
                zeroes += 1
            current = current.next
        return zeroes


    # add polynomial p to this polynomial and return the sum
    def add (self, p):

        # assign temp variables
        current = self.first
        current2 = p.first
        poly_sum = LinkedList()

        # inserts first polynomial (self) into the new linked list of sum
        while current != None:
            poly_sum.insert_in_order(current.coeff, current.exp)
            current = current.next

        while current2 != None:
            poly_curr = poly_sum.first

            while poly_curr != None:
                if current2.exp == poly_curr.exp:
                    poly_curr.coeff = poly_curr.coeff + current2.coeff
                    break

                elif poly_curr.next == None:
                    poly_sum.insert_in_order(current2.coeff, current2.exp)
                    break
                else:
                    poly_curr = poly_curr.next

            current2 = current2.next

        # reduce polynomials
        poly_sum.reduce()

        # delete any possible zero coefficients
        num_zeroes = poly_sum.count_zeroes()
        for i in range(num_zeroes):
            poly_sum.delete_zero()

        return poly_sum


    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        current = self.first
        poly_mult = LinkedList()

        while current!= None:
            current2 = p.first

            while current2 != None:
                new_coeff = current.coeff * current2.coeff
                new_exp = current.exp + current2.exp
                poly_mult.insert_in_order(new_coeff, new_exp)
                current2 = current2.next
            current = current.next

        # check to see if numbers with same exponents can be added together
        poly_mult.reduce()

        # delete any possible zero coefficients
        num_zeroes = poly_mult.count_zeroes()
        for i in range(num_zeroes):
            poly_mult.delete_zero()

        return poly_mult


    # create a string representation of the polynomial
    def __str__(self):
        s = ''
        current = self.first
        while current != None:
            s += str(current) + ' + '
            current = current.next

        s = s.strip(' + ')

        return s

def main():
    # open file poly.txt for reading
    in_file = open('poly.txt', 'r')

    data = []
    for line in in_file:
        line = line.strip()
        data.append(line)

    # data for first polynomial
    poly1_len = int(data[0])
    poly1 = []
    for i in range(1, poly1_len + 1):
        points = data[i].split()
        for point in points:
            point = int(point)
            poly1.append(point)

    # data for second polynomial
    poly2 = []
    for i in range(poly1_len + 3, len(data)):
        points = data[i].split()
        for point in points:
            point = int(point)
            poly2.append(point)

    # create polynomial p
    p = LinkedList()
    for i in range(0, len(poly1), 2):
        p.insert_in_order(poly1[i], poly1[i+1])

    # create polynomial q
    q = LinkedList()
    for i in range(0, len(poly2), 2):
        q.insert_in_order(poly2[i], poly2[i+1])

    # get sum of p and q and print sum
    pq_sum = p.add(q)
    print(pq_sum)

    # get product of p and q and print product
    pq_product = p.mult(q)
    print(pq_product)

if __name__ == "__main__":
    main()