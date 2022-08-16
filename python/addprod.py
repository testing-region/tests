import math

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        val = [int(x) for x in str(n)]
        return math.prod(val) - sum(val)
