Brainfuck Interpreter in Python

A simple Brainfuck interpreter written in Python. This project reads Brainfuck source code from a file, validates bracket matching, and executes the program using a circular memory tape.

📌 Features

Brainfuck interpreter implemented in Python.
30,000 memory cells, initialized to zero.
8-bit cell values, ranging from 0 to 255, with circular arithmetic.
Circular memory tape that wraps around at both ends.
Precomputed jump table for efficient loop execution.
Syntax validation for unmatched square brackets.
Immediate output using the . command.
Error handling for missing files, invalid syntax, and incorrect command-line arguments.

⚙️ Requirements

Python 3.x<br>
No external dependencies. The project uses only Python's standard library (os and sys).

📂 Project Structure<br>
.<br>
├── brainfuck.py       # Brainfuck interpreter<br>
├── hello.bf           # Example Brainfuck program<br>
└── README.md          # Project documentation<br>

Note: hello.bf is an example file. You can replace it with any file containing Brainfuck code.

🚀 Installation

Clone the repository:

git clone https://github.com/USERNAME/REPOSITORY.git

Navigate to the project directory:

cd REPOSITORY

No additional installation is required.

▶️ Usage

Run the interpreter by passing the source file as a command-line argument:

python brainfuck.py hello.bf

The interpreter reads the file, builds the jump table, and executes the code.

When execution completes successfully, the following message is displayed:

Program executed

🧩 Supported Instructions

The interpreter recognizes the eight standard Brainfuck commands.

Command	Description
- \>	Move the memory pointer one cell to the right.<br>
- \<	Move the memory pointer one cell to the left.<br>
- \+	Increment the current cell's value.<br>
- \-	Decrement the current cell's value.<br>
- \.	Print the character corresponding to the current cell's value.<br>
- \[	If the current cell is zero, jump to the matching ].<br>
- \]	If the current cell is nonzero, jump back to the matching [.<br>

Characters that are not valid Brainfuck commands are ignored.
