'''
Name: AYTIJHA CHAKRABORTY
BTech (CSE-AI/ML)   Sem: 5
Class Roll: 17      Sec: K
University Roll: 1914009

Problem Statement:
Given an array of non-negative integers, design an algorithm and a program to count the 
number of pairs of integers such that their difference is equal to a given key, K.
'''

def DiffSearch(arr, low, high, key):
    if high >= low:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return DiffSearch(arr, mid+1, high, key)
        else:
            return DiffSearch(arr, low, mid-1, key)
    else:
        return -1

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    diff = int(input())
    count = 0
    for i in range(0, n-1):
        if (DiffSearch(arr, i+1, n-1, arr[i]+diff) != -1):
            count += 1
    print(count)