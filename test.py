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

    def test_increment_cell(self):
        program = Program(1)
        self.assertEqual(program.cell, 0)
        program.execute_one("+")
        self.assertEqual(program.cell, 1)


    def test_decrement_cell(self):
        program = Program(1)
        program.cell = 1
        program.execute_one("-")
        self.assertEqual(program.cell, 0)

    
    def test_increment_pointer(self):
        program = Program(1)
        self.assertEqual(program.pointer, 0)
        program.execute_one(">")
        self.assertEqual(program.pointer, 1)


    def test_decrement_pointer(self):
        program = Program(1)
        program.pointer = 1
        program.execute_one("<")
        self.assertEqual(program.pointer, 0)


    def test_loop(self):
        program = Program(1)
        program.cell = 3
        program.execute_one(["-"])
        self.assertEqual(program.pointer, 0)


    def test_loop_complex(self):
        program = Program(2)
        program.execute_many(["+", "+", ["-", ">", "+", "+", "<"], ">"])
        self.assertEqual(program.pointer, 1)
        self.assertEqual(program.cell, 4)
        program.modify_pointer(-1)
        self.assertEqual(program.cell, 2)


if __name__ == "__main__":
    unittest.main()

