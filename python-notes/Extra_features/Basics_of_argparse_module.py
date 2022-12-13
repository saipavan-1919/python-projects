import argparse
import sys
  

print(type(sys.argv))
args = sys.argv
print(args)
for i in args:
    print(i)


"""
    There are three main steps while dealing with the command line arguments using the argparse module
    1) creating parser
    2) adding arguments to the parser
    3) parsing arguments
"""

"""
    1) creating a parser
    syntax :  class argparse.ArgumentParser()
    this returns a parser object
"""
# description– text to display before the argument help(default: none)
# epilog  text to display after the argument help (default: none)
parser = argparse.ArgumentParser(description="addition of arguments", epilog="done with the addition of cmd args")
print(type(parser))


""" 
    2) adding arguments to the parser
    we can add the commandline arguments to the parser by using add_argument() method
    syntax: ArgumentParser.add_argument()
"""
# name or flags : either a name or list of option string
# action : basic type of action to be taken when this argument is encountered at the command line
# help : brief description of what the argument does
parser.add_argument("-a","-ab",action="store_true",help="this will store value of 1")
# action : store_false
parser.add_argument("-n3",action='store_false')

# default : value produced if the arguments are absent from the command line
# nargs : number of command-line arguments that should be consumed
# if nargs = '*' --> 0 or more than 0
# if nargs = '+' --> 1 or more than 1
parser.add_argument("-n",default=10,nargs="*")

# if nargs = 2   --> exactly 2 arguments after matching with the string
parser.add_argument("-n1",nargs=2)

# type : type to which the command line arguments should be converted.
# converts the command line arguments into the type mentioned
parser.add_argument("-n2",nargs=2,type=int)

# const : constant value required by some action and nargs selections
parser.add_argument("-n4",const=12,nargs='?')

# choices : A container of the allowable values for the argument
parser.add_argument("-n5",choices=['hi','how'],default=None)

# parsing arguments
args = parser.parse_args()
print(args)
print(args.a)
print(args.n)
print(args.n1)
print(args.n2)
print(args.n3)
print(args.n4)
print(args.n5)
