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

            elif token_type == "KEYWORD" and value == "VAR":
                statements.append(self.parse_variable())

            else:
                print(f"ERROR: Unexpected token '{value}' at position {self.position}")
                self.position += 1  # Skip unknown tokens

        return statements

    def parse_print(self):
        """Parse PRINT statements like: ezhuthu "Hello";"""
        self.position += 1
        if self.position >= len(self.tokens):
            print("ERROR: Expected a value after 'ezhuthu'")
            return None
        
        value = self.tokens[self.position][1]
        self.position += 1  # Move past the value

        # Check if the next token is ';'
        if self.position < len(self.tokens) and self.tokens[self.position][1] == ";":
            self.position += 1  # Move past the semicolon
        else:
            print("ERROR: Missing ';' at the end of print statement")
            return None

        return ("PRINT", value)

    def parse_variable(self):
        """Parse variable assignments like: varuval x = 10;"""
        self.position += 1  # Move to variable name
        if self.position >= len(self.tokens):
            print("ERROR: Expected variable name after 'varuval'")
            return None
        
        var_name = self.tokens[self.position][1]

        self.position += 1  # Move past variable name
        if self.position >= len(self.tokens) or self.tokens[self.position][1] != "=":
            print(f"ERROR: Expected '=' after variable name '{var_name}'")
            return None

        self.position += 1  # Move to variable value
        if self.position >= len(self.tokens):
            print(f"ERROR: Expected a value after '=' for variable '{var_name}'")
            return None

        var_value = self.tokens[self.position][1]

        self.position += 1  # Move past the value

        # Ensure the next token is a semicolon
        if self.position < len(self.tokens) and self.tokens[self.position][1] == ";":
            self.position += 1  # Move past the semicolon
        else:
            print("ERROR: Missing ';' at the end of variable declaration")
            return None

        return ("VAR", var_name, var_value)

if __name__ == "__main__":
    from TAN.lexer import lexer
    
    code = 'ezhuthu "Vanakkam"; varuval x = 10;'
    tokens = lexer(code)
    parser = Parser(tokens)
    print(parser.parse())
