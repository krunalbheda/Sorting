n = int(input())
arr = list(map(int, input().strip().split()))[:n]

def Division(arr):
    i = 0
    j = 0
    k = 0
    if len(arr) > 1:
        middle = (0 + (len(arr)//2))
        l = arr[0:middle]
        r = arr[middle:]
        Division(l)

print(arr)

