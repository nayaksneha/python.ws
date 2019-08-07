import re

data = "1001 DBMS 20   1002 JS 23    1003 SQL 15"

#lst = re.split(r"\s+",data)
#print(lst)

#lst = re.split("\d{4}",data)
#print(lst)
lst = re.findall("[A-z]+",data)

print(lst)

lst = re.findall("(\d{4})\s([A-z]*)\s+(\d{2})",data)
print(lst)


d = "sneha is in 560070 works at banglore and krish is 522612 works at guntur "
lst = re.findall("\d{6}",d)
print(lst)
li = re.findall(r"at\s+(.*?)\s",d)
print(li)
l = re.findall(r"at\s+([A-z]+)",d)
print(l)



dt = "house number 198 and pincode 560070"
res = re.search("\d+",dt)
print(dt[res.start():res.end()])
print(res.group())



data = "blue shape red toy green"
res = re.sub('(blue|red|green)', 'color' ,data)
print(res)
