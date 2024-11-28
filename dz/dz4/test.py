import unittest
from assembler import assemble
from interpreter import execute
import json
import subprocess

class TestUVM(unittest.TestCase):
    def setUp(self):
        self.test_asm_path = "test_program.asm"
        self.test_bin_path = "test_program.bin"
        self.test_log_path = "test_program.json"
        self.test_result_path = "results_test_program.json"

    def test_assembler_and_interpreter(self):
        assemble(self.test_asm_path, self.test_bin_path, self.test_log_path)
        execute(self.test_bin_path, self.test_result_path, "1000:1007")
        with open(self.test_result_path, 'r') as f:
            result = json.loads(f.read())
        expected_result = [
            121,
            8,
            16,
            24,
            33,
            41,
            49,
            57
        ]
        self.assertTrue(result == expected_result)

if __name__ == '__main__':
    unittest.main()