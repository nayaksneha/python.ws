class MaxLimitError(Exception):
    def __init__(self,message):
        self.message = message

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"

c =0
def login(usnme,passwrd):
    global c
    if usnme == "abc" and passwrd == "cba":
        print("login successful")
    else:
        print("unsccessful")
    c+=1
    if c>2:
        raise MaxLimitError("you have reached maximum number 0")

login("abc","cba")
login("a","c")
login("ABC","CBA")

