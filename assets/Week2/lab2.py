"""
Lab 2: Classes and Inheritance
This is a two-dimensional example
See inlab2.py for a one-dimensional example 
""" 
import random 

# background: 
# http://en.wikipedia.org/wiki/Median_voter_theorem
# http://en.wikipedia.org/wiki/Jefferson_(Pacific_state)
# http://www.youtube.com/watch?v=31FFTx6AKmU

class Individual(object):
	def __init__(self, ideology):
		self.ideology = ideology


class Candidate(Individual):
  def __init__(self, ideology, party, taxRate, publGoods):
    Individual.__init__(self, ideology)
    self.party = party 
    self.taxRate = taxRate
    self.publGoods = publGoods

  def __repr__(self):
  	return "%s party" % self.party 


class Voter(Individual):
	def __init__(self, ideology , income):
		Individual.__init__(self, ideology)
		self.income = income 


class Polity(object):
  def __init__(self):
    self.voters = []
    self.candidates = []

  def __repr__(self):
    return "There are %d candidates and %d voters" % (len(self.candidates), len(self.voters))

  def populate(self, count):
    for i in range(count):
      ideol = random.betavariate(5,5)
      inc = random.gauss(50000, 10000)
      voter = Voter(ideol, inc) 
      self.voters.append(voter)

  def nominate(self, cand):
		self.candidates.append(cand)

  def election(self):
    counts = [0] * len(self.candidates) 
    ballots = dict(zip(self.candidates, counts))
    for voter in self.voters: 
      idDiff = min(range(len(self.candidates)), key = lambda i: abs(voter.ideology - self.candidates[i].ideology))
      moneyDiff = max(range(len(self.candidates)), 
        key = lambda i: voter.income*(1-self.candidates[i].taxRate) + 
          self.candidates[i].publGoods/len(self.voters) )
      if idDiff > moneyDiff: # strong ideological preference
        choice = self.candidates[idDiff]
      else: 
        choice = self.candidates[moneyDiff] 
      ballots[choice] += 1
    print ballots 
    winner = max(ballots, key=ballots.get)
    return winner 

# Make candidates
sensible = Candidate(.55, "sensible", .3, 1000000)
silly = Candidate(.45, "silly", .4, 1100000)
slightly_silly = Candidate(.4, "slightly silly", .35, 900000)
very_silly = Candidate(.1, "very silly", .5, 800000)
stone_dead = Candidate(.01, "stone dead", .6, 0)

print sensible, silly, slightly_silly, very_silly, stone_dead

# Create and populate polity
jefferson = Polity()
jefferson.populate(100)

# Nominate candidates
jefferson.nominate(sensible)
jefferson.nominate(silly)
jefferson.nominate(slightly_silly)
jefferson.nominate(very_silly)
jefferson.nominate(stone_dead)

print jefferson 

# Have an election 
victor = jefferson.election()
print "And the winner is... the %s!" % victor




