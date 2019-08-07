try:
    with open("file.txt") as fin, open("file2.txt","w") as fon:
        lines = fin.readlines()
        lines = [l.upper() for l in lines]
        fon.writelines(lines)
except Exception  as a:
    print(f"file not found :{a}")