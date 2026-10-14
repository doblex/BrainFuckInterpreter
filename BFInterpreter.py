import os, sys
import argparse

script_dir = os.path.dirname(os.path.abspath(__file__)) #get current directory

MEMORY_SIZE = 30000 #number of cells
CELL_MEMORY = 256   #max number on a cell

def readFile(filename):
    """Read file"""

    with open(filename) as f:
        return f.read()


def build_jump_table(code):
    """Create a table for the parenthesis"""
    stack = []
    jump_table = {}

    for i, command in enumerate(code):
        if command == "[":
            stack.append(i)

        elif command == "]":
            if not stack:
                raise SyntaxError(
                    f"']' not coupled in position {i}"
                )

            start = stack.pop()
            jump_table[start] = i
            jump_table[i] = start

    if stack:
        raise SyntaxError(
            f"'[' not coupled in position {stack[-1]} "
        )

    return jump_table


def execute(code):
    """Execute the code"""

    #memory init
    Addresses = [0] * MEMORY_SIZE 
    index = 0  #current cell position
    pc = 0     #current command position

    #getting precalc jumps
    jump_table = build_jump_table(code)

    while pc < len(code):
        command = code[pc]

        if command == ">":
            index = (index + 1) % MEMORY_SIZE

        elif command == "<":
            index = (index - 1) % MEMORY_SIZE

        elif command == "+":
            Addresses[index] = (Addresses[index] + 1) % CELL_MEMORY

        elif command == "-":
            Addresses[index] = (Addresses[index] - 1) % CELL_MEMORY

        elif command == ".":
            sys.stdout.write(chr(Addresses[index]))
            sys.stdout.flush()

        elif command == "[":
            if Addresses[index] == 0:
                pc = jump_table[pc]

        elif command == "]":
            if Addresses[index] != 0:
                pc = jump_table[pc]

        pc += 1

    print("\nProgram executed")

def main():

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--Text", help="Interpret the text passed")
    group.add_argument("-f", "--File", help="Interpret the file passed")
    args = parser.parse_args()

    if args.File:

        filename = args.File

        try:
            code = readFile(filename)
            execute(code)

        except FileNotFoundError:
            print(f"Error: Cannot find file '{filename}'.")
            sys.exit(1)

        except SyntaxError as error:
            print(f"Syntax error: {error}")
            sys.exit(1)

    elif args.Text:
        try:
            execute(args.Text)

        except SyntaxError as error:
                    print(f"Syntax error: {error}")
                    sys.exit(1)

    else:
        parser.print_help()
        sys.exit(1)




if __name__ == "__main__":
    main()
        