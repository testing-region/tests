import math

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_ = 0
        mul_ = 1

        while n > 0:
            temp = n % 10
            mul_ *= temp
            sum_ += temp
            n //= 10

        return mul_ - sum_
