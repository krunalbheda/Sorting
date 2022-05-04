# Selection sorting
# user given the n number of array

n = int(input())
A = list(map(int, input().strip().split()))[:n]


# A = list(map(int,input("enter the nuber").split()))

for i in range(len(A)):
        min = i

        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j

        A[i], A[min] = A[min], A[i]

#print the Array
print(A)

