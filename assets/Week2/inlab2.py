"""Lab 2: Classes and Inheritance
Demonstrating the Median Voter Theorem""" 
import random 

# background: 
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

  # TODO: have a voter tell you their ideology


class Polity(object):
  def __init__(self):
    self.voters = []
    self.candidates = []

  # TODO: have a polity print count of candidates and voters

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
    print ballots 
    winner = max(ballots, key=ballots.get)
    return winner 

# Make candidates
sensible = Candidate(.55, "sensible")
silly = Candidate(.45, "silly")
slightly_silly = Candidate(.4, "slightly silly")
# TODO: initialize very silly party with ideology .1
#       and a stone dead party with ideology .01 

print sensible, silly, slightly_silly

# Create and populate polity
jefferson = Polity()
jefferson.populate(100)

# Nominate candidates
jefferson.nominate(sensible)
jefferson.nominate(silly)
jefferson.nominate(slightly_silly)
# don't forget to nominate your new candidates! 

print jefferson 

# Have an election 
victor = jefferson.election()
# Who do you think it will be? 
print "And the winner is... the %s!" % victor

# TODO: make candidates respond to the votes
#       and hold another election