#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new = []
    for idx in range(len(my_list)):
        if my_list[idx] % 2 == 0:
            new.append(True)
        else:
            new.append(False)

    return (new)
