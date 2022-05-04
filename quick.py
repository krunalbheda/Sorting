# quick sorting
# user given the n number of array
n = int(input())
arr = list(map(int, input().strip().split()))[:n]

def quick_sort(array):
    sort(array, 0, len(array) - 1)


def sort(array, l, r):
    if l >= r:
        return array
    pivot = array[(l + r) // 2]
    index = partition(array, l, r, pivot)

    sort(array, l, index - 1)
    sort(array, index, r)


def partition(array, l, r, pivot):
    while l <= r:
        while array[l] < pivot:
            l += 1
        while array[r] > pivot:
            r -= 1

        if l <= r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1

    return l

quick_sort(arr)

print(arr)