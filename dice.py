import random

class Roll:
    num_die = 0
    die_sides = 0
    roll_bonus = 0
    roll_results = []
    def __init__(self, roll_req):
        '''

        :param roll_req: The input string formatted, for example, 2d2+1

        >>> random.seed(1)
        >>> roll_req = Roll("4d10-2")
        >>> roll_req.num_die
        4
        >>> roll_req.die_sides
        10
        >>> roll_req.roll_bonus
        -2
        >>> roll_req.die()
        8
        >>> roll_req.roll_results
        [3, 2, 5, 2]
        >>> roll_req.pretty_print()
        '3 + 2 + 5 + 2'
        >>> Roll("2e20").num_die
        Traceback (most recent call last):
          ...
        IndexError: list index out of range

        '''
        # Reads and separates the incoming roll request
        str_reader = roll_req.split("d")
        if str_reader[0].isdigit():  # Number of dice to roll
            self.num_die = int(str_reader[0])
        else:
            self.num_die = 1

        if "+" or "-" in str_reader[1]:  # Determines presence of a positive modifier
            if "+" in str_reader[1]:
                str_reader.append(str_reader[1].split("+"))
                self.roll_bonus = int(str_reader[2][1])  # Roll with a positive modifier

            elif "-" in str_reader[1]:  # Determines presence of a negative modifier
                str_reader.append(str_reader[1].split("-"))
                self.roll_bonus = 0 - int(str_reader[2][1])  # Roll with a negative modifier

            self.die_sides = int(str_reader[2][0])  # Number of sides on die

        else:  # No roll modifier present
            self.die_sides = int(str_reader[1])  # Number of sides on die

        for self.i in range(self.num_die):  # Dice roll
            self.roll_results.append(self.die())

    def die(self):
        return random.randrange(1, self.die_sides)  # Die roll

    def pretty_print(self):  # Makes a math formula
        self.pretty = " + ".join(map(str, self.roll_results))
        return self.pretty