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

def FizzBuzz(upper):
  for i in range(upper):
    if i % 15 == 0:
      raise Exception, "Divisible by both!"
    elif i % 3==0:
      print "Fizz"
    elif i % 5 == 0:
      print "Buzz"
    else: 
      print i 

def NewtonRoot(number, epsilon=0.0000001):
  """Newton-Raphson method to find square root of number
  http://en.wikipedia.org/wiki/Newton's_method#Square_root_of_a_number"""
  a = number 
  x = 10.0
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

NewtonRoot(9.0)
  

