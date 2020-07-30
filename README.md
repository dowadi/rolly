# Rolly
Rolly is a tool that parses command line arguments to simulate a die roll.

e.g. 
```
$  python rolly.py 2d6+2
Your 2d6+2 roll resulted in: 10
```

Handles multiple dice rolls, and provides a total 

e.g.
```
$ python rolly.py 2d6-4 d20-2
Your 2d6-4 roll resulted in: -1
Your d20-2 roll resulted in: 12
Total of all dice rolls is: 11
```

With an additional `-p` argument, Rolly will print the individual rolls (and the modifier)

e.g.
```
$ python rolly.py 2d6-4 d20-2 -p
Your 2d6-4 roll resulted in: 4
The individual rolls and bonus modifier were: (5 + 3) + -4
Your d20-2 roll resulted in: 12
The individual rolls and bonus modifier were: (14) + -2
Total of all dice rolls is: 16
```
