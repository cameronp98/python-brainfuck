"""
Parse brainfuck programs into operations.
"""

class ParseError(Exception):
    pass


def parse(string):
    """Parse the given string into a list of operators and loops"""

    ops = []
    stack = []

    for c in program:
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
            # report unrecognised character
            raise ParseError(f"Unknown character '{c}'")

    # report unmatched '['
    if stack:
        raise ParseError("Unmatched '['")

    return ops

