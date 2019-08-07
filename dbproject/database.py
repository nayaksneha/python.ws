import sqlite3 

host_name = "data.db"
def create_table():
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("create table student (regno integer primary key,name text,sem integer,placed integer)")
        #conn.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def add_new_student(regno,name,sem,placed):
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("insert into student(regno,name,sem,placed) values(?,?,?,?)",(regno,name,sem,placed))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close


def show_student():
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("select regno,name,sem,placed from student")
        rows = cursor.fetchall()
        for row in rows:
            status = "placed" if row[3] == 'yes' else "not placed"
            print(f"{row[0]},{row[1]},{row[2]} and {status}")
    except Exception as e:
        print(e)
    finally:
        conn.close


def update_student(regno,placed):
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("update student set placed = ? where regno=?",(placed,regno))
        #cursor.execute("insert into student(regno,name,sem,placed) values(?,?,?,?)",(regno,name,sem,placed))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close



def show_det_student(regno):
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("select regno,name,sem,placed from student where regno=?",(regno,))
        row= cursor.fetchone()
        if row:
            #print(f"{row[0]},{row[1]},{row[2]}")
            status = "placed" if row[3] == 'yes' else "not placed"
            print(f"{row[0]},{row[1]},{row[2]} and {status}")
        else:
            print(f"student not found:{regno}")
    except Exception as e:
        print(e)
    finally:
        conn.close


#create_table()
#add_new_student(1003,'joy',7,'yes')
#show_student()
update_student(1001,'yes')
show_det_student(1001)