#  File: EvenMagicSquare.py

#  Description: Program that uses recursion to find 4x4 magic squares

#  Student Name: Isabella Joseph

#  Student UT EID: ij2799

#  Partner Name:  Kaitlyn Ng

#  Partner UT EID:  kn8685

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/19/19

#  Date Last Modified:

# Create list of integers of 1 through 16
def create_1d():
    list_1d = []
    for i in range(1, 17):
        list_1d.append(i)
    return list_1d


# Permute list of integers
def permute(a, lo, count):
    hi = len(a)
    if count == 10:
        return count

    # Base case
    if (lo == hi):

        # Check columns
        if (a[0] + a[4] + a[8] + a[12]) == 34 and (a[1] + a[5] + a[9] + a[13]) == 34 and (a[2] + a[6] + a[10] + a[14]) == 34:

            # Check diagonals
            if (a[3] + a[6] + a[9] + a[12]) == 34 and (a[0] + a[5] + a[10] + a[15]) == 34:
                print(a)
                return count + 1

        else:
            return count

    # Check rows
    elif (lo == 4) and (a[0] + a[1] + a[2] + a[3]) != 34:
        return count

    elif (lo == 8) and (a[4] + a[5] + a[6] + a[7]) != 34:
        return count

    elif (lo == 12) and (a[8] + a[9] + a[10] + a[11]) != 34:
        return count

    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            count = permute(a, lo + 1, count)
            a[lo], a[i] = a[i], a[lo]

    return count


def main():
    permute(create_1d(), 0, 0)
main()

