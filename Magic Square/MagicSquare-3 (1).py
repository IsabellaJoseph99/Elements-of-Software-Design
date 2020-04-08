#  File: MagicSquare.py

#  Description: A program that generates a magic square given the number inputted by the user.

#  Student's Name: Isabella Joseph

#  Student's UT EID: ij2799

#  Partner's Name: N/A

#  Partner's UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/6/2019

#  Date Last Modified: 9/6/2019

def make_square(n):
    square_number = int(n ** 2)
    magic_square = [[0] * n for i in range(n)]
    i, j = (n - 1), (n - 1) // 2
    magic_square[i][j] = 1

    for digit in range(2, square_number + 1):
        if i < (n - 1) and j < (n - 1):
            i, j = i + 1, j + 1
        elif i == (n - 1) and j < (n - 1):
            i, j = 0, j + 1
        elif i < (n - 1) and j == (n - 1):
            i, j = i + 1, 0
        elif i == (n - 1) and j == (n - 1):
            i, j = i - 1, j
        elif i == (n - 1) and j > (n - 1):
            i, j = i + 1, 0
        if magic_square[i][j] != 0:
            i, j = i - 2, j - 1
        magic_square[i][j] = digit
    return(magic_square)

def print_square(magic_square):
    n = len(magic_square)
    square = int(n**2)
    square_string = str(square)
    x = int(len(square_string))
    for row in magic_square:
        for element in row:
            element_string = str(element)
            print(element_string.rjust(x+1), end=" ")
        print('')

def check_square(magic_square):
    n = int(len(magic_square))
    sum_actual, sum_correct = 0,0

    for j in range(0,n,1):
        sum_of_digits = magic_square[n-1][j]
        sum_correct = sum_correct + sum_of_digits

    # check for sum of rows
    for i in range(0,n,1):
        sum_actual = 0
        for j in range(0,n,1):
            sum_of_digits = magic_square[i][j]
            sum_actual = sum_actual + sum_of_digits
        if sum_actual != sum_correct:
            return False
        else:
            pass

    # check for sum of columns
    for j in range(0,n,1):
        sum_actual = 0
        for i in range(0,n,1):
            sum_of_digits = magic_square[i][j]
            sum_actual = sum_actual + sum_of_digits
        if sum_actual != sum_correct:
            return False
        else:
            pass

    # check for diagonals down to right
    sum_actual = 0
    sum_actual = sum([magic_square[i][i] for i in range(0, n)])
    if sum_actual != sum_correct:
        return False
    else:
        pass

    # check for diagonals down to left
    sum_actual = 0
    sum_actual = sum([magic_square[i][n-1-i] for i in range(0, n)])
    if sum_actual != sum_correct:
        return False
    else:
        pass

    return True

def main():
    while True:
        try:
            n = int(input('Please enter an odd number: '))
        except ValueError:
            n = int(input('Please enter an odd number: '))
        if n<1:
            n = int(input('Please enter an odd number: '))
        if n%2 == 0:
            n = int(input('Please enter an odd number: '))
        else:
            break
    magic_square = make_square(n)
    check_square(magic_square)
    if check_square(magic_square) is True:
        print("Here is a "+ str(n) +" x " + str(n)+ " magic square:")
        print(" ")
        print_square(magic_square)
        sum_actual = sum([magic_square[i][i] for i in range(0, n)])
        print(" ")
        print("This is a magic square and the canonical sum is "+str(sum_actual))

    if check_square(magic_square) is False:
        print("This is not a magic square")

if __name__ == "__main__":
    main()



