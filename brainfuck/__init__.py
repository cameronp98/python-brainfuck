"""
A brainfuck interpreter.
"""

from brainfuck.parse import parse
from brainfuck.program import Program


# The standard cell requirement is 30,000 cells
CELLS_DEFAULT = 30000


def execute(string, num_cells=CELLS_DEFAULT):
    """
    Parse and evaluate a brainfuck program from a string.
    """

    ops = parse(string)
    program = Program(num_cells)
    program.execute_many(ops)



