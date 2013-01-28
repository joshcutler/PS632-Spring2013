a = "I'm global a"
b = "I'm global b"

def bothLocal():
	print "both local:"
	a = "I'm local a"
	b = "I'm local b"
	print a
	print b 

def oneLocalOneGlobal(var):
	print "one local one global:"
	global a # BAD IDEA
	b = "I'm local b"
	print a
	print b

def globalsGetPassed(var1, var2):
	print "globals get passed:"
	print var1
	print var2

bothLocal()
oneLocalOneGlobal(a)
globalsGetPassed(a, b) 