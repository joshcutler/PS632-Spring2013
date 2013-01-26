#import random 
import time 
import lab3 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot

def getRunningTime(func, maxN=250, repetitions=100):
	times = []

	for n in range(1, maxN):
		start = time.clock()
		for rep in range(repetitions):
			func(n)
		end = time.clock()
		avg = (end-start)/float(repetitions)
		times.append(avg)

	return times 

def getRunningTime2(func, maxN=250, repetitions=100):
	times = []

	for n in range(1, maxN):
		start = time.clock()
		for rep in range(repetitions):
			func(n-1, n)
		end = time.clock()
		avg = (end-start)/float(repetitions)
		times.append(avg)

	return times 

def plotRunningTime(times, name="plot"): 
	x = range(len(times))
	pyplot.plot(x, times, 'o')
	pyplot.savefig(name + "%d.png" % len(times))
	pyplot.close()

runFizz14 = getRunningTime(lab3.FizzBuzz, 14, 100)
print runFizz14

runRoot1000 = getRunningTime(lab3.NewtonRoot, 1000, 100)
# print runRoot1000 
plotRunningTime(runRoot1000, "roots")

primetime = getRunningTime(lab3.primes_sieve, 100000, 100)
plotRunningTime(primetime, "primes")

runGcd1 = getRunningTime2(lab3.gcd1, 10000, 100)
plotRunningTime(runGcd1, "gcd")

runGcd2 = getRunningTime2(lab3.gcd2, 10001, 100)
plotRunningTime(runGcd2, "gcd")
