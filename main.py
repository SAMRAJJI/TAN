# main.py

from lexer import lexerexer
from parser import Parser
from interpreter import Interpreter
import sys

def run_tanglish_code(source_code):
    # Step 1: Lexical Analysis
    lexer = lexer(source_code)
    tokens = lexer.tokenize()

    # Step 2: Parsing
    parser = Parser(tokens)
    ast = parser.parse()

    # Step 3: Interpretation
    interpreter = Interpreter()
    interpreter.visit(ast)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>.tl")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            code = file.read()
            run_tanglish_code(code)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
