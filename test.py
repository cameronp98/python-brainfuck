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

    def test_init_pointer(self):
        """
        Test that the program's pointer is initialised at 0.
        """

        program = Program(3)
        self.assertEqual(program.pointer, 0,
                "Pointer should equal 0")

    
    def test_init_cells(self):
        """
        Test that the program has the right number of cells,
        with all initialised to zero.
        """

        program = Program(4)
        self.assertEqual(program.cells, [0, 0, 0, 0],
                "Program should have 4 cells initialised to 0")


    def test_modify_pointer(self):
        """
        Test that modify pointer increments and decrements
        the pointer by the correct amount, and wraps around
        by the correct number of cells.
        """

        program = Program(3)
        program.modify_pointer(2)
        self.assertEqual(program.pointer, 2,
                "Pointer should be incremented by 2")
        program.modify_pointer(-2)
        self.assertEqual(program.pointer, 0,
                "Pointer should be decremented by 2")
        program.modifyPointer(3)
        self.assertEqual(program.pointer, 0,
                "Pointer should be incremented by 3 and wrap around")


    def test_increment_cell(self):
        """
        Test that executing a '+' operation increments the cell
        at the pointer by the correct amount.
        """

        program = Program(1)
        program.execute_one("+")
        self.assertEqual(program.cell, 1,
                "Cell should be incremented to 1")


    def test_decrement_cell(self):
        """
        Test that executing a '-' operation decrements the cell
        at the pointer by the correct amount.
        """

        program = Program(1)
        program.cell = 1
        program.execute_one("-")
        self.assertEqual(program.cell, 0,
                "Cell should be decremented to 0")

    
    def test_increment_pointer(self):
        """
        Test that executing a '>' command increments the pointer
        by the correct amount.
        There is no need to test wrapping, as it is accomodated
        by modify_pointer.
        """

        program = Program(2)
        program.execute_one(">")
        self.assertEqual(program.pointer, 1,
                "Pointer should be incremented by 1")


    def test_decrement_pointer(self):
        """
        Test that executing a '<' command decrements the pointer
        by the correct amount.
        There is no need to test wrapping, as it is accomodated
        by modify_pointer.
        """

        program = Program(2)
        program.modify_pointer(1)
        program.execute_one("<")
        self.assertEqual(program.pointer, 0,
                "Pointer should be decremented by 1")


    def test_loop(self):
        """
        Test that a simple loop will repeat until the end condition
        is met. The cell at the pointer should have a non-zero value
        before the loop and be zero when after the loop.
        """

        program = Program(1)
        program.cell = 3
        program.execute_one(["-"])
        self.assertEqual(program.pointer, 0,
                "Pointer should be reduced to 0")


    @unittest.skip("Buggy")
    def test_loop_complex(self):
        """
        Test a complex program which uses a loop to multiply the contents
        of its first cell into its second cell, by reducing the
        first cell to zero in order to end the loop.
        """

        program = Program(2)
        program.execute_many(["+", "+", ["-", ">", "+", "+", "<"], ">"])

        if program.pointer == 1 and program.pointer == 4:
            self.assertEqual(program.cells[0], 0,
                    "Cell 0 should be 0")
        else:
            self.fail("Should be at cell 1 with value 4")


if __name__ == "__main__":
    unittest.main()

