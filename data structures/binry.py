def binarySearch(lst,key):
    l=0
    h=len(lst)-1
    while l<=h:
        mid = (l +h)//2
        if lst[mid]==key:
            return mid 
        elif key > lst[mid]:
            l = mid+1
        else:
            h = mid-1
    return -1
ele = 5
res = binarySearch([1,4,3,9,5,6,2,8],ele)
if res == -1:
    print(f"element {ele} is not found")
else:
    print(f"element {ele} found at {res} ")
    
