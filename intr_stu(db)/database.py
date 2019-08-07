import time
import random as rn
import dbcontext as db
from models import Internship , Student , Company,Report,StudentCount
from beautifultable import BeautifulTable

def _get_new_id():
    t_obj = time.localtime()
    new_id = rn.randint(1000,9900) + (t_obj.tm_min + t_obj.tm_hour + t_obj.tm_sec)
    return new_id

def add_internship(iname,company,i_year):
        id = _get_new_id()
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("insert into internship(id,iname,company,i_year,status) values(?,?,?,?,?)",(id,iname,company,i_year,1))
                        print(f"Internship is added successfully with id:{id}")
        except Exception as e:
                print(str(e))

def view_all_internships():
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("select id,iname,company,i_year,status from internship")
                        rows = cursor.fetchall()
                        intern_pro_lst = [Internship(*row) for row in rows]
                        _view_internship_list(intern_pro_lst)
        except Exception as e:
                print(str(e))

def search_internship_by_name(name):
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("select id,iname,company,i_year,status from internship where iname LIKE ?",(name,))
                        rows = cursor.fetchall()
                        intern_pro_lst = [Internship(*row) for row in rows]
                        _view_internship_list(intern_pro_lst)
        except Exception as e:
                print(str(e))
            
def change_status_internship(id,status):
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("update internship set status=? where id=?",(status,id))
                        print("update status is done")
        except Exception as e:
                print(str(e)) 


def delete_internship(id):
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("delete from internship where id=?",(id,))
                        print("intership deleted")
        except Exception as e:
                print(str(e))

def add_student(usn,name,sem,placed):
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("insert into Student (usn,name,sem,placed) values(?,?,?,?)",(usn,name,sem,placed))
                        print("added successfully")
        except Exception as e:
                print(str(e))

def view_all_reg_student():
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("select usn,name,sem,placed from Student")
                        rows = cursor.fetchall()
                        stu_pro_lst = [Student(*row) for row in rows]
                        _view_student_list(stu_pro_lst)
        except Exception as e:
                print(str(e))

def search_student_by_name(name):
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("select usn,name,sem,placed from Student where name=?",(name,))
                        rows = cursor.fetchall()
                        stu_pro_lst = [Student(*row) for row in rows]
                        _view_student_list(stu_pro_lst)
        except Exception as e:
                print(str(e))

def update_student(sid,sem):
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("update Student set sem=? where usn=?",(sem,sid))
                        #rows = cursor.fetchone()
                        #stu_pro_lst = [Student(*row) for row in rows]
                        #_view_student_list(stu_pro_lst)
                
                        print("update is done")
        except Exception as e:
                print(str(e))


def delete_student(sid):
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("delete from Student where usn=?",(sid,))
                        print("delete done")
        except Exception as e:
                print(str(e))


def company_ws_count():
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("select company,count(*) from internship group by company")
                        rows = cursor.fetchall()
                        company_pro_lst = [Company(*row) for row in rows]
                        _view_company_count(company_pro_lst)
        except Exception as e:
                print(str(e))
def student_ws_count():
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("select company,count(*) from internship group by company")
                        rows = cursor.fetchall()
                        company_pro_lst = [Company(*row) for row in rows]
                        _view_company_count(company_pro_lst)
        except Exception as e:
                print(str(e))

def ws_student_reports():
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("select r.usn ,s.name ,i.iname, i.company, i.i_year from Registration r JOIN Student s ON (s.usn = r.usn) JOIN Internship i ON (i.id = r.iid) order by r.usn ;")
                        rows = cursor.fetchall()
                        student_report_lst = [Report(*row) for row in rows]
                        _view_student_report(student_report_lst)
        except Exception as e:
                print(str(e))


def reg_stu_internship(iid,usn,status):
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("insert into Registration (iid,usn,status) values(?,?,?)",("iid","usn","status"))
                        print(f"Student registered successfully for internship")
        except Exception as e:
                print(str(e))

def update_stu_internship_status(usn,status):
        try:
                with db.DbContext() as connection:
                        cursor = connection.cursor()
                        cursor.execute("update Registration set status = ? where usn=?",("status","usn"))
                        print("Status updated!")
        except Exception as e:
                print(f"{str(e)}")


def _view_internship_list(lst):
        if lst and len(lst) > 0:
                table = BeautifulTable()
                table.column_headers = ["ID", "NAME", "COMPANAY", "YEAR","STATUS"]
                for l in lst:
                        status = "Comleted" if l.status == 0 else "Going on" 
                        table.append_row([l.id, l.iname, l.company, l.i_year,status])
                print(table)
        else:
                print(f"There are no Intership programms, yet to add...")



def _view_student_list(lst):
        if lst and len(lst) > 0:
                table = BeautifulTable()
                table.column_headers = ["USN", "NAME", "SEM", "PLACED"]
                for l in lst:
                        status = "Placed" if l.placed == 1 else "not placed" 
                        table.append_row([l.usn, l.name, l.sem, status])
                print(table)
        else:
                print(f"There are no student added, yet to add...")



def _view_registered_list(lst):
        if lst and len(lst) > 0:
                table = BeautifulTable()
                table.column_headers = ["IID", "USN", "STATUS"]
                for l in lst:
                        #status = "Not completed" if l.status == 0 else "Completed" 
                        table.append_row([l.iid, l.usn, l.status])
                print(table)
        else:
                print(f"There are no Students registered for any internship!")



def _view_company_count(lst):
        if lst and len(lst) > 0:
                table = BeautifulTable()
                table.column_headers = ["Company", "Count"]
                for l in lst:
                        table.append_row([l.company, l.count])
                print(table)
        else:
                print(f"There are no company taken internship!")


def _view_student_count(lst):
        if lst and len(lst) > 0:
                table = BeautifulTable()
                table.column_headers = ["USN", "NAME","COUNT"]
                for l in lst:
                        table.append_row([l.usn, l.name,l.count])
                print(table)
        else:
                print(f"No student joined any internship!")



def _view_student_report(lst):
        if lst and len(lst) > 0:
                table = BeautifulTable()
                table.column_headers = ["USN", "NAME","INTERNSHIP NAME","COMPANY","YEAR"]
                for l in lst:
                        table.append_row([l.usn, l.name,l.iname,l.company,l.i_year])
                print(table)
        else:
                print(f"No internship conducted yet!") 