"""
Lab 2: Classes and Inheritance
Demonstrating the Median Voter Theorem
""" 

import random 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import numpy as np 
from scipy.stats import gaussian_kde

# background: 
# http://en.wikipedia.org/wiki/Median_voter_theorem
# http://en.wikipedia.org/wiki/Jefferson_(Pacific_state)
# http://www.youtube.com/watch?v=31FFTx6AKmU

class Individual(object):
	def __init__(self, ideology):
		self.ideology = ideology


class Voter(Individual):
  def __init__(self, ideology):
    Individual.__init__(self, ideology)
  
  def __repr__(self):
    return "I think %d is the best policy" % self.ideology


class Candidate(Individual):
  def __init__(self, ideology, party):
    Individual.__init__(self, ideology)
    self.old_ideology = self.ideology
    self.party = party 
    self.numerator = 1
    self.denominator = 1

  def __repr__(self):
  	return "%s party" % self.party 

  def report_ideology(self):
    return self.ideology 

  def update_ideology(self, ballot):
    self.old_ideology = self.report_ideology()
    self.numerator += ballot[self]
    self.denominator += ballot[self]
    ideologies = [self.old_ideology]
    numerators = [self.numerator]
    for candidate in ballot: 
      if ballot[candidate] >= ballot[self]:
        ideologies.append(candidate.old_ideology)
        numerators.append(ballot[candidate])
    denominator = float(sum(numerators))
    weights = [x/denominator for x in numerators]
    linear_mix = sum([a*b for a,b in zip(ideologies, weights)])
    self.ideology = linear_mix


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
    
  def get_winner(self, ballots):
    winner = max(ballots, key=ballots.get)
    return winner 

  def report_candidate_ideologies(self):
    for candidate in self.candidates:
      print candidate, ":", candidate.report_ideology()

  def update_candidate_ideologies(self, ballot):
    for candidate in self.candidates:
      candidate.update_ideology(ballot)

  def plot_voter_ideologies(self):
    ids = []
    for voter in self.voters:
      ids.append(voter.ideology)
    density = gaussian_kde(ids)
    xs = np.linspace(0,1,200)
    density.covariance_factore = lambda : .25
    density._compute_covariance()
    pyplot.plot(xs, density(xs))
    pyplot.savefig('voter-ideologies.png')
    pyplot.close()

  def plot_candidate_ideologies(self, vertical=1):
    x = []
    for candidate in self.candidates:
      x.append(candidate.report_ideology())
    y = [vertical] * len(x)
    pyplot.axis([0.0, 1.0, 0.5, vertical+0.5])
    ax = pyplot.gca()
    ax.set_autoscale_on(False)
    pyplot.plot([0,1], [vertical,vertical], '-')
    colors = 'b,g,r,c,m,y,k,w'.split(',')
    colors = colors[0:len(x)]
    pyplot.scatter(x, y, marker='o', color=colors, s=150)


def print_winner(winner):
    print "And the winner is... the %s!" % winner 

def election(polity):
  result = jefferson.election() 
  print result 
  winner = jefferson.get_winner(result)
  print_winner(winner)
  print "OLD IDEOLOGIES:"
  jefferson.report_candidate_ideologies()
  jefferson.plot_candidate_ideologies(rounds)
  print "NEW IDEOLOGIES:"
  jefferson.update_candidate_ideologies(result)
  jefferson.report_candidate_ideologies()
  print "\n"
  return winner 

# Make candidates
sensible = Candidate(.55, "sensible")
silly = Candidate(.45, "silly")
slightly_silly = Candidate(.4, "slightly silly")
very_silly = Candidate(.1, "very silly")
stone_dead = Candidate(.01, "stone dead")

# print sensible, silly, slightly_silly, very_silly, stone_dead

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
jefferson.plot_voter_ideologies()

# Have an election 
winner = sensible
rounds = 0
while winner == sensible:
  rounds += 1
  winner = election(jefferson)
  pyplot.savefig("candidate-ideologies%d.png" % rounds)
print "it took %d rounds for the sensible party to lose" % rounds
