"""
Write a program that prints the numbers from 1 to 100. 
But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”. 
For numbers which are multiples of both three and five print “ThreeFive”. 
"""

import argparse


def main(args: argparse.Namespace) -> None:
    """
    gets the argument and send to the function to print

    """
    start = args.start
    stop =  args.stop

    _printMultiples(start, stop)


def _printMultiples(start: int, stop: int) -> None:
    """
    print multples for three, five and three and five

    """
    for n in range(start, stop):
        if _multiplesThreeAndFive(n):
            print("ThreeFive")
            continue

        if _multiplesThree(n):
            print("Three")
            continue

        if _multiplesFive(n):
            print("Five")
            continue

        print(n)


def _multiplesThree(n:int) -> bool:
    if not isinstance(n, int):
        raise TypeError("'n' value is not a integer")
    return True if n % 3 == 0 else False


def _multiplesFive(n:int) -> bool:
    if not isinstance(n, int):
        raise TypeError("'n' value is not a integer")
    return True if n % 5 == 0 else False


def _multiplesThreeAndFive(n:int) -> bool:
    if not isinstance(n, int):
        raise TypeError("'n' value is not a integer")
    return True if n % 3 == 0 and n % 5 == 0 else False


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Program that prints the numbers from 1 to 100.')
    parser.add_argument('--start', 
                        type=int, 
                        default=1,
                        help='an integer for start')

    parser.add_argument('--stop', 
                        type=int, 
                        default=101,
                        help='an integer for stop')


    args = parser.parse_args()
  
    main(args)