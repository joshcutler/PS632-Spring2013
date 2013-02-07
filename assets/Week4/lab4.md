Make sure everyone understands `&` (lowest bit, used to check odd/even) and `break` to get out of a loop. 

Introduce the concept of an [Eulerian path](http://en.wikipedia.org/wiki/Eulerian_path) and an Eulerian tour.

Discuss chain networks and ring networks. Also describe how these would be represented in an adjacency matrix.

Now, explain `make_link()` and the `ring` network. Discuss grid networks.

Then, have students join in groups of 2-3 and complete the following exercises: 

1.  Use the code to count how many edges a 16x16 grid network would have. 
2. Play around with the movie graph (or another graph of your choosing). Lots of information about actors' linkages can be found [here](http://oracleofbacon.org/). Can you find an Eulerian tour of the movie graph? Who does it end with? Verify your answer in Python.
3. Show `factorial.py` to demonstrate recursion. Implement `findShortestPath` and `findAllPaths` based on the code given for `findPath`.  


If they don't finish all of these in lab thats fine--just do as many as they can. Note that recursion is they key to completing all of these algorithms (there are other ways, but we want them to learn recursion for the HW assignment). Discuss the Big-Oh complexity of each algorithm. Mention Big-Theta notation for graph complexity. 
