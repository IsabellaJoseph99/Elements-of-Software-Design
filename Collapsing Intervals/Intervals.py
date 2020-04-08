#  File: Intervals.py

#  Description: A program that can be used to collapse various intervals

#  Student Name: Isabella Joseph

#  Student UT EID: ij2799

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/9/2019

#  Date Last Modified: 9/9/2019

#citation: https://stackoverflow.com/questions/28090960/read-file-as-a-list-of-tuples
def main():
    import collections
    text_file = "intervals.txt"
    initial_list = []
    with open(text_file) as f:
        for i in f.readlines():
            interval = i.split(" ")
            try:
                initial_list.append((eval(interval[0]), eval(interval[1])))
            except:
                pass

    initial_list.sort()

    #citation: https://stackoverflow.com/questions/5679638/merging-a-list-of-time-range-tuples-that-have-overlapping-time-ranges
    collapsed_list = [initial_list[0]]
    for x,y in initial_list[1:]:
        i,j = collapsed_list[-1]
        if x<=j and j<y:
            collapsed_list[-1] = i,y
        elif j<x and x<y:
            collapsed_list.append((x,y))
        else:
            pass

    collapsed_list.sort()

    print("Non-intersecting Intervals:")
    for x in collapsed_list:
        print(x)
    print(" ")
    print("Non-intersecting Intervals in order of size:")
    size_list = []
    for c,d in collapsed_list:
        y = d-c
        size_list.append(y)
        #print(size_list)
    keys = size_list
    values = collapsed_list
    dictionary = dict(zip(keys,values))
    #print(dictionary)

    sorted_dictionary = collections.OrderedDict(sorted(dictionary.items()))
    #print(sorted_dictionary)
    #citation: https://thomas-cokelaer.info/blog/2017/12/how-to-sort-a-dictionary-by-values-in-python/
    x = sorted_dictionary.values()
    for tuple in x:
        print(tuple)
main()




