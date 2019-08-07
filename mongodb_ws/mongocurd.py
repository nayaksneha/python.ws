import pymongo  as pm 

conn = pm.MongoClient("mongodb://localhost:27017")
db = conn["fc"]

collection = db["faculty"]

def add_new_faculty():
    data = {

    "name" : "Sneha",
    "age" : 38.0,
    "gender" : "F",
    "exp" : 12.0,
    "address" : {
        "city" : "Bangalore",
        "state" : "Karnataka"
    },
    "subjects" : [ 
        "JAVA", 
        "DBMS"
    ],
    "type" : "Full Time",
    "qualification" : "Ph.D",
    "rating" : [ 
        5.0, 
        6.0, 
        7.0
    ],
    "deptno" : 10.0,
    "salary" : 5000.0,
    "bonus" : 2000.0
          }
    d = collection.insert_one(data)
    print(str(d))
        
def add_subject_to_faculty():
    d = collection.update_one({"name":"Sneha"},{"$push":{"subjects":"CN"}})
    print(str(d))
def remove_subject_from_faculty():
    d = collection.update_one({"name":"Sneha"},{"$pull":{"subject":"CN"}})
    print(str(d))
def increment_exp_by_one_year():
    d = collection.update_one({"name":"Sneha"},{"$inc":{"exp":1}})
    print(str(d))
def update_qualification():
    d = collection.update_one({"name":"Sneha"},{"$set":{"qualification":"Msc"}})
    print(str(d))
def total_duration_by_faculty():
    pipe = [{"$group":{"_id":"null", "res":{"$sum":"$exp"}}},{"$project":{"_id":"0"}}]
    print(collection.aggregate(pipe))
def subject_with_faclty_name():
    d = collection.aggregate([{"$project":{"name":"$name","subjects":1, "_id":0}}])
    for i in d:
        print(i)
def delete_faculty():
    collection.remove({"name":"Latha"})

