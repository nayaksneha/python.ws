try:
    with open("file.txt") as f:
        lines = f.readlines()
        cline ,cword = 0 ,0
        cline = len(lines)
        for line in lines:
            cword+= len(line.split(" "))
            
        print(f"the count and word is : {cline},{cword}")
            

except Exception as e:
    print(f"file not found please check path {e}")