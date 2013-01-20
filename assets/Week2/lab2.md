Make sure everyone understands:

1. `Class`
1. `object`
1. `__init__`
1. `__str__` and `__repr__`
1. `self`
2. `dict()`, and the key/value pattern
3. `range`
4. `zip`
5. `min`
6. `lambda`

Give students the code for making an `Individual` object and a `Candidate`, which inherits from `Individual` with the addition of a `party` attribute. Based on this example, have students flesh out the `Voter` class by having a voter tell you their ideology when printed. 
Next, go through the `Polity` class and its methods. Have students explain how `populate`, `nominate`, and `election` work. How do these behaviors modify the state of the Polity? What values do they return? Are their any potentially undesirable side effects that should be handled? 

Now it's time for "election night." Initiate candidates from each of the five parties. Create a Polity with 100 voters, and nominate the candidates. Who do the students think will win the election? Why? 

Run the election and see whether the guesses were correct. 

Now, have the students write a method in the `Candidate` class by which they adjust their ideology to appeal to the voters. However, Candidates cannot access voters' ideology--they can only "learn" from the ballot in the election. (Notice that you might have to adjust this method slightly.) 

Then test that method by simulating 2 or more subsequent elections and monitoring how the candidates adjust their positions. What can we learn from this result? How might we make the model more realistic? How might we simplify (or generalize) it even further? 
