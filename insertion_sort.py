#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:10:52 2021

@author: yogisharo
"""

arr = [5,2,4,6,1,3]

def insertion_sort(arr):
    #Store the range between index
    index_to_sort = range(0,len(arr))
    #Get the value to do sort
    iter_ = 1
    for i in index_to_sort:
        value_to_sort = arr[i]
        
        #left value should be larger than right value
        #Make sure python index starts at 0
        #Swap variable if condition met
        while arr[i-1] > value_to_sort and i >0 : 
            arr[i-1] , arr[i] = arr[i] , arr[i-1]
            i = i-1 #Doing incremental stepping of the list
            print ("step :", iter_, " ", arr)
            iter_ = iter_ + 1
    return arr
            
            

insertion_sort(arr)
        