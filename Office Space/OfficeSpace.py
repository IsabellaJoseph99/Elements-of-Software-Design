#  File: OfficeSpace.py

#  Description: A program that determines allocated and contested space in an office setting.

#  Student Name: Isabella Joseph

#  Student UT EID: ij2799

#  Partner Name: Kaitlyn Ng

#  Partner UT EID: kn8685

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/23/2019

#  Date Last Modified: 9/23/2019

def test_case_data():
    with open('office.txt', 'r') as file:
        data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip('\n')
    i = 0
    test_cases = 0
    all_data = []
    num_people = []
    total_area = []
    while i < len(data):
        num = data[i+1]
        num_people.append(int(num))
        # Creates list for people and their coordinates
        case = []
        for j in range(i, i + int(num) + 2):
            x = data[j].split()
            case.append(x)
        all_data.append(case)
        case = []

        # Creates list for area   
        y = data[i].split()
        total_area.append(y)

        # Increments while loop
        i = i + int(num) + 2 
        test_cases += 1
    return (total_area, all_data, test_cases, num_people)
total_area, all_data, test_cases, num_people = test_case_data()

def get_points(all_data):
    all_points = []
    points = []
    temp_point = []
    next_case = []
    for x in range(len(all_data)):
        for y in range(2, len(all_data[x])):
            for z in range(1,5):
                temp_point.append(int(all_data[x][y][z]))
            points.append(temp_point)
            temp_point = []
            next_case.append(points)
        all_points.append(points)
        points = []
    return all_points

def get_names(all_data):
    all_names = []
    names = []
    temp_names = []
    next_names = []
    for x in range(len(all_data)):
        for y in range(2, len(all_data[x])):
            for z in range(0,1):
                temp_names.append(all_data[x][y][z])
            names.append(temp_names)
            temp_names = []
            next_names.append(names)
        all_names.append(names)
        names = []
    return all_names

def make_matrix():
    total_area, all_data, test_cases, num_people = test_case_data()
    # Find total area of building
    matrix = []
    list_per_case = []
    temp_list = []
    for x in range(test_cases):
        building_area = int(total_area[x][0]) * int(total_area[x][1])
        for i in range(0, int(total_area[x][1])):
            for j in range(0, int(total_area[x][0])):
                temp_list.append(0)
            list_per_case.append(temp_list)
            temp_list = []
        matrix.append(list_per_case)
        list_per_case = []
    return matrix

new_matrix = make_matrix()

def update_matrix(new_matrix):
    points = get_points(all_data)
    for a in range(test_cases):
        for b in range(0,num_people[a]):
            x1 = int((points[a][b][0]))
            x2 = int((points[a][b][2]))
            y1 = int((points[a][b][1]))
            y2 = int((points[a][b][3]))

            if x1 == -1:
                x1 = 0
            if x2 == -1:
                x2 = 0
            if y1 == -1:
                y1 = 0
            if y2 == -1:
                y2 = 0

            for c in range(y1, y2):
                for d in range(x1, x2):
                    new_matrix[a][c][d] += 1

    return new_matrix
update_matrix(new_matrix)

def guaranteed_space(new_matrix):
    points = get_points(all_data)

    guaranteed_all = []
    for a in range(test_cases):
        guaranteed_case = []
        for b in range(0,num_people[a]):

            x1 = int((points[a][b][0]))
            x2 = int((points[a][b][2]))
            y1 = int((points[a][b][1]))
            y2 = int((points[a][b][3]))

            if x1 == -1:
                x1 = 0
            if x2 == -1:
                x2 = 0
            if y1 == -1:
                y1 = 0
            if y2 == -1:
                y2 = 0


            guaranteed = 0
            for c in range(y1, y2):
                for d in range(x1, x2):
                    if new_matrix[a][c][d] == 1:
                        guaranteed += 1

            guaranteed_case.append(guaranteed)
            guaranteed = 0
        guaranteed_all.append(guaranteed_case)
        guaranteed_case = []

    return guaranteed_all
guaranteed_space(new_matrix)

def area(new_matrix):
    total_area, all_data, test_cases, num_people = test_case_data()
    unallocated_area = 0
    unallocated_area_list = []
    contested_area = 0
    contested_area_list = []
    area_guaranteed = 0
    area_guaranteed_list = []
    office_area_total = []
    for a in range(0,test_cases):
        for b in range(int(total_area[a][1])):
            for c in range(int(total_area[a][0])):
                if new_matrix[a][b][c] == 0:
                    unallocated_area += 1
                if new_matrix[a][b][c] > 1:
                    contested_area += 1

        office_area_total.append(int(total_area[a][1])*int(total_area[a][0]))

        unallocated_area_list.append(unallocated_area)
        unallocated_area = 0

        contested_area_list.append(contested_area)
        contested_area = 0

    return unallocated_area_list, contested_area_list, office_area_total
area(new_matrix)

def main():
    unallocated_area_list, contested_area_list, office_area_total = area(new_matrix)
    names = get_names(all_data)
    guar = guaranteed_space(new_matrix)
    for x in range(test_cases):
        print("Total", office_area_total[x])
        print("Unallocated", unallocated_area_list[x])
        print("Contested", contested_area_list[x])

        for y in range(num_people[x]):
            print(names[x][y][0], guar[x][y])

        print('')
main()



