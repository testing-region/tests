from fizzbuzz import FizzBuzz


class Numbers(FizzBuzz):
    
    def __init__(self, num):
        self.num = num
        
    def display(self):
        for i in range(self.num):
            print(self.fizzbuzz(i))
