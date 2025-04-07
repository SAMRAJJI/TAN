from lexer import lexer
from myparser import Parser
from interpreter import Interpreter

def run(filename):
    with open(filename, 'r') as file:
        code = file.read()

    tokens = lexer(code)
    parser = Parser(tokens)
    parsed_statements = parser.parse()
    interpreter = Interpreter(parsed_statements)
    interpreter.run()

if __name__ == '__main__':
    run('test.tl')
