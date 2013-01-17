def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: 
  	return '0'
  digits = []
  while num: 
    digits.append(str(num % 2))
    num /= 2
  digits.reverse()
  return ''.join(digits)

def anyary(num, base):
 	"""function name from Max Gallop"""
 	if num<=0: 	return '0' 
 	digits = []
 	while num:
 		digits.append(str(num % base))
 		num /= base
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


