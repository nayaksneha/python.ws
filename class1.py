class Car:


    def __init__(self, regno, no_gears): #constructor(dunder method)
            self.regno = regno
            self.no_gears = no_gears 
            self.is_started = False
            self.c_gear = 0
    
    def start(self):
        if self.is_started:
            print(f"{self.regno} already started....")
        else:
            print(f"{self.regno}  started....")
            self.is_started = True


    def stop(self):
        if self.is_started:
            print(f"{self.regno} stopped....")
            self.is_started =  False
        else:
            print(f"{self.regno} already stopped....")
            #self.is_started =  False



    def change_gear(self):
        if self.is_started:
            if self.c_gear < self.no_gears:
                self.c_gear += 1
                print(f"car with regno: {self.regno} changed gear....")
            else:
                print(f"car with regno :{self.regno}  cant chnge gear....")
        else:
            print(f" car with regno: {self.regno} stopped")
            
    def showInfo(self):
        
