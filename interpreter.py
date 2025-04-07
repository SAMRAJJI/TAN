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

    def handle_print(self, value):
        if value.startswith('"') and value.endswith('"'):
            print(value[1:-1])
        elif value in self.variables:
            print(self.variables[value])
        else:
            print("ERROR: Undefined variable", value)

    def handle_assign(self, var_name, var_value):
        # Auto-detect type
        if var_value.isdigit():
            self.variables[var_name] = int(var_value)
        elif var_value.startswith('"') and var_value.endswith('"'):
            self.variables[var_name] = var_value[1:-1]
        elif var_value in self.variables:
            self.variables[var_name] = self.variables[var_value]
        else:
            print(f"ERROR: Invalid value '{var_value}' for variable '{var_name}'")

# Test
if __name__ == "__main__":
    from lexer import lexer
    from myparser import Parser

    code = 'a = 10; ezhuthu a;'
    tokens = lexer(code)
    parser = Parser(tokens)
    parsed_statements = parser.parse()
    interpreter = Interpreter(parsed_statements)
    interpreter.run()
