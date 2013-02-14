import re

# open text file of 2008 NH primary Obama speech
file = open("obama-nh.txt", "r")
text = file.readlines()
file.close()

# compile the regular expression
keyword = re.compile(r"the ")

# search file for keyword, line by line
for line in text:
	if keyword.search(line):
		print line 

# print all lines that DO NOT contain "the "
# if not keyword.search (line):

# print lines that contain a word of any length starting with s and ending with e
# keyword = re.compile(r"\bs\w*e\b")

file = open("example.html","r")
html = file.readlines()
file.close()

# searching the file content line by line:
keyword = re.compile(r"<.+?>")

for line in html:
  result = keyword.search(line)
  if result:
   	print result.group(), ":", line
	
