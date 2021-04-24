# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def bubble_sort(arr):
    #Get range of the array
    iter_ = 0
    n = len(arr)
    #Scans through all 1st array elements
    for i in range(n-1):
    #range(n) is outside the list


        for j in range(n-i-1):
        #Scans for 2nd value for comparison 
        #Swap if the earlier value larger than the next one
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
            print("step :", iter_, " ",arr)
            iter_ += 1

arr = [20,19,11,5,1,8]

print(bubble_sort(arr))


print ("Final Sorted Array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 