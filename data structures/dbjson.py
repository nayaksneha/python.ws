import json

ws_lst = [
        {"id":1001,"name":"python","year":"2019","status":1,"company":"heraizen"},
        {"id":1002,"name":"web","year":"2018","status":1,"company":"spaneos"}
]

try:
    with open("ws.json","w",newline='') as file:
        json.dump(ws_lst,file,indent=4)
        print(json.dumps(ws_lst))

except Exception as r:
    print(str(r))