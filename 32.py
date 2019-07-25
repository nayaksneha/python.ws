'''	Write a program to find the sum of squares of only the even numbers in the given list. (Hint: Use the methods filter, map, reduce.)
Example:Input:list = [1, 2, 3, 4, 5, 6, 7, 8, 9]'''
from functools import reduce
lst1 = [1,2,3,4,5,6,7,8,9]

lst2 = reduce(lambda x,y:x+y, list(filter(lambda x:x%2 == 0,list(map(lambda x: x*x,lst1)))))
print(lst2)
