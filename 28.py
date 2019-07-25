names = ["PKM","ALN","PVR","PKM","ALN","NVR"]
c_nme = {}
for name in names:
    if c_nme.get(name) == None:
        c_nme[name] = 1
    else:
        c_nme[name]+=1
print(c_nme)