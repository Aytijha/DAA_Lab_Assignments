'''
Name: AYTIJHA CHAKRABORTY
BTech (CSE-AI/ML)   Sem: 5
Class Roll: 17      Sec: K
University Roll: 1914009

Problem Statement:
Given a sorted array of positive integers containing few duplicate elements,
design an algorithm and implement it using a program to find:
    Whether the given key element is present in the array or not.
    If present, then also find the number of copies of given key.
Time Complexity = O(log n)
'''

def FrontIndex(arr, low, high, key):
    if(high >= low): #to make sure that subarray is still valid
        mid = ((low + high) // 2) #mid value of a subarray
        if((mid == 0 or arr[mid-1] < key) and arr[mid] == key): #when arr[mid] is the foremost occurence of the key
            return mid                                          #because (elements to it's left is < key) in the sorted array
        elif(arr[mid] < key): #to search right subarray
            return FrontIndex(arr, mid+1, high, key)
        else: #to search left subarray
            return FrontIndex(arr, low, mid-1, key)
    return -1 #when key is not present

def RearIndex(arr, low, high, key):
    if(high >= low): #to make sure that subarray is still valid
        mid = (low + high) // 2 #mid value of a subarray
        if((mid == n-1 or arr[mid+1] > key) and arr[mid] == key): #when arr[mid] is the rearmost occurence of the key
            return mid                                            #because (elements to it's right is > key) in the sorted array
        elif(arr[mid] > key): #to search left subarray
            return RearIndex(arr, low, mid-1, key)
        else: #to search right subarray
            return RearIndex(arr, mid+1, high, key)
    return -1 #when key is not present

for _ in range(int(input())): #for a variable no. of test cases
    n = int(input()) #size of input array
    arr = list(map(int, input().split())) #split n space-separated inputs and convert them into an array
    arr.sort() #to sort the array, since Binary Search only works on Sorted Array
    key = int(input()) #element to be searched
    front = FrontIndex(arr, 0, n-1, key) #get the frontmost occurence index of key
    rear = RearIndex(arr, 0, n-1, key) #get the rearmost occurence index of key
    if front != -1 and rear != -1:
        print(key, "-", (rear-front+1)) #no. of occurences
    else:
        print("Key not present") #key not found in array