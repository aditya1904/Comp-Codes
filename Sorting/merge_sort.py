#!/usr/bin/python3

# https://www.hackerrank.com/challenges/ctci-merge-sort/problem

def merge_sort(arr):
    global count
    if len(arr)>1:
        split_point = int(len(arr)/2)
        left_arr = arr[:split_point]
        right_arr = arr[split_point:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        le_arr_len = len(left_arr)
        ri_arr_len = len(right_arr)
        l_itr = 0
        r_itr = 0
        arr_itr = 0

        while l_itr < le_arr_len and r_itr < ri_arr_len:
            if left_arr[l_itr] <= right_arr[r_itr]:
                arr[arr_itr] = left_arr[l_itr]
                l_itr += 1
            else:
                arr[arr_itr] = right_arr[r_itr]
                r_itr += 1
                count += le_arr_len - l_itr
            arr_itr += 1

        while l_itr < len(left_arr):
            arr[arr_itr] = left_arr[l_itr]
            l_itr += 1
            arr_itr += 1

        while r_itr < len(right_arr):
            arr[arr_itr]= right_arr[r_itr]
            r_itr += 1
            arr_itr += 1
    return count

def countInversions(arr):
    global count
    count = 0
    merge_sort(arr)
    return count

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))
        result = countInversions(arr)

        print(result)
