class FizzBuzz:

    def fizzbuzz(self, num):
        msg = num

        if num % 3 == 0 and num % 5 == 0:
            msg = "FizzBuzz"
        elif num % 3 == 0:
            msg = "Fizz"
        elif num % 5 == 0:
            msg = "Buzz"

        return msg
