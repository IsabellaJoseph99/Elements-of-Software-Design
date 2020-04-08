#  File: Bridge.py

#  Description:  A function that gives the minimum time for a group of people of different speeds to cross a bridge with one flashlight.

#  Student Name: Isabella Joseph

#  Student UT EID:  ij2799

#  Partner Name: Kaitlyn Ng

#  Partner UT EID: kn8685

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/4/2019

#  Date Last Modified: 10/4/2019


def case1(case):
    case_sort = sorted(case)

    time = 0
    danger = case_sort
    safe = []

    if len(case_sort) == 1:
        time = case_sort[0]

    elif len(case_sort) == 2:
        time = case_sort[1]

    else:

        fastest = case_sort[0]
        second_fastest = case_sort[1]

        while len(danger)>0:


            if len(danger)>3:

                if fastest and second_fastest in danger:
                    safe.append(fastest)
                    safe.append(second_fastest)
                    danger.remove(fastest)
                    danger.remove(second_fastest)
                    time += second_fastest





                    danger.append(fastest)
                    safe.remove(fastest)
                    time += fastest





                else:
                    safe.append(danger[-1])
                    safe.append(danger[-2])
                    time += danger[-1]



                    danger.remove(danger[-1])
                    danger.remove(danger[-1])
                    danger.append(second_fastest)
                    safe.remove(second_fastest)
                    time += second_fastest


            elif len(danger) == 3:

                a = time + sum(danger)

                safe.append(danger[-1])
                safe.append(danger[-2])
                b = time + danger[-1]

                danger.remove(danger[-1])
                danger.remove(danger[-1])
                danger.append(min(safe))
                b += max(danger)

                safe.remove(min(safe))
                safe.append(danger[0])
                safe.append(danger[1])
                b += danger[1]

                danger.remove(danger[0])
                danger.remove(danger[0])

                time = min(a,b)

            else:
                break

            safe = sorted(safe)
            danger = sorted(danger)

    return time



def case2(case):
    case_sort = sorted(case)

    time = 0
    danger = case_sort
    safe = []
    i = 0
    if len(case_sort) == 1:
        time = case[0]
    else:
        while len(danger)>0 and (i+1) < len(danger):
            #move the fastest and slowest
            safe.append(danger[i])
            safe.append(danger[-1])

            time += max(danger[i], danger[-1])

            del danger[i]
            del danger[-1]

            if len(danger) == 0:
                break
            else:

                #move fastest to danger
                time += min(safe)
                danger.append(min(safe))
                safe.remove(min(safe))

    return time

def main():
    with open('bridge.txt', 'r') as file:
        data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip('\n')

    data = list(filter(lambda x: len(x) > 0, data))
    for x in range(0, len(data)):
        data[x] = int(data[x])
    num_cases = data[0]

    x = 1
    cases = []
    temp_list = []

    while x < len(data):
        num_people = data[x]
        for y in range(x+1, x + num_people + 1):
            temp_list.append(data[y])
        cases.append(temp_list)
        temp_list = []
        x = x + num_people + 1
    for x in cases:
        final_time = min(case1(x), case2(x))
        print(final_time)
        print()
main()