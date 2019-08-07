def bubuleSort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]

l = [3,4,5,6,2]
bubuleSort(l)
print(l)