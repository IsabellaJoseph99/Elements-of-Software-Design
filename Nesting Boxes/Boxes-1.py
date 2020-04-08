#  File: Boxes.py

#  Description: A program that gives us nested boxes

#  Student Name: Isabella Joseph

#  Student UT EID: ij2799

#  Partner Name:  Kaitlyn Ng

#  Partner UT EID:  kn8685

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/18/19

#  Date Last Modified: 10/18/2019

def does_fit(box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])


def sub_sets(a, b, lo):
  hi = len(a)
  if (lo == hi):
    return [b]
  else:
    c = b[:]
    b.append(a[lo])
    return sub_sets(a, b, lo + 1) + sub_sets(a, c, lo + 1)


def main():
  # open the file for reading
  in_file = open ("./boxes.txt", "r")

  # read the number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int(line)

  # create an empty list of boxes
  box_list = []

  # read the list of boxes from the file
  for i in range(num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for j in range(len(box)):
      box[j] = int(box[j])

    box.sort()
    box_list.append(box)

  # sort the box list
  box_list.sort()

  # get all subsets of boxes
  box_sub_set = sub_sets(box_list,[],0)

  # create empty list for nested boxes
  nested_boxes = []

  # check if all the boxes in a given subset fit
  for x in range(len(box_sub_set)):
    for y in range(len(box_sub_set[x])):
      if box_sub_set[x][y] == [] or len(box_sub_set[x][y]) == 1:
        continue

      elif (y+1) < len(box_sub_set[x]):
        box1 = box_sub_set[x][y]
        box2 = box_sub_set[x][y+1]

        if does_fit(box1, box2):
          continue
        else:
          break
      nested_boxes.append(box_sub_set[x])

  # print all the largest subset of boxes
  max_len = len(max(nested_boxes, key=len))

  if max_len == 0 or max_len == 1:
    print('No Nesting Boxes')
  else:
    print('Largest Subset of Nesting Boxes')
    for nested in nested_boxes:
      if len(nested) == max_len:
        for box in nested:
          print(box)
        print()


  # close the file
  in_file.close()

main()











