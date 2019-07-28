import unittest
from gdsort import SortScript
from io import StringIO
import sys

class TestSortScript(unittest.TestCase):

    def setUp(self):
        self.filename = 'test.gd'
        self.sort_script = SortScript(self.filename)
        self.function_names = ['_ready', 'func1', 'func2', 'func3', 'process']

    def test_get_func_name__should_return_function_name(self):
        self.assertEqual(self.sort_script.get_func_name('function1():\n'), 'function1', "Function name not returned correctly")

    def test_parse_script__should_return_functions(self):
        with open(self.filename, 'r') as f:
            self.sort_script.parse_script(f)
        functions = [f.name for f in self.sort_script.functions]
        self.assertCountEqual(functions, self.function_names, "Not all functions were captured")

    def test_write_script__output_should_return_as_golden_file(self):
        # Sort the functions before we write. This is done in exec()
        self.sort_script.sort_functions()

        # Capture the output of our function
        mock_output = StringIO()
        self.sort_script.write_script(mock_output)

        self.assertEqual(mock_output.getvalue(), self.get_golden_data())
            
        
    def get_golden_data(self):
        data = ''
        with open('golden_file.gd', 'r') as f:
            data = f.read()
        return data

if __name__ == '__main__':
    unittest.main()