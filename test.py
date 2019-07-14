import unittest

from brainfuck import execute
from brainfuck.program import Program
from brainfuck.parse import parse


class TextExecute(unittest.TestCase):

    def test_execute_empty(self):
        program = ""
        execute(program)


    def test_execute_not_empty(self):
        program = "++++<<<<>>>>----."
        execute(program)


class TestProgram(unittest.TestCase):

    def test_modify_pointer(self):
        """
        Test that modify pointer increments and decrements
        the pointer by the correct amount, and wraps around
        by the correct number of cells.
        """

        program = Program(3)
        assertEqual(program.pointer, 0)
        program.modify_pointer(2)
        assertEqual(program.pointer, 2)
        program.modify_pointer(-2)
        assertEqual(program.pointer, 0)
        program.modifyPointer(3)
        assertEqual(program.pointer, 0)

    def test_increment_cell(self):
        """
        Test that executing a '+' operation increments the cell
        at the pointer by the correct amount.
        """

        program = Program(1)
        self.assertEqual(program.cell, 0)
        program.execute_one("+")
        self.assertEqual(program.cell, 1)


    def test_decrement_cell(self):
        """
        Test that executing a '-' operation decrements the cell
        at the pointer by the correct amount.
        """

        program = Program(1)
        program.cell = 1
        program.execute_one("-")
        self.assertEqual(program.cell, 0)

    
    def test_increment_pointer(self):
        """
        Test that executing a '>' command increments the pointer
        by the correct amount.
        There is no need to test wrapping, as it is accomodated
        by modify_pointer.
        """

        program = Program(2)
        self.assertEqual(program.pointer, 0)
        program.execute_one(">")
        self.assertEqual(program.pointer, 1)


    def test_decrement_pointer(self):
        """
        Test that executing a '>' command decrements the pointer
        by the correct amount.
        There is no need to test wrapping, as it is accomodated
        by modify_pointer.
        """

        program = Program(2)
        program.pointer = 1
        program.execute_one("<")
        self.assertEqual(program.pointer, 0)


    def test_loop(self):
        """
        Test that a simple loop will repeat until the end condition
        is met. The cell at the pointer should have a non-zero value
        before the loop and be zero when after the loop.
        """

        program = Program(1)
        program.cell = 3
        program.execute_one(["-"])
        self.assertEqual(program.pointer, 0)


    def test_loop_complex(self):
        """
        Test a complex program which uses a loop to multiply the contents
        of its first cell into its second cell, by reducing the
        first cell to zero in order to end the loop.
        """

        program = Program(2)
        program.execute_many(["+", "+", ["-", ">", "+", "+", "<"], ">"])
        self.assertEqual(program.pointer, 1)
        self.assertEqual(program.cell, 4)
        program.modify_pointer(-1)
        self.assertEqual(program.cell, 2)


if __name__ == "__main__":
    unittest.main()

