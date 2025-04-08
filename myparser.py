class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        statements = []
        while self.position < len(self.tokens):
            token_type, value = self.tokens[self.position]

            if token_type == "KEYWORD" and value == "PRINT":
                stmt = self.parse_print()
                if stmt:
                    statements.append(stmt)
            elif token_type == "IDENTIFIER":
                stmt = self.parse_assignment()
                if stmt:
                    statements.append(stmt)
            else:
                print(f"ERROR: Unexpected token '{value}' at position {self.position}")
                self.position += 1
        return statements

    def parse_print(self):
        self.position += 1  # Skip 'PRINT' token

        if self.position >= len(self.tokens):
            print("ERROR: Expected value after 'ezhuthu'")
            return None

        expression = self.parse_expression()

        if not self.expect_symbol(";"):
            print("ERROR: Missing ';' at end of print statement")
            return None

        return ("PRINT", expression)

    def parse_assignment(self):
        var_name = self.tokens[self.position][1]
        self.position += 1  # Move past the variable name

        if not self.expect_symbol("="):
            print(f"ERROR: Expected '=' after variable name '{var_name}'")
            return None

        expression = self.parse_expression()

        if not self.expect_symbol(";"):
            print("ERROR: Missing ';' at end of assignment")
            return None

        return ("ASSIGN", var_name, expression)

    def parse_expression(self):
        expr = []
        while self.position < len(self.tokens):
            token_type, value = self.tokens[self.position]
            if token_type == "SYMBOL" and value == ";":
                break
            if token_type != "KEYWORD":  # Skip any keywords
                expr.append(value)
            self.position += 1
        return expr

    def expect_symbol(self, symbol):
        if self.position < len(self.tokens) and self.tokens[self.position][1] == symbol:
            self.position += 1
            return True
        return False


# Test
if __name__ == "__main__":
    from lexer import lexer

    code = 'a = 5 + 3; ezhuthu a;'
    tokens = lexer(code)
    parser = Parser(tokens)
    print(parser.parse())
