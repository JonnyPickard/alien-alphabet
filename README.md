Alien alphabet
==============

The idea here was given a sorted dictionary of alien words to work out the alphabet.

For example, if the words were ["z", "yx", "yz"] the alphabetical order would be
"xzy," which means x < z < y. The first two words tell you that z < y, and the
last two words tell you that x < z.

Method
------

In the end my solution involved 3 stages.

- Creating a graph using each individual letter of the alphabet once.
- Creating edges between the nodes of the graph.
- Sorting the resulting graph with a topological sort and returning it as a string.

This code is written in Python and I test drove the development using testtunit.

To Do Next
----------

Refactor the solution to be more agile and work faster. 
