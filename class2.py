class Employee:

    def __init__(self,empno,ename,qual,sal,dept_nme):
        self.empno = empno
        self.ename = ename
        self.qual = qual
        self.sal = sal
        self.dept_nme = dept_nme

    def show_info(self):
        print(f"{self.empno} - {self.ename} - {self.qual} - {self.sal} -{self.dept_nme}")

    def inc_sal(self,inc_amount):
        self.sal += inc_amount
        print(f"{self.ename} salary after increment {self.sal} ")
        