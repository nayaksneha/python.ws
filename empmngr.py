from class2 import Employee

lst_emp = []

def load_emp():
    with open("emp.txt") as f:
        fdata = f.readlines()
        for data in fdata:
            edata = data.strip("\n").split(",")
            empno = int(edata[0])
            ename = edata[1]
            qual = edata[2]
            sal = int(edata[3])
            dept_nme = edata[4]
            emp = Employee(empno,ename,qual,sal,dept_nme)
            lst_emp.append(emp)
    print(f"total count : {len(lst_emp)}")

def showDNme():
    dnames = set(map(lambda emp:emp.dept_nme,lst_emp))
    for name in dnames:
        print(name)

def shoAllQual():
    quali = set(map(lambda emp:emp.qual,lst_emp))
    for qual in quali:
        print(qual)

def maxSal():
    max_sal = max(list(map(lambda x:x.sal,lst_emp)))
    lst = list(filter(lambda x: x.sal == max_sal,lst_emp))
    for emp in lst:
        emp.show_info()

def showEmpCountByNme():
    pass


def showTtlSalByDeptnme():
    pass

def showEmpContByQual():
    pass


load_emp()
print("all dept names: ")

showDNme()
print("all qualification")

shoAllQual()

maxSal()


