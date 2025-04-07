class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        statements = []
        while self.position < len(self.tokens):
            token_type, value = self.tokens[self.position]

            if token_type == "KEYWORD" and value == "PRINT":
                statements.append(self.parse_print())
            elif token_type == "IDENTIFIER":
                statements.append(self.parse_assignment())
            else:
                print(f"ERROR: Unexpected token '{value}' at position {self.position}")
                self.position += 1
        return statements

    def parse_print(self):
        self.position += 1
        if self.position >= len(self.tokens):
            print("ERROR: Expected value after 'ezhuthu'")
            return None

        value = self.tokens[self.position][1]
        self.position += 1

        if self.position < len(self.tokens) and self.tokens[self.position][1] == ";":
            self.position += 1
        else:
            print("ERROR: Missing ';' at end of print statement")
            return None

        return ("PRINT", value)

    def parse_assignment(self):
        var_name = self.tokens[self.position][1]
        self.position += 1

        if self.position >= len(self.tokens) or self.tokens[self.position][1] != "=":
            print(f"ERROR: Expected '=' after variable name '{var_name}'")
            return None

        self.position += 1

        if self.position >= len(self.tokens):
            print(f"ERROR: Expected value after '=' for '{var_name}'")
            return None

        var_value = self.tokens[self.position][1]
        self.position += 1

        if self.position < len(self.tokens) and self.tokens[self.position][1] == ";":
            self.position += 1
        else:
            print("ERROR: Missing ';' at end of assignment")
            return None

        return ("ASSIGN", var_name, var_value)

# Test
if __name__ == "__main__":
    from lexer import lexer

    code = 'a = 5; ezhuthu a;'
    tokens = lexer(code)
    parser = Parser(tokens)
    print(parser.parse())
