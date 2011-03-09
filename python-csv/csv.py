#!/usr/bin/python

# csv parser

# A CSV File should look something like this

# either strings:
# "hello","my","name","is","bob"

# or data:
# 1,2,3,4

# i'll attempt to parse for either

# this is how you pull in libraries
# we'll need sys to use the argument list
# in order to put a filename on the command line
import sys

def main():
    """this doesn't actually have to be called main..
    what i'm writing now is called a docstring - its more than
    just a comment. python considers it formal documentation"""

    # this uses the len function on the argument list to make sure there are
    # 2 items in the list - the script name(e.g. csv.py) and the CSV filename
    if len(sys.argv) != 2:
        print("Please provide a CSV filename.")
        exit()

    # this is all you have to do to call your function
    # note that the order you write your functions in the file
    # doesn't matter
    parse_csv(sys.argv[1])

def parse_csv(filename):
    """This function has the argument "filename" and
    will only be called if a filename was provided on the command line"""

    f = open(filename)
    f.close()

# below is something you put in every file you plan to call from the command line.
# it basically just means that hey, if you ran this script on its own call main
# the only time this script will be loaded and wont just automatically run main
# is when you import it into another script
if __name__=="__main__":
    main()
