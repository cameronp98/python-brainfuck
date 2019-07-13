""" A Brainfuck Interpreter """

from typing import List


class ParseError(Exception):
    def __init__(self, message):
        self.message = message


def parse(line) -> List:

    ops = []
    stack = []

    for c in line:
        if c.isspace():
            # skip whitespace
            continue
        if c in "><+-.,":
            # add simple operators to the program list
            ops.append(c)
        elif c == "[":
            # save the current program on the stack and start accumulating
            # instructions until a close loop instruction is encountered
            stack.append(ops)
            ops = []
        elif c == "]":
            # save the loop body, pop the original program from the stack,
            # and add the new loop to the end of the program
            loop = ops
            if stack:
                ops = stack.pop()
            else:
                raise ParseError("Unexpected ']'")
            ops.append(loop)
        else:
            # report unreckognised character
            raise ParseError(f"Unknown character '{c}'")

    # report unmatched '['
    if stack:
        raise ParseError("Unmatched '['")

    return ops


