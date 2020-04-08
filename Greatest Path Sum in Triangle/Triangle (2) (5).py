#  File: Triangle.py

#  Description: A program that finds the greatest path in a triangle using brute force, greedy, divide and conquer and dynamic programming methods

#  Student's Name: Kaitlyn Ng

#  Student's UT EID: kn8685

#  Partner's Name: Isabella Joseph

#  Partner's UT EID: ij2799

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 12/4/2019

#  Date Last Modified: 12/7/2019

import time
# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
    if len(grid) == 0:
        return 0
    row = 0
    col = 0
    all_paths = exhaustive_search_helper(grid, row, col)
    sums = []
    for path in all_paths:
        sums.append(sum(path))
    return max(sums)


def exhaustive_search_helper (grid, row, col):
    current = grid[row][col]
    if row < (len(grid)-1):
        paths_below = exhaustive_search_helper(grid, row+1, col) + exhaustive_search_helper(grid, row+1, col+1)
        return [[current] + path for path in paths_below]
    else:
        return [[current]]

# returns the greatest path sum using greedy approach
def greedy (grid):
    if len(grid) == 0:
        return 0
    sum = grid[0][0]
    return greedy_helper(grid, sum, 0, 0)

def greedy_helper(grid, sum, row, col):
    if row == len(grid)-2:
        return sum + max(grid[row+1][col], grid[row+1][col+1])
    else:
        max_value = max(grid[row+1][col], grid[row+1][col+1])
        if grid[row+1][col] > grid[row+1][col+1]:
            idx = col
        else:
            idx = col+1
        return greedy_helper(grid, sum+max_value, row+1, idx)


# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
    if len(grid) == 0:
        return 0
    sum_list = rec_search_helper(grid, 0, 0, 0)
    return max(sum_list)

def rec_search_helper(grid, row, col, biggest_sum):
    num_rows = len(grid)
    if row >= num_rows:
        return [biggest_sum]
    else:
        if row == len(grid)-1:
            return rec_search_helper(grid, row+1, col, (biggest_sum+grid[row][col]))
        else:
            return rec_search_helper(grid, row+1, col, (biggest_sum+grid[row][col])) + rec_search_helper(grid, row+1, col+1, (biggest_sum+grid[row][col]))

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    return dynamic_prog_helper(grid, -2, grid[:])


def dynamic_prog_helper(grid, counter, memo):
    num_rows = len(grid)
    if num_rows == 0:
        return 0
    elif num_rows == 1:
        return grid[0][0]
    elif counter == -1 * num_rows:
        return memo[counter][0] + max(grid[counter + 1][0], grid[counter + 1][1])
    else:
        for x in range(len(grid[counter])):
            memo[counter][x] += max(grid[counter + 1][x], grid[counter + 1][x + 1])
        return dynamic_prog_helper(grid, counter - 1, memo)


# reads the file and returns a 2-D list that represents the triangle
def read_file ():
    in_file = open('triangle.txt', 'r')

    # determine how many rows are in triangle
    num_rows = in_file.readline()

    # read the triangle int oa 2-D list
    tri_list = []
    for line in in_file:
        line = line.strip()
        line = line.split(' ')
        for i in range(len(line)):
            line[i] = int(line[i])
        tri_list.append(line)
    return num_rows, tri_list

def main ():
    # read triangular grid from file
    num_rows, grid = read_file()

    ti = time.time()
    # output greates path from exhaustive search
    print('The greatest path sum through exhaustive search is ' + str(exhaustive_search(grid)) + '.')
    tf = time.time()
    del_t = tf - ti
    # print time taken using exhaustive search
    print('The time taken for exhaustive search is', del_t, 'seconds.')

    # output greatest path from greedy approach
    greedy_search_times = []
    for x in range(100):
        ti = time.time()
        path_sum = greedy(grid)
        tf = time.time()
        del_t = tf - ti
        greedy_search_times.append(del_t)
    average = sum(greedy_search_times) / 100

    print('The greatest path sum through greedy search is ' + str(greedy(grid)) + '.')
    # print time taken using greedy approach
    print('The time taken for greedy approach is', average, 'seconds.')

    ti = time.time()
    # output greates path from divide-and-conquer approach
    print('The greatest path sum through recursive search is ' + str(rec_search(grid)) + '.')
    tf = time.time()
    del_t = tf - ti
    # print time taken using divide-and-conquer approach
    print('The time taken for recursive search is', del_t, 'seconds.')

    # output greatest path from dynamic programming

    print('The greatest path sum through dynamic programming is ' + str(dynamic_prog(grid)) + '.')

    # print time taken using dynamic programming
    dynamic_search_times = []
    for x in range(100):
        ti = time.time()
        path_sum = dynamic_prog(grid)
        tf = time.time()
        del_t = tf - ti
        dynamic_search_times.append(del_t)
    average = sum(dynamic_search_times) / 100
    print('The time taken for dynamic programming is', average, 'seconds.')

if __name__ == "__main__":
    main()