import math 

def romanify(num):
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
def makeLink(G, node1, node2):
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
  ring = makeLink(ring, i, (i+1)%n)

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
    if i < side-1: makeLink(grid, (i,j), (i+1,j)) # link to node below
    if j < side-1: makeLink(grid, (i,j), (i,j+1)) # link to node at right

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

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day


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
tour(movies, movie_tour)

# find path between two nodes
# http://www.python.org/doc/essays/graphs.html
def findPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = findPath(graph, node, end, path)
                if newpath: return newpath
        return None

print findPath(movies, jr, ms)

def findAllPaths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = findAllPaths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

allPaths = findAllPaths(movies, jr, ms)
print " "
print "Here are all paths connecting JR and MS:"
for path in allPaths:
  print path 

def findShortestPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = findShortestPath(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

print findShortestPath(movies, jr, dh)
