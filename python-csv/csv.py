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

    # we're going to try to open the file but if it doesn't exist
    # an exception will be thrown - an IOError specifically
    try:
        f = open(filename)
    except IOError:
        print("Error opening file. Check the filename?")
        exit()
    
    # this is how you declare a list in python

    my_table = []


    # each element of this list will be a line from the csv file

    # there are a couple different ways to read a file in
    # python can turn the whole file into a string by simply doing
    # s = f.read()
    # and s will automatically obtain the type "string"
    # but in case that csv file is 10 gigs... lets just read a line at a time
    # this is how easy python for loops are, you specify a variable name (e.g. line)
    # and it automatically obtains the type for whatever you have a list of, in this case
    # they are strings ending with '\n'

    for line in f:

        # this is a tricky addition that helps us skip empty lines

        if len(line) < 1:
            pass


        # this is another tricky addition to remove the '\n' from the end of the string
        # we're using python's slicing feature to remove the last element from
        # the string. python strings can be referred to character-by-character just like C
        # e.g. line[0] is the first character. Except python also allows you to start at the end
        # line[-1] is the last character
        # slicing is done by specifying a place to start, then a ':' and a place to stop.
        # we didn't specify a start, so it assumes we want the beginning of the string, up til the last char

        if line.endswith("\n"):
            line = line[:-1]


        # the reason the "line" becomes a list is the "split" function - it
        # automatically transforms a string into a list by picking a character to throw
        # out, in this case "," and splitting on that character, into individual items

        tmp = line.split(',')


        # here we'll find out if its a string or not, python lets us just say not instead of using "!"
        # we're going to naively assume that each row all has the same type..
        # you'd need a couple more lines of logic to do otherwise

        if not tmp[0].startswith('"') and not tmp[0].endswith('"'):


            # this is the good old map function, it takes a function "int" and a list and applies the
            # function to each element of the list. Since tmp is a list of strings (that's how the file
            # is interpreted), we want to convert the "1" string into an actual 1. 
            # (normally this would just be int("1"))
            # we're going to use the list function "append" to add a new element to
            # the "my_table" list. 

            my_table.append(map(int, tmp))
        else:

            # next we need to deal with the pesky quotation marks that are hanging on the strings
            # I decided to copy them to a new list using the string function "strip" to take the
            # first and last character off of the list, assuming they match the pattern specified.

            new_tmp = []
            for badstring in tmp:
                new_tmp.append(badstring.strip('"'))


            # now that we've cleaned up the string, we can put them in our table

            my_table.append(new_tmp)

    # and now we're done with the file so we'll close it
    f.close()
    

    # in order to see the results, lets print it out!
    for row in my_table:
        print(row)


# below is something you put in every file you plan to call from the command line.
# it basically just means that hey, if you ran this script on its own call main
# the only time this script will be loaded and wont just automatically run main
# is when you import it into another script

if __name__=="__main__":
    main()
