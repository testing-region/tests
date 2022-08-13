class FizzBuzz:

    def fizzbuzz(self, num):
        # if num == 3:
        #     return "Fizz"
        # elif num == 5:
        #     return "Buzz"
        # return num

        # A great design should most likely have one exit point for a function
        # A good suggestion would be to have the return value stored in a variable and have just one exit point
        
        msg = num

        if num == 3:
            msg = "Fizz"
        elif num == 5:
            msg = "Buzz"

        return msg
