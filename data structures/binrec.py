def binarySearch(lst,l,h,key):
    if l<=h:
        mid = (l +h)//2
        if key == lst[mid]:
            return mid
        
        elif key>lst[mid]:
            return binarySearch(lst,mid+1,h,key)
        else:
            return binarySearch(lst,l,mid-1,key)
    return -1

ele = 3
res = binarySearch([1,4,3,9,5,6,2,8],0,9,ele)
if res == -1:
    print(f"element {ele} is not found")
else:
    print(f"element {ele} found at {res} ")