def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits = []
  while num: 
    digits.append(str(num % 2))
    num /= 2
  digits.reverse()
  return ''.join(digits)

def int_to_base(num, base):
  if num==0 or base <= 0 : return '0'
  digits = []
  absnum = abs(num)
  while absnum:
    digits.append(str(absnum % base))
    absnum /= base
  if num < 0: digits.append('-')
  digits.reverse()
  return ''.join(digits)

def base_to_int(string, base):
  if string=="0" or base <= 0 : return 0 
  elif string[0]=="-" : rev = (string[1:])[::-1]
  else: rev = string[::-1]
  result = 0 
  for i in range(len(rev)):
    num = int(rev[i])
    result += num * base ** i  
  if string[0]=="-" : result *= -1 
  return result 

def flexibase_add(str1, str2, base1, base2):
  num1 = base_to_int(str1, base1)
  num2 = base_to_int(str2, base2)
  tmp = num1 + num2 
  result = int_to_base(tmp, base1)
  return result 

def flexibase_multiply(str1, str2, base1, base2):
  num1 = base_to_int(str1, base1)
  num2 = base_to_int(str2, base2)
  tmp = num1 * num2 
  result = int_to_base(tmp, base1)
  return result 

def romanify(num):
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

# def deromanify(string):
#   # TODO: go over this once they know dicts


