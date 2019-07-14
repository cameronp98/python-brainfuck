"""
Model the state of a brainfuck program and
act upon it using brainfuck operations.
"""

class ExecutionError(Exception):
    pass


class Program:
    """Represents the execution state of a brainfuck program."""

    def __init__(self, num_cells):
        self.cells = [0 * num_cells]
        self.pointer = 0

    
    @property
    def cell(self):
        return self.cells[self.pointer]
    

    @cell.setter
    def cell(self, value):
        self.cells[self.pointer] = value


    def modify_pointer(self, amount):
        self.pointer = (self.pointer + amount) % len(self.cells)


    def execute_one(self, op):
        """
        Executes the given operation.
        """

        if isinstance(op, list):
            # If the cell at the pointer is non-zero, execute the 
            # operations inside the loop.
            # If the cell at the pointer is still non-zero, repeat.
            while self.cell != 0:
                self.execute_many(op)
                if self.cell == 0:
                    break

        elif op == "+":
            # increment the cell at the pointer
            self.cell += 1

        elif op == "-":
            # decrement the cell at the pointer
            self.cell -= 1

        elif op == ">":
            # move the pointer one cell to the right
            self.modify_pointer(+1)

        elif op == "<":
            # move the pointer one cell to the left
            self.modify_pointer(-1)

        elif op == ".":
            # output the cell at the pointer
            print(self.cell)
            
        elif op == ",":
            # input the cell at the pointer as either a number,
            # or a single character
            value = input(f"Input for cell {self.pointer}: ")
            if value.isnumeric():
                self.cell = int(value)
            elif len(value) == 1:
                self.cell = ord(value)
            else:
                raise ExecutionError(
                        "Input must be a number or a single character")

        else:
            ExecutionError(f"Unknown operation: {op}")
    
    
    def execute_many(self, ops):
        """
        Executes many operations sequentially.
        """

        for op in ops:
            self.execute_one(op)


