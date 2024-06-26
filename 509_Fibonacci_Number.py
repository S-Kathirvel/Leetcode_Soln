class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n==1:
            return 1
        else:
            return (self.fib(n-1) + self.fib(n-2))

# memo = {}
# if n == 0:
#	return 0
# elif n==1:
#       return 1
# elif n in memo:
#	return memo[n]
# else:
#	memo[n] = self.fib(n-1) + self.fib(n-2)
#       return memo[n]