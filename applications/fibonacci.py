# fix the fibonacci to make it run faster..
# 0 1 1 2 3 5 8 13 21 34 ...

"""
instead of having to compute the same back 2 numbers over and over again,
 it stores it in a cache. So it can just reach in instead of computing. 
"""
cache = {}
def fib(n):
	if n <= 1:
		return n
	if n not in cache:
		cache[n] = fib(n-1) + fib(n-2)
	return cache[n]
for i in range(2000):
	print(f"{i:3}: {fib(i)}")