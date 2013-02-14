import re

# open text file of 2008 NH primary Obama speech
file = open("obama-nh.txt", "r")
text = file.readlines()
file.close()

# compile the regular expression
keyword = re.compile(r"yes we can", re.I)

counter = 0
# search file for keyword, line by line
for line in text:
	if keyword.search(line):
		counter += 1
print counter  

# print all lines that DO NOT contain "the "
keyword = re.compile(r"[a-s,u-z][a-g,j-z][a-d,f-z]") # Cindy

# print lines that contain a word of any length starting with s and ending with e
# keyword = re.compile(^(s[\w]*)e$) # Max 
	
# date = raw_input("Please enter a date in the format MM.DD.YY: ")
# keyword = re.compile(r"(\d\d?)\.(\d\d?)\.(\d\d)")
# result = keyword.search(date)
# if result:
# 	print "Month: ", result.group(1)
# 	print "Day: ", result.group(2)
# 	print "Year: ", result.group(3)	

# Write a regular expression that finds html tags in example.html and prints them.
# print lines that contain a word of any length starting with s and ending with e
# keyword = re.compile(r"\bs\w*e\b")

file = open("example.html","r")
html = file.readlines()
file.close()

# searching the file content line by line:
# keyword = re.compile(r"<.+?>")
keyword = re.compile(r"[<\\\w][>][\w][<\w]")

for line in html:
  result = keyword.search(line)
  if result:
   	print result.group(), ":", line

