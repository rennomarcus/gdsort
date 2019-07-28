import re
from func import Func
import sys

class SortScript:
    script_name = ''
    functions = []
    general_content = []

    def __init__(self, script_name):
        self.script_name

    def get_func_name(self, word):
        return word[:word.find('(')]

    def debug(self):
        print(self.functions)
        print(self.general_content)
        print('-------------')
        for f in self.functions:
            print("###############")
            print(f.name)
            print("-----")
            for c in f.content:
                print(c, end='')

    def parse_script(self, file_object):
        func_counter = -1
        line_counter = -1
        func = Func('')
    
        for line in file_object.readlines():
            line_counter += 1
            splitted = line.split(' ')
            if splitted[0] == 'func':
                func_name = self.get_func_name(splitted[1])
                func = Func(func_name)
                func.add_content(line)
                self.functions.append(func)
                func_counter = line_counter
            
            elif re.match(r'\s', splitted[0]) and func_counter != -1:
                func.add_content(line)
            else:
                self.general_content.append(line)
                func_counter = -1

    def sort_functions(self):
        self.functions.sort()

    def write_script(self, file_object):
        for line in self.general_content:
            file_object.write(line)
        for func in self.functions:
            for c in func.content:
                file_object.write(c)
            
    def exec(self):
        with open(self.script_name, 'r') as file_object:
            sort_script.parse_script(file_object)

        sort_script.sort_functions()

        with open(self.script_name, 'w') as file_object:
            sort_script.write_script(file_object)

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Error. Please insert the script")
    else:
        sort_script = SortScript(sys.argv[1])
        sort_script.exec()