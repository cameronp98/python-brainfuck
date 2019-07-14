"""
Parse brainfuck programs into a list of operations.
"""

class ParseError(Exception):
    pass


def parse(string):
    """
    Parse the given string into a list of operators.
    Loops (`[...]`) are stored as nested lists.
    """

    ops = []
    stack = []

    for c in string:
        if c.isspace():
            # skip whitespace
            continue
        
        if c in "><+-.,":
            # add the simple operators to the operation list
            ops.append(c)

        elif c == "[":
            # save the current operations to the stack and start
            # accumulate instructions until ']' is encountered
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
            # report unrecognised character
            raise ParseError(f"Unknown character '{c}'")

    # report unmatched '['
    if stack:
        raise ParseError("Unmatched '['")

    return ops

