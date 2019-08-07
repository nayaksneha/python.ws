import csv 

ws_lst = [
        {"id":1001,"name":"python","year":"2019","status":1,"company":"heraizen"},
        {"id":1002,"name":"web","year":"2018","status":1,"company":"spaneos"
]

try:
    with open("ws.csv","w",newline='') as file:
        headings = ["id","name","year","status","company"]
        obj = csv.DictWriter(file,fieldnames=headings)
        obj.writeheader()
        obj.writerows(ws_lst)
            #line = f'{d["id"]},{d["name"]},{d["year"]},{d["status"]},{d["company"]}\n'
            #file.write(line)
except Exception as r:
    print(str(r))