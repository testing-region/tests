class FizzBuzz:

    def fizzbuzz(self, num):
        msg = num

        if num == 3:
            msg = "Fizz"
        elif num == 5:
            msg = "Buzz"

        return msg
