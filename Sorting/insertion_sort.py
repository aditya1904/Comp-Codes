#!/usr/bin/python3

def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            count += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return count

if __name__ == '__main__':
    prices = list(map(int, input().rstrip().split()))
    insertion_sort(prices)
    print(prices)