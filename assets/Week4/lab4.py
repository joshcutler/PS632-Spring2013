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

def DeRomanify(string):
  return 0 
  # TODO: make this work! 

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