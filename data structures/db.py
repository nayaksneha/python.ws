d_lst = [
    {"id":1001,"name":"python","year":"2019","status":1,"company":"heraizen"},
    {"id":1002,"name":"web","year":"2018","status":1,"company":"spaneos"},
    #[1003,"java",2020,1,"heraizen"]
]

try:
    with open("ws.txt","w") as file:
        for d in d_lst:
            line = f'{d["id"]},{d["name"]},{d["year"]},{d["status"]},{d["company"]}\n'
            file.write(line)
except Exception as r:
    print(str(r))