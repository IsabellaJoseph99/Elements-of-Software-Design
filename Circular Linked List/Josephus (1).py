#  File: Josephus.py

#  Description: A code that returns where Josephus should stand in a circle to not die

#  Student Name: Isabella Joseph

#  Student UT EID: ij2799

#  Partner Name: Kaitlyn Ng

#  Partner UT EID: kn8685

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11/4/2019

#  Date Last Modified: 11/4/2019

class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class CircularList(object):
  # Constructor
    def __init__ ( self ):
        self.last = None
        self.first = None
        self.numLinks = 0


  # Insert an element (value) in the list
    def insert ( self, data):

        newLink = Link(data)
        current = self.first

        if (current == None):
            self.first = newLink
            newLink.next = self.first
            self.last = newLink
            self.numLinks += 1
            return

        else:
            newLink.next = self.first
            self.last.next = newLink
            self.last = newLink
            self.numLinks += 1
            return


    # Find the link with the given data (value)
    def find(self, data):

        current = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == self.first):
                return None
            else:
                current = current.next

        return current


    # Delete a link with a given data (value)
    def delete(self, data):

        current = self.first
        previous = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == self.first):
                return None
            else:
                previous = current
                current = current.next

        if (current.data == self.first.data):
            self.first = self.first.next
            self.last.next = previous.next
        elif (current.data == self.last.data):
            self.last = previous
            previous.next = current.next

        else:
            previous.next = current.next


        self.numLinks -= 1
        return current



    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def delete_after(self, start, n):
        current = self.find(start.data)

        for x in range(n - 1):
            current = current.next

        print(current.data)
        self.delete(current.data)
        return current.next


    def __str__ ( self ):
        ret = ''
        current = self.first

        if current == None:
            return '[]'
        else:
            ret += str(current.data) + ' '
            current = current.next

        while current.data != self.first.data:
            ret += (str(current.data)  + ' ')
            current = current.next

        return ret


def main():

    # read in file
    data = []
    in_file = open('josephus.txt', 'r')
    for line in in_file:
        line = line.strip()
        line = int(line)
        data.append(line)
    in_file.close()

    num_soldiers = data[0]
    start = Link(data[1])
    step_size = data[2]


    # create a linked list with specified number of soldiers
    aList = CircularList()
    for i in range(1,num_soldiers + 1):
        aList.insert(i)


    # delete links
    while aList.numLinks > 0:
        new_start = aList.delete_after(start,step_size)
        start = new_start

main()