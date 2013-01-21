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
  def __init__(self, ideology, party):
    Individual.__init__(self, ideology)
    self.party = party 

  def __repr__(self):
  	return "%s party" % self.party 


class Voter(Individual):
  def __init__(self, ideology):
    Individual.__init__(self, ideology)
  
  def __repr__(self):
    return "I think %d is the best policy" % self.ideology


class Polity(object):
  def __init__(self):
    self.voters = []
    self.candidates = []

  def __repr__(self):
    return "There are %d candidates and %d voters" % (len(self.candidates), len(self.voters))

  def populate(self, count):
    for i in range(count):
      ideol = random.betavariate(5,5)
      voter = Voter(ideol) 
      self.voters.append(voter)

  def nominate(self, cand):
		self.candidates.append(cand)

  def election(self):
    counts = [0] * len(self.candidates) 
    ballots = dict(zip(self.candidates, counts))
    for voter in self.voters: 
      minDiff = min(range(len(self.candidates)), key = lambda i: abs(voter.ideology - self.candidates[i].ideology))
      choice = self.candidates[minDiff]
      ballots[choice] += 1 
    return ballots 
    
  def get_winner(self):
    ballots = self.election()
    winner = max(ballots, key=ballots.get)
    return winner 

# Make candidates
sensible = Candidate(.55, "sensible")
silly = Candidate(.45, "silly")
slightly_silly = Candidate(.4, "slightly silly")
very_silly = Candidate(.1, "very silly")
stone_dead = Candidate(.01, "stone dead")

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
result = jefferson.election() 
victor = jefferson.get_winner()
print "And the winner is... the %s!" % victor




