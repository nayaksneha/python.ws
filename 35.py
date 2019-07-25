'''Write a program to determine the work hours of the day entered based on the timetable provided below'''

lst = ['mon','tus','wed','thr','fry','sat','sun']

wek1 = [3,3,3,3,3,3,0]
wek2 = [2,2,2,2,2,1,0]
wek3 = [2,2,2,1,1,0,0]

inp = input("enter the day")
inp = inp.lower()
li = lst.index(inp)
c = [i for i in zip(wek1,wek2,wek3)]
print(c[li])