# py_calc.py
import argparse, sys, re
from math import *

def get_args(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument('ip_expr', nargs='?',
                    help="input expression to be evaluated")
    parser.add_argument('-f', metavar='precision', nargs='?', const=2, type=int,
                    help="specify floating point output precision")
    parser.add_argument('-F', action="store_true",
                    help="turn off the default precision .2f")
    parser.add_argument('-b', action="store_true",
                    help="output in binary format")
    parser.add_argument('-o', action="store_true",
                    help="output in octal format")
    parser.add_argument('-x', action="store_true",
                    help="output in hexadecimal format")
    parser.add_argument('-v', action="store_true",
                    help="verbose mode, shows both input and output")
    args = parser.parse_args()

    if args.ip_expr in (None, '-'):
        args.ip_expr = sys.stdin.readline().strip()

    try:
        # https://stackoverflow.com/questions/55072669/how-to-replace-x-with-math-factorialx-intelligently
        change_expr = re.sub(r'([\w]+)!|\((.+?)\)!', r'factorial(\1\2)', args.ip_expr)
        result = eval(change_expr)

        if isinstance(result, float):
            if args.f:
                result = f'{result:.{args.f}f}'
            elif args.F:
                result = f'{result}'
            else:
                result = f'{result:.2f}'
        elif args.b:
            result = f'{int(result):#b}'
        elif args.o:
            result = f'{int(result):#o}'
        elif args.x:
            result = f'{int(result):#x}'

        if args.v:
            return f'{args.ip_expr} = {result}'
        else:
            return f'{result}'
    except (NameError, SyntaxError):
        sys.exit("Error: Not a valid input expression")
    
if __name__ == '__main__':
    import sys
    output = get_args(sys.argv)
    print(output)
