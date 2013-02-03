import math 

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


# Code from Udacity CS 215, Unit 2 
def make_link(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

# Ring Network
# Make an empty graph (dict)
ring = {}

n = 5

# Add in edges
for i in range(n):
  ring = make_link(ring, i, (i+1)%n)

# How many nodes?
print len(ring)

# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2 

print ring 


# Grid Network
grid = {}

n = 256 
side = int(math.sqrt(n))

# Add in edges
for i in range(side):
  for j in range(side):
    if i < side-1: make_link(grid, (i,j), (i+1,j)) # link to node below
    if j < side-1: make_link(grid, (i,j), (i,j+1)) # link to node at right

# How many nodes?
print len(grid)

# How many edges?
print sum([len(grid[node]) for node in grid.keys()])/2 # make this a function

def count_edges(graph):
  return sum([len(graph[node]) for node in graph.keys()])/2

# Social network
class Actor(object):
  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return "My name is " + self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

make_link(movies, dh, rd) # Wag the Dog
make_link(movies, rd, ms) # Marvin's Room
make_link(movies, dh, ss) # Midnight Mile
make_link(movies, dh, jr) # Hook
make_link(movies, dh, kb) # Sleepers
make_link(movies, ss, jr) # Stepmom
make_link(movies, kb, jr) # Flatliners
make_link(movies, kb, ms) # The River Wild
make_link(movies, ah, ms) # Devil Wears Prada
make_link(movies, ah, jr) # Valentine's Day


print len(movies) # How many nodes?
print count_edges(movies) # How many edges?

def tour(graph, nodes):
  for i in range(len(nodes)):
    node = nodes[i] 
    if node in graph.keys():
      print node 
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass 
        else:
          print "Can't get there from here!"
          break 

movie_tour = [ms, rd, dh, ss, jr, ah, ms, kb, dh, jr, kb] 
# print rd in movies[ms]
tour(movies, movie_tour)

# TODO: write a function to find an Eulerian tour 

