'''
Name: AYTIJHA CHAKRABORTY
BTech (CSE-AI/ML)   Sem: 5
Class Roll: 17      Sec: K
University Roll: 1914009

Problem Statement:
Given a sorted array of positive integers, design an algorithm and implement it using a program to 
find three indices i, j, k such that arr[i] + arr[j] = arr[k]
'''

for _ in range(int(input())): #for a variable no. of test cases
    n = int(input()) #size of input array
    arr = list(map(int, input().split())) #split n space-separated inputs and convert them into an array
    #arr.sort()
    count = 0 #to count if atleast one triplet has been found
    for k in range(n-1, -1, -1): #backwards iteration for RHS variable
        i, j = 0, k-1 #initialising i and j as the front and rear of the subarray (from 0 to k-1)
        while (i < j) and count != 1: #constraints to prevent infinite loop
            if (arr[i] + arr[j] == arr[k]):
                print(arr[i], arr[j], arr[k]) #triplet found
                count = 1 #to prevent further searching
            elif (arr[i] + arr[j] < arr[i]): #if sum < RHS, increment front index
                i += 1
            else: #if sum > RHS, decrement rear index
                j -= 1
    if count == 0: #if no triplet was found
        print("No sequence found")