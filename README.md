# rolly
Rolly is a tool that parses command line arguments to simulate dice rolls, and can handle multiple rolls at once.  

e.g. 
```
$ python rolly.py 2d6+2
Your 2d6+2 roll resulted in: 9
The individual rolls and bonus modifier were: (2 + 5) + 2
Total of all dice rolls is: 9
```

```
$ python rolly.py 2d6-4 d20-2
Your 2d6-4 roll resulted in: 0
The individual rolls and bonus modifier were: (3 + 1) + -4
Your d20-2 roll resulted in: 8
The individual rolls and bonus modifier were: (10) + -2
Total of all dice rolls is: 8
```
