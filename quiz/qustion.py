class Question:

    def __init__(self,qdata,op1,op2,op3,op4,c_ans):
        self.qdata = qdata
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.c_ans = c_ans


    def __str__(self):
        return f"{self.qdata}\n A.{self.op1} B.{self.op2} C.{self.op3} D.{self.op4}"

