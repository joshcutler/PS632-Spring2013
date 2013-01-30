"""Lab 3:
Algorithms and Exceptions
"""

def FizzBuzzLoop(upper):
  for i in range(1,upper):
    print FizzBuzz(i)

def FizzBuzz(i): 
    if i % 15 == 0:
      raise Exception, "Divisible by both 3 and 5!"
    elif i % 3==0:
      return "Fizz"
    elif i % 5 == 0:
      return "Buzz"
    else: 
      return i

# FizzBuzzLoop(14)

# try: 
#   FizzBuzz(16)
# except Exception as e:
#   print "Error Caught!"