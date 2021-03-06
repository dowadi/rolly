import random


class DieRoll:

    """
    Simulates a dice roll, roll_req should be in the format of "#d#±#"

    >>> random.seed(1)
    >>> roll_req = DieRoll("4d10-2")
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

    Must separate number of dice and number of die sides with a "d"
    >>> DieRoll("2e20").num_die
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    """

    def __init__(self, roll_req):
        """

        :param roll_req: The input string formatted, for example, 2d2+1

        """
        self.num_die = 0
        self.die_sides = 0
        self.roll_bonus = 0
        self.roll_results = []
        self.pretty = []

        # Parse the incoming roll request
        str_reader = roll_req.split("d")
        if str_reader[0].isdigit():  # Number of dice to roll
            self.num_die = int(str_reader[0])
        else:
            self.num_die = 1

        if "+" in str_reader[1] or "-" in str_reader[1]:  # Determines presence of a roll modifier
            if "+" in str_reader[1]:  # Positive roll modifier
                str_reader.append(str_reader[1].split("+"))
                self.roll_bonus = int(str_reader[2][1])  # Roll with a positive modifier

            else:  # Negative roll modifier
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
