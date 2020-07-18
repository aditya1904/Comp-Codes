#!/bin/python3

def median(exp, d, even):
    if even:
        med = (exp[int(d / 2)] + exp[int(d / 2 + 1)]) / 2
    else:
        med = exp[int(d / 2)]
    return med

## insert function inserts a new element in the previously sorted array of d days
def insert(arr, i):
    while arr[i-1] > arr[i] and i > 0:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        i = i - 1
    return arr

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    if d % 2 == 0:
        even = True
    else:
        even = False
    frauds = 0
    initial_array = expenditure[0:d]
    initial_array.sort()
    ## Counting frauds for the first d records##
    medi = median(initial_array, d, even)
    if expenditure[d] >= 2 * medi:
        frauds += 1
    new_arr = initial_array
    for day in range(d+1, len(expenditure)):
        new_arr = new_arr[1:] + [expenditure[day-1]]
        med = median(insert(new_arr, d-1), d, even)  ## insert function inserts a new element in the previously sorted array of d days
        if expenditure[day] >= 2 * med:
            frauds += 1
    return frauds


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)

