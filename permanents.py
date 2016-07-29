#!/usr/bin/env python

"""

"""

## IMPORTS ##
import curses
import ystockquote

## FUNCTIONS ##

def get_perm_list():

    perm_list = []
    row1_list = []
    row2_list = []
    row3_list = []

    with open("permanents/perm_l1", "r") as f:
        for line in f:
            row1_list.append(line.rstrip('\n'))
    f.close()
    perm_list.append(row1_list)

    with open("permanents/perm_l2", "r") as f:
        for line in f:
            row2_list.append(line.rstrip('\n'))
    f.close()
    perm_list.append(row2_list)

    with open("permanents/perm_l3", "r") as f:
        for line in f:
            row3_list.append(line.rstrip('\n'))
    f.close()
    perm_list.append(row3_list)

    return perm_list

def get_permanents(perm):

    data = ystockquote.get_all(str(perm))

    return data

def prep_perm_dict(perm, perm_data, perm_data_dict, row):

    perm_data_dict[row][str(perm)] = perm_data

    return perm_data_dict

def write_perm_data(perm_data_dict):

    with open("permanents/perm_data", "w") as f:
        f.write(str(perm_data_dict))
    f.close()


def read_perm_data():

    try:
        with open("permanents/perm_data", "r") as f:
            perm_data_dict = eval(f.read())
    except:
        perm_data_dict = []

    return perm_data_dict

def print_permanents(scr_top, perm, row, col, perm_data):

    if perm == "GC=F":
        perm = "Gold"
    elif perm == "SI=F":
        perm = "Silver"
    elif perm == "HG=F":
        perm = "Copper"
    elif perm == "CL=F":
        perm = "Crude"
    elif perm[-2:] == "=X":
        perm = perm[0:3] + "/" + perm[3:6]
    elif perm[0] == "^":
        perm = perm[1:]


    printing_perm = str(perm) + "=" + str(perm_data["price"])

    perm_length = len(printing_perm) + 1
    
    if perm_length+col < curses.COLS:
        scr_top.addstr(1+row, col, str(printing_perm))

    return perm_length
