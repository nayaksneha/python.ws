from openpyxl import Workbook
import openpyxl as pyxl

wb = Workbook()
sheet = wb.active
data = [
    ('id','name','year','status','company'),
    (1001,"python",2019,1,"heraizen"),
    (1002,"web",2018,1,"spaneos")
]
for row in data:
    sheet.append(row)
wb.save("ws.xlsx")