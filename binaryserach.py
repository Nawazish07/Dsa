def binarysearch(key):
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        print(mid)
        
        if arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            print("key found at", mid)
            return
    
    print("search exhausted, key not found")

binarysearch(1)
  