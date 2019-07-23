import random as rn 
lst = []
for i in  range(1,101):
    lst.append(rn.randint(1,1000))

new_lst = []
for j in lst:
    if j % 3 == 0 and j%6==0 and j %9!=0:
        new_lst.append(j)
print(new_lst)



