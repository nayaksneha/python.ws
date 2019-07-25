'''Write a program to add the elements of 2 arrays that are of the same dimension'''
lst1 = [1,2,3,4]
lst2 = [5,6,7,8]
lst3 = []
lst3 = list(map(lambda x,y:x+y,lst1,lst2))
print(lst3)