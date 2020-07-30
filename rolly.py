import argparse
import dice

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Rolly', description='Roll some dice!')

    parser.add_argument('die', type=str, nargs='+', help='a die to roll')
    parser.add_argument('--version', action='version', version='%(prog)s 0.2')
    parser.add_argument('-p', '--pretty', action="store_true", help='display individual rolls')

    rolls = parser.parse_args()  # Parses command line input

    rolls_total = 0
    for die in rolls.die:  # Isolates individual rolls
        roll_result = dice.Die_Roll(die)
        rolls_total += sum(roll_result.roll_results) + roll_result.roll_bonus
        print("Your {} roll resulted in: {}".format(die, sum(roll_result.roll_results) + roll_result.roll_bonus))
        if rolls.pretty:  # Checks for pretty print flag
            print("The individual rolls and bonus modifier were: ({}) + {}".format(roll_result.pretty_print(),
                                                                                   roll_result.roll_bonus))
    if len(rolls.die) > 1:  # Prints total if rolling more than 1 die
        print("Total of all dice rolls is: {}".format(rolls_total))
