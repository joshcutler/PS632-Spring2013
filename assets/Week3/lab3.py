"""Lab 3:
Algorithms and Exceptions
"""

def Romanify(num):
  """turns a base-10 integer between 0 and 4000 into
  a Roman numeral string"""

  if not 0 < num< 4000:
    return "out of range"
  ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
  nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
  result = ""
  for i in range(len(ints)):
    count = int(num / ints[i])
    result += nums[i] * count 
    num -= ints[i] * count 
  return result

# thisYear = Romanify(2013)
# print thisYear 


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


def linear_search(x, nums):
  """Linear search from Zelle (2002) p. 226"""
  for i in range(len(nums)):
    if nums[i] == x:
      return i 
  return -1 

def binary_search(x, nums):
  """Zelle (2002) p. 227; expects sorted list"""
  low = 0 
  high = len(nums) -1
  while low < high: 
    mid = (low+high)/2
    item = nums[mid]
    if x == item:
      return mid
    elif x < item: 
      high = mid -1 
    else: 
      low = mid + 1
  return -1 

print linear_search(1, [0,1,2,3])
print binary_search(1, [0,1,2,3])

def DeRomanify(string):
  return 0 
  # TODO: make this work! 

