class Interpreter:
    def __init__(self, parsed_statements):
        self.parsed_statements = parsed_statements
        self.variables = {}  # Store variables

    def run(self):
        for statement in self.parsed_statements:
            if statement[0] == "PRINT":
                self.handle_print(statement[1])
            elif statement[0] == "VAR":
                self.handle_var(statement[1], statement[2])

    def handle_print(self, value):
        if value.startswith('"') and value.endswith('"'):  # String
            print(value[1:-1])  # Remove quotes
        elif value in self.variables:  # Variable
            print(self.variables[value])
        else:
            print("ERROR: Undefined variable", value)

    def handle_var(self, var_name, var_value):
        self.variables[var_name] = int(var_value)  # Store variable

# Test case
if __name__ == "__main__":
    from lexer import lexer
    from myparser import Parser

    code = 'ezhuthu "Vanakkam"; varuval x = 10; ezhuthu x;'
    tokens = lexer(code)
    parser = Parser(tokens)
    parsed_statements = parser.parse()
    interpreter = Interpreter(parsed_statements)
    interpreter.run()
