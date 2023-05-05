def BinarySearch(arr,key,start,end):
    while start<=end:
        mid=(start+end)//2
        if arr[mid][1]==key:
            return True
        if arr[mid]>key:
            end=mid-1
        else:
            start=mid+1
    return False