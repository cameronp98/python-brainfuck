"""
A brainfuck interpreter.
"""


from brainfuck.parse import parse
from brainfuck.program import Program


__all__ = ["parse", "program"]


# The standard cell requirement is 30,000 cells
CELLS_DEFAULT = 30000


def execute(string, num_cells=CELLS_DEFAULT):
    """
    Parse and evaluate a brainfuck program from a string.
    Returns the program after execution.
    """

    ops = parse(string)
    program = Program(num_cells)
    program.execute_many(ops)

    return program



