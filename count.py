# # n = int(input())
# # arr = list(map(int, input().strip().split()))[:n]
# #
# # def count_sort():
# #     max_val = max(arr)
# #     m = max_val + 1
# #     count = [0] * m
# #
# #     for a in arr:
# #         count[a] += 1
# #         return arr
# #     i = 0
# #     for a in range(m):
# #         for c in range(count[a]):
# #             arr[i] = a
# #             i += 1
# #             return arr
# #         return arr
# #
# #
# # print(arr)
# #
# # # def counting(data):
# # #     counts = [0 for i in xrange(max(data) + 1)]
# # #
# # #     for el in data:
# # #         counts[el] += 1
# # #
# # #     for index in xrange(1, len(counts)):
# # #         counts[index] = counts[index - 1] + counts[index]
# # #
# # #     L = [0 for loop in xrange(len(data) + 1)]
# # #     for el in data:
# # #         index = counts[el] - 1
# # #         L[index] = el
# # #         counts[el] -= 1
# # #
# # #     return L
# # #
# # #
# def countingSort(A, k):
#
# 	# Create empty list for the sorted list
# 	B = [0 for el in A]
#
# 	# Initialise counter with zeroes
# 	C = [0 for el in xrange(0, k+1)]
#
# 	# Count elements
# 	for i in xrange(0, len(A)):
# 		C[A[i]] += 1
#
# 	# How many elements are equal or lower?
# 	for i in xrange(1, k + 1):
# 		C[i] += C[i - 1]
#
# 	# The actual sorting
# 	for j in xrange(len(A)-1, 0 - 1, -1):
# 		tmp = A[j]
# 		tmp2= C[tmp] -1
# 		B[tmp2] = tmp
# 		C[tmp] -= 1
# 	return B
#
# """ Usage example """
# print countingSort([6,0,2,0,1,3,4,6,1,3,2], 6)

def counting_sort(l):
    k = max(l) + 1
    n = len(l)
    count = [0] * k

    for x in l:
        count[x] += 1

    total = 0
    for x in range(k):
        old = count[x]
        count[x] = total
        total += old

    result = [0] * n
    for x in l:
        result[count[x]] = x
        count[x] += 1

    return result


def print_list(l):
    for i, x in enumerate(l):
        print(i, x)


def counting_sort_print(l):
    k = max(l) + 1
    n = len(l)
    count = [0] * k

    print('Input:')
    print_list(l)

    for x in l:
        count[x] += 1



    total = 0
    for x in range(k):
        old = count[x]
        count[x] = total
        total += old


    result = [0] * n
    for x in l:
        result[count[x]] = x
        count[x] += 1

    print('Result:')
    print_list(result)

    return result

if __name__ == '__main__':
    """Example"""

    l1 = [5, 4, 3, 2, 1, 0]
    l2 = [5, 5, 4, 3, -3, 0, 1, 1]

    counting_sort_print(l1)
    counting_sort_print(l2)