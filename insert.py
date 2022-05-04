n = int(input())
arr = list(map(int, input().strip().split()))[:n]

for i in range(1, len(arr)):
    while arr[i-1] > arr[i] and i > 0:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        i -= 1
    
print(arr)