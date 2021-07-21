'''
Name: AYTIJHA CHAKRABORTY
BTech (CSE-AI/ML)   Sem: 5
Class Roll: 17      Sec: K
University Roll: 1914009

Problem Statement:
An Array and a key element will be provided. Return:
    1. If the key is Present/Absent
    2. No. of comparisons made to find the key
Search the array in time O(log N)
'''
import math #for floor() function to calculate mid

def BinarySearch(arr, low, high, key, count): #Binary Search implementation
    if low <= high: #to make sure that subarray is still valid
        mid = math.floor((low + high) / 2) #mid value of a subarray
        count = count + 1 #incrementing count for each subarray
        if arr[mid] == key:
            print('Present', count) #when element found
        elif arr[mid] > key: #to search Left subarray
            return BinarySearch(arr, low, mid-1, key, count)
        elif arr[mid] < key: #to search Right subarray
            return BinarySearch(arr, mid+1, high, key, count)
    else:
        print('Absent', count) #when element not found

for _ in range(int(input())): #for a variable no. of test cases
    n = int(input()) #size
    arr = list(map(int, input().split())) #split n space-separated inputs and convert them into an array
    arr.sort() #to sort the array, since Binary Search only works on Sorted inputs
    key = int(input()) #element to be searched
    BinarySearch(arr, 0, n-1, key, 0) #function call with count initialised to 0