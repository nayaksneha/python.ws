class Queue:

    def __init__(self,):
        self.st = []

    def push(self,ele):
        #ele = input("enter the element")
        #push.append(ele)
        self.st.append(ele)

    def pop(self):
        if self.is_empty():
            print("queue empty")
        else:
            ele = self.st.pop(0)
            print(f"elemnt {ele} is popped")

    def search(self,sreele):
        if self.is_empty():
            print("queue empty")
        else:
            for index,ele in enumerate(self.st):
                if ele == sreele:
                    return index
            return -1                
                



    def show(self):
        if self.is_empty():
            print("queue empty")
        else:
            print(self.st)

        
    
    def is_empty(self):
        return len(self.st) == 0



if __name__ == "__main__":
    st = Queue()
    #op_dict = {1:st.push(),2:st.pop(),3:st.search(),4:st.show,5:exit}
    while True:
        print("1.push 2.pop 3.search 4.show 5.exit")
        try:
            ch = int(input("enter your choice"))
            if ch == 1:
                ele = input("enter ele")
                st.push(ele)
            elif ch ==2:
                st.pop()
            elif ch == 3:
                ele = input("enter ele")
                res = st.search(ele)
                if res !=-1:
                    print(f"elemnt found at {res}")
                else:
                    print("element not found")
            elif ch == 4:
                st.show()
            elif ch == 5:
                exit()
            else:   
                raise ValueError()
        except (ValueError,TypeError):
            print("enter the only number between 1 to 5:")




            
            

