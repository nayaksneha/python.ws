def searchLinear(lst,ele):
    index = 0
    for i in lst:
        if i == ele:
            return index
        index +=1 
    return False
ele = 6
res = searchLinear([1,2,3,4,5,6,7,8],ele)
if res:
    print(f"element {ele} is found")
else:
    print(f"element {ele} not found")
