import json

try:
    with open("ws.json","r") as file:
        ws_lst = json.load(file)
        for w in ws_lst:
            print(f"id:{w['id']} name:{w['name']} year:{w['year']}")

except Exception as r:
    print(str(e))
