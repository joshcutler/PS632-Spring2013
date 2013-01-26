"""Lab 3:
Algorithms and Exceptions
"""

def FizzBuzz(upper):
  for i in range(1,upper):
    if i % 15 == 0:
      raise Exception, "Divisible by both 3 and 5!"
    elif i % 3==0:
      print "Fizz"
    elif i % 5 == 0:
      print "Buzz"
    else: 
      print i

# FizzBuzz(14)

# try: 
#   FizzBuzz(16)
# except Exception as e:
#   print "Error Caught!"


def NewtonRoot(number, epsilon=0.0000001):
  """Newton-Raphson method to find square root of number
  http://en.wikipedia.org/wiki/Newton's_method#Square_root_of_a_number"""
  a = number 
  x = a/2.0
  y = (x + a/x) / 2 
  iterations = 1 
  dif = abs(y-x) > epsilon
  while dif: 
    print iterations, ":", x
    y = (x + a/x) / 2
    dif = abs(y-x) > epsilon
    x = y 
    iterations += 1
  return y 

# num = 9.0
# root = NewtonRoot(num)
# print "Root of %f is approximately %f" % (num, root)


def gcd1(a, b):
  """Find the greatest common divisor of A and B. (Downey 2008: 61) 
  Hint: wikipedia.org/wiki/Euclidean_algorithm."""
  while b > 0:
    a, b = b, a % b
  return a

def gcd2(a, b):
  if(b == 0): return a
  else: 
    r = a % b 
    return gcd2(b, r)

# print gcd1(54,72)
# print gcd2(54, 72)


def primes_sieve(limit):
  # http://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
  a = [True] * limit   # Initialize the primality list
  a[0] = a[1] = False

  for (i, isprime) in enumerate(a):
    if isprime:
      yield i
      for n in xrange(i*i, limit, i):     # Mark factors non-prime
        a[n] = False

# primes = primes_sieve(14)
# for prime in primes:
#   print prime 


