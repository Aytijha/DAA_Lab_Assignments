'''
Name: AYTIJHA CHAKRABORTY
BTech (CSE-AI/ML)   Sem: 5
Class Roll: 17      Sec: K
University Roll: 1914009

Problem Statement:
An Array and a key element will be provided. Return:
    1. If the key is Present/Absent
    2. No. of comparisons made to find the key
Search the array in time < O(N), and jump indices in this fashion: arr[0], arr[2], arr[4], .... arr[2^k]
Once a block is reached such that: arr[2^k] < key < arr[2^(k+1)], perform a Linear Search in that block
'''

def JumpSearch(arr , key , n, count):
    jump = 2 #block size to be jumped
    low = 0
    while arr[int(min(jump, n)-1)] < key: #Finding the block where element lies
        count += 1 #incrementing counter for each block jump
        low, jump = jump, jump*2 #updating low, high values
        if low >= n: #edge case when we exceed block limit, i.e. go outside array bounds
            print('Absent', count)
            break
    while low <= n and arr[int(low)] < key: #doing a linear search for key in block beginning with low
        count += 1
        low += 1
        if low == min(jump, n): #if we reached next block or end of array, element is not present
            print('Absent', count)
            return
    if low <= n and arr[int(low)] == key: #if element is found within the block iteration
        print('Present', count)
        return
    else:
        print('Absent', count) #if key is not found within the block iteration

for _ in range(int(input())): #for a variable no. of test cases
    n = int(input()) #size
    arr = list(map(int, input().split())) #split n space-separated inputs and convert them into an array
    arr.sort() #to sort the array, since Jump Search only works on Sorted inputs
    key = int(input()) #element to be searched
    count = 0 #to count the number of comparisons performed
    if arr[0] == key: #initializing low and high pointers to define bounds for the Linear Search
        print('Present', 1)
        continue
    if arr[0] > key:
        print('Absent', 1)
    JumpSearch(arr, key, n, 1) #function call with count initialised to 0