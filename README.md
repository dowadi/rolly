# rolly
Rolly is a tool that parses command line arguments to simulate dice rolls, and can handle multiple rolls at once.  

e.g. 
```
$ python rolly.py 2d6-4
Your 2d6-4 roll resulted in: 3
The individual rolls and bonus modifier were: (3 + 4) + -4
```

```
$ python rolly.py 2d6-4 d20-2
Your 2d6-4 roll resulted in: -2
The individual rolls and bonus modifier were: (1 + 1) + -4
Your d20-2 roll resulted in: 6
The individual rolls and bonus modifier were: (1 + 1 + 6) + -2

```
