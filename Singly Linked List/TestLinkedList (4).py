#  File: TestLinkedList.py

#  Description: A code that explores Linked Lists

#  Student Name: Isabella Joseph

#  Student UT EID: ij2799

#  Partner Name: Kaitlyn Ng

#  Partner UT EID: kn8685

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11/1/2019

#  Date Last Modified: 11/1/2019



class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):

    def __init__(self):
        self.first = None
        self.num_links = 0


    def __str__(self):
        counter = 0
        ret = ''
        current = self.first

        while current != None:
            counter += 1
            ret += (str(current) + '  ')
            current = current.next

            if counter % 10 == 0:
                ret += '\n'
        return ret


    # get number of links
    def get_num_links(self):
        return self.num_links


    # add an item at the beginning of the list
    def insert_first(self, data):
        newLink = Link(data)
        newLink.next = self.first
        self.first = newLink
        self.num_links += 1

    # add an item at the end of a list
    def insert_last(self, data):
        newLink = Link(data)
        # data -> next
        current = self.first

        if (current == None):
            self.first = newLink
            return

        while (current.next != None):
            current = current.next

        current.next = newLink
        self.num_links += 1


    def insert_in_order(self, data):

        newLink = Link(data)

        current = self.first
        if current == None or current.data > data:
            self.insert_first(data)
        else:



            while current.next and current.next.data < data:
                current = current.next


            newLink.next = current.next
            current.next = newLink



    def findLink(self, data):
        current = self.first
        if (current == None):
            return None
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current


    # search in an unordered list, return None if not found
    # will return data if found
    def find_unordered(self, data):
        current = self.first
        if (current == None):
            return None
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):

        current = self.first
        if (current == None):
            return None
        while (current.data != data):
            if (current.next == None):
                return None
            elif (current.data > data):
                return None
            else:
                current = current.next

        return current


    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        current = self.first
        previous = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next

        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

    # Copy the contents of a list and return new list
    def copy_list(self):
        copy_of_list = LinkedList()

        if self.get_num_links() == 0:
            return copy_of_list

        current = self.first

        while current != None:
            copy_of_list.insert_last(current.data)
            current = current.next

        return copy_of_list


    # Reverse the contents of a list and return new list
    def reverse_list(self):
        copy_of_list = LinkedList()
        current = self.first

        while current != None:
            copy_of_list.insert_first(current.data)
            current = current.next

        return copy_of_list

    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        ### empty case
        sorted_list = LinkedList()
        current = self.first

        if current == None:
            return sorted_list

        sorted_list.insert_first(current.data)
        current = current.next


        while current != None:
            sorted_list.insert_in_order(current.data)
            current = current.next

        return sorted_list

    # # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        current = self.first
        while current.next != None:
            if current.data > current.next.data:
                return False
            else:
                current = current.next
        return True


    # Return True if a list is empty or False otherwise
    def is_empty(self):
        if self.num_links == 0:
            return True
        else:
            return False


    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):

        if self.get_num_links() == 0 and other.get_num_links() == 0:
            return self.copy_list()
        elif self.get_num_links() == 0:
            return other.copy_list()                         ###### Make copy
        elif other.get_num_links() == 0:
            return self.copy_list()
        else:
            merged = self.copy_list()
            current = other.first
            while current != None:
                merged.insert_last(current.data)
                current = current.next

        return merged.sort_list()


    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        if self.get_num_links() == 0 and other.get_num_links() == 0:
            return True

        elif self.get_num_links() != other.get_num_links():
            return False
        else:
            current1 = self.first
            current2 = other.first

            while current1 != None and current2 != None:
                # print(current1, current2)
                if current1.data == current2.data:
                    if current1.next != None or current2.next!= None:
                        current1 = current1.next
                        current2 = current2.next
                    else:
                        break
                else:
                    return False
            return True

    # # Return a new list, keeping only the first occurence of an element
    # # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):

        current = self.first
        duplicate_data = []           ## Normal list of duplicate data
        duplicate_linked = LinkedList()         ## Linked list of duplicates
        while current != None:
            if current.data not in duplicate_data:    ## if data not in the list of dupicates, insert into linkedlist
                duplicate_linked.insert_last(current.data)        ## insert last into linked list to keep order
                duplicate_data.append(current.data)                ## append to normal list, to check next time
                current = current.next
            else:
                current = current.next
        return duplicate_linked


def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    # aList = LinkedList()
    # aList.insert_first(3)
    # aList.insert_first(10)
    # aList.insert_first(1)
    # aList.insert_first(2)
    # aList.insert_first(7)
    # aList.insert_first(9)
    # aList.insert_first(0)
    # aList.insert_first(-7)
    # aList.insert_first(-4)
    # aList.insert_first(-9)
    # aList.insert_first(19)
    # aList.insert_first(188)
    # print(aList.__str__())
    # print()

    # Test method insert_last()
    # bList = LinkedList()
    # bList.insert_last(5)
    # bList.insert_last(6)
    # bList.insert_last(9)
    # bList.insert_last(11)
    # print(bList)
    # print()

    # Test method insert_in_order()
    # print(bList.insert_in_order(10))

    # Test method get_num_links()
    # print(bList.get_num_links())

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    # print(bList.find_unordered(6))

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    # cList = LinkedList()
    # cList.insert_last(1)
    # cList.insert_last(2)
    # cList.insert_last(3)
    # cList.insert_last(4)

    # print(cList.find_ordered(4))

    # Test method delete_link()
    # Consider two cases - data is there, data is not there

    # Test method copy_list()

    # Test method reverse_list()

    # Test method sort_list()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted

    # Test method is_empty()
    # emptyList = LinkedList()
    # emptyList.insert_first(4)
    # print(emptyList.is_empty())
    #
    # # Test method merge_list()
    #
    # # Test method is_equal()
    # # Consider two cases - lists are equal, lists are not equal
    #
    # # Test remove_duplicates()
    #
    # aList = LinkedList()
    # aList.insert_first(-1)
    # aList.insert_first(3)
    # aList.insert_first(3)
    # aList.insert_first(1)

    # print(aList)

    # print(aList.remove_duplicates())
    #
    # # print(aList)
    # # aList.insert_in_order()
    # # for i in range(20):
    # #     import random
    # #     item = random.randint(1,100)
    # #     aList.insert_in_order(item)
    # #     print(aList, "donee")
    # # print(aList)
    # #
    # bList = LinkedList()
    # bList.insert_first(4)
    # # bList.insert_in_order(3)
    # # print(bList)

    Isabella_Kaitlyn = LinkedList()
    Isabella_Kaitlyn.insert_first(0)
    Isabella_Kaitlyn.insert_first(0)
    # bList.insert_first(0)
    # bList.insert_first(0)
    # bList.insert_first(0)

    # print(bList)
    #
    # print(bList.remove_duplicates())




if __name__ == "__main__":
    main()