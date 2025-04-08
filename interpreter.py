import re
class Interpreter:
    def __init__(self, parsed_statements):
        self.parsed_statements = parsed_statements
        self.variables = {}

    def run(self):
        for statement in self.parsed_statements:
            if statement is None:
                continue
            if statement[0] == "PRINT":
                self.handle_print(statement[1])
            elif statement[0] == "ASSIGN":
                self.handle_assign(statement[1], statement[2])

    def handle_print(self, expression):
        result = self.evaluate_expression(expression)
        if result is not None:
            print(result)

    def handle_assign(self, var_name, expression):
        result = self.evaluate_expression(expression)
        if result is not None:
            self.variables[var_name] = result

    def evaluate_expression(self, expr):
        if not expr:
            return None
        expr_str = ""
        for token in expr:
            if token in self.variables:
                expr_str += str(self.variables[token])
            else:
                expr_str += token
        try:
            return eval(expr_str)
        except Exception as e:
            print(f"ERROR: Invalid expression '{' '.join(expr)}' — {e}")
            return None

if __name__ == "__main__":
    import re
    from lexer import lexer
    from myparser import Parser

    code = '''
    a = 10 + 5;
    b = a * 2;
    c = b / 3;
    ezhuthu c;
    '''
    tokens = lexer(code)
    parser = Parser(tokens)
    parsed_statements = parser.parse()
    interpreter = Interpreter(parsed_statements)
    interpreter.run()
