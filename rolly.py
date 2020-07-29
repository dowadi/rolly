import argparse
import dice

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Rolly', description='Roll some dice!')

    parser.add_argument('die', type=str, nargs='+', help='a die to roll')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')

    rolls = parser.parse_args()  # Parses command line input

    for key in vars(rolls):
        roll_total = 0
        for roll in getattr(rolls, key):  # Isolates individual rolls
            result = dice.Roll(roll)
            roll_total += sum(result.roll_results) + result.roll_bonus
            print("Your {} roll resulted in: {}\nThe individual rolls and bonus modifier were: ({}) + {}".format(roll, sum(result.roll_results) + result.roll_bonus, result.pretty_print(), result.roll_bonus))
        print("Total of all dice rolls is: {}".format(roll_total))