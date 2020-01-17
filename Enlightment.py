# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:16:35 2019

@author: NDM2KOR
"""

import numpy as np
#from itertools import permutations
from itertools import product
from copy import deepcopy


#Note: Here I considered that input text file has no spaces between one entry and other in a single row. 
#i.e. .x.x is correct but not . x . x
#So while you are giving the input please consider the same way. 
#If not let me know, we will have to change few lines of the code

### In given pdf, one example exit is mentioned as 'o' and in other example exit is mentioned as 'e'
## Here we consider exit is 'e'


#Problem1 : Establishment

# Shift function to shift in the direction specified
def shift(array,row,col,p,n):
    if(row+p >=0 and col+n >= 0):
        array[row+p][col+n] = array[row][col]
        array[row][col] = '.'
        if_shift = True
    else:
        if_shift = False
    return [array,if_shift]

# Function to execute the shift according to the given input string character
def find_route(flag,array_lines,p,n):
    find_B = np.where(array_lines == 'B')
    row_B = find_B[0][0]
    col_B = find_B[1][0]
    find_G = np.where(array_lines == 'g')
    row_G1 = find_G[0][0]
    col_G1 = find_G[1][0]
    row_G2 = find_G[0][1]
    col_G2 = find_G[1][1]
    find_E = np.where(array_lines == 'e')
    if(find_E[0].size == 0):
        result = "win"
        flag = False
    else:
        row_E = find_E[0][0]
        col_E = find_E[1][0]
    result = "Null"
    while(flag):
            flag = False
            if(row_B+p <=3 and col_B+n <=3):
                if(array_lines[row_B+p][col_B+n] == '.'):
                    shifted_array = shift(array_lines,row_B,col_B,p,n)
                    if(shifted_array[1] == False):
                        flag = False
                    else:
                        array_lines = shifted_array[0]    
    #                    print(col_B, "Here")
                        flag = True
                elif(array_lines[row_B+p][col_B+n] == 'g'): 
                    result = "lose"
                    flag = False
                elif(array_lines[row_B+p][col_B+n] == 'e'):
                    if(col_E == 3 or col_E == 0):
                        if(row_B == row_E):
                            shifted_array = shift(array_lines,row_B,col_B,p,n)
                            if(shifted_array[1] == False):
                                flag = False
                            else:
                                result = "win"
                                flag = False
                    elif(row_E == 3 or row_E == 0):
                        if(col_B == col_E):
                            shifted_array = shift(array_lines,row_B,col_B,p,n)
                            if(shifted_array[1] == False):
                                flag = False
                            else:
                                result = "win"
                                flag = False
            if(row_G1+p <=3 and col_G1+n <=3):
                if(array_lines[row_G1+p][col_G1+n] == '.'):
                    shifted_array = shift(array_lines,row_G1,col_G1,p,n)
                    if(shifted_array[1] == False):
                        flag = False
                    else:
                        array_lines = shifted_array[0]    
    #                    print("No Here")
                        flag = True
            if(row_G2+p <=3 and col_G2+n <=3):
                if(array_lines[row_G2+p][col_G2+n] == '.'):
                    shifted_array = shift(array_lines,row_G2,col_G2,p,n)
                    if(shifted_array[1] == False):
                        flag = False
                    else:
                        array_lines = shifted_array[0]    
    #                    print("Here I Guess")
                        flag = True
            find_B = np.where(array_lines == 'B')
            row_B = find_B[0][0]
            col_B = find_B[1][0]
            find_G = np.where(array_lines == 'g')
            row_G1 = find_G[0][0]
            col_G1 = find_G[1][0]
            row_G2 = find_G[0][1]
            col_G2 = find_G[1][1]
    return [array_lines,result]

if __name__ == '__main__':
    #Take the input string
    raw_input = [input("input:")]
#    if(raw_input == ""):
#        input_string = 'lrud'
#        win_values=input_string
#        perms = [''.join(p) for p in product(input_string, repeat=4)]
#    else:
#        input_string = raw_input
#        perms = [input_string]
    with open("Input.txt","r") as input_file:
        line_1 = input_file.readlines()
        
    # Finding number of inputs for given row to identify the array size
    first_line = list(line_1[0])
    split_list = len(first_line)-2
    
    #Asserting if the width of the given matrix is below 10
    assert split_list <= 10, "Square matrix size cannot exceed 10"
    list_lines=[]
    for i in range(split_list):
        lines = list(line_1[i])
        lines = lines[0:split_list]
        list_lines.append(lines)
            
    #    Converting the given input to an array     
    array_lines = np.reshape(list_lines,(split_list,split_list))
    array_lines_mod =0
#    array_lines_mod = array_lines
#    unchanged_array = array_lines
    
    #Finding the locations of two Guards and Brynjolf 
    
    #In this problem, since it was no where mentioned I considered there are only two guards
    
    
#    print(perms)
    input_string = 'lrud'
    chance_to_win = False
    win_values=input_string
#    perms =['lu']
    perms = [''.join(p) for p in product(input_string, repeat=4)]
    perms = raw_input+perms
    j=0
    for value in perms:
        flag = True
        if(perms[0] == ''):
            array_lines = np.reshape(list_lines,(split_list,split_list))
            final_array = array_lines
        else:
            if( j != 1):
#                print(array_lines_mod)
#                print(j)
                if(j==0):
                    final_array = array_lines
#                    print(final_array)
                else:
                    final_array = deepcopy(array_lines_mod)
            elif(j == 1):
                
                array_lines_mod = deepcopy(final_array)
#                print(array_lines_mod)
#                print("Here")
        j=j+1    
#        print(value)
        for i in range (len(value)):
#            print(i,value[i])
            if(value[i] == "l"): 
                p = 0
                n = -1
            elif(value[i] == "r"):
                p = 0
                n = 1
            elif(value[i] == "u"):
                p = -1
                n = 0
            elif(value[i] == "d"):
                p = 1
                n = 0
        #    mod_list_BG = make_list_BG(p,n,list_BG)
#            print("Here")
            final_array_result = find_route(flag,final_array,p,n)
            if(final_array_result[1] == "win"):
#                print("HERE win")
#                print(final_array_result[0])
                if(len(win_values)>len(value[0:i+1])):
                    chance_to_win = True
                    win_values = value[0:i+1]
                
                break
            elif(final_array_result[1] == "lose"):
#                print("HERE lose")
#                print(final_array_result[0])
#                print("Lose: executed",i+1,"moves out of",len(input_string),"moves")
                break
            else:
                final_array = final_array_result[0]
#                print(final_array, "HHHH")
#                if(i == len(input_string)-1):
#                    break
#                    print(final_array_result[0])
#                    print("Undecided: executed",i+1,"moves out of",len(input_string),"moves")
    if(chance_to_win == True):
        print("Win:",win_values)
    else:
        print("Struck: no way to win")
        