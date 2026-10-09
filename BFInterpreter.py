import os, sys

script_dir = os.path.dirname(os.path.abspath(__file__)) #get current directory

MEMORY_SIZE = 30000 #number of cells
CELL_MEMORY = 256   #max number on a cell

def readFile(filename):
    """Read file"""
    filepath = os.path.join(script_dir, filename)

    with open(filepath) as f:
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
    if len(sys.argv) != 2:
        print("Use: python brainfuck.py <file.xxx>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        code = readFile(filename)
        execute(code)

    except FileNotFoundError:
        print(f"Errore: file '{filename}' non trovato.")
        sys.exit(1)

    except SyntaxError as error:
        print(f"Errore di sintassi: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
        