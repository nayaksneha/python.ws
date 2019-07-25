from qustion import Question

class Questions:

    qustn = []


    @classmethod
    def loadqustn(cls):
        with open("qust.txt") as file:
            data = file.readlines()
            for line in data:
                q = line.split(",")
                cls.qustn.append(Question(*q))

    @classmethod
    def begin_quiz(cls):
        cls.loadqustn()
        print(f"total qustions found :{len(cls.qustn)}")
        crct = 0
        wrng = 0
        for i,qustn in enumerate(cls.qustn):
            print(f"{i+1}.{qustn}")
            ch = input("enter your choice [A,B,C,D] ")
            if ch == qustn.c_ans.strip():
                crct+=1
            else:
                wrng+=1

        cls.show_result(crct,wrng)



    @classmethod
    def show_result(cls,crct,wrng):
        print("*"*50)
        total_q = len(cls.qustn)
        print(f"total questions : {total_q}")
        print(f"number of correct answer:{crct}")
        print(f"number of wrng answer :{wrng}")
        perc = ((crct)/total_q)*100
        print(f"the percentage is :{perc}")
        if perc >= 65:
            print("congratulation")
        else:
            print("better luck next time")