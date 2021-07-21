'''
Name: AYTIJHA CHAKRABORTY
BTech (CSE-AI/ML)   Sem: 5
Class Roll: 17      Sec: K
University Roll: 1914009

Problem Statement:
An Array and a key element will be provided. Return:
    1. If the key is Present/Absent
    2. No. of comparisons made to find the key
Search the array in time O(N)
'''

for _ in range(int(input())): #for a variable no. of test cases
    n = int(input()) #size
    arr = list(map(int, input().split())) #split n space-separated inputs and convert them into an array
    key = int(input()) #element to be searched
    count = 0 #to count the number of comparisons performed
    for i in arr: #Linear Search implementation
        count += 1 #incrementing count for each subarray
        if i==key:
            print('Present', count)
            break
    else: #when element not found
        print('Absent', count)

''' Inputs:
3
8
34 35 65 31 25 89 64 30
89
5
977 354 244 546 355
244
6
23 64 13 67 43 56
63
'''