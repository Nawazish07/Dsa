def binsearch(arr,key,low,high):
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        
        if arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
    return low


def binsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        pos=binsearch(arr,key,0,i-1)

        arr=arr[:pos]+[key]+arr[pos:i]+arr[i+1:]
    return arr

arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
sorted_arr = binsort(arr)
print("Sorted array:", sorted_arr)