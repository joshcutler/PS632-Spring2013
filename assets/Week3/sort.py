import random
import sys, time

# Random sort
n = 10

sorted_array = range(1, n)

def random_sort(array_to_sort, sorted_array, debug=False):
  count = 0
  while (array_to_sort != sorted_array):
    random.shuffle(array_to_sort)
    count += 1

    if debug and count % 100 == 0:
      sys.stdout.write(".")
  if debug: sys.stdout.write(" Done!")

trials = 10
random_times = [0] * trials
quick_times = [0] * trials
for i in range(0, trials):
  random_array = range(1, n)
  random.shuffle(random_array)

  start_time = time.time()
  random_sort(random_array, sorted_array)
  random_times[i] = time.time() - start_time

  random_array = range(1, n)
  random.shuffle(random_array)

  start_time = time.time()
  random_array.sort()
  quick_times[i] = time.time() - start_time


print "Random"
print "======================"
print "Max:   {0}".format(max(random_times))
print "Min:   {0}".format(min(random_times))
print "Mean:  {0}".format(sum(random_times) / len(random_times))
print "Total: {0}".format(sum(random_times))

print "\nQuick"
print "======================"
print "Max:  {0}".format(max(quick_times))
print "Min:  {0}".format(min(quick_times))
print "Mean: {0}".format(sum(quick_times) / len(quick_times))
print "Total: {0}".format(sum(quick_times))
