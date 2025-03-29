import re

KEYWORDS = {
    "ezhuthu": "PRINT",
    "varuval": "VAR"
}

TOKEN_REGEX = [
    (r'\b\d+\b', "NUMBER"),          # Numbers
    (r'\"[^\"]*\"', "STRING"),       # Strings inside double quotes
    (r'\b[a-zA-Z_]\w*\b', "IDENTIFIER"),  # Identifiers (variable names)
    (r'[=;+]', "SYMBOL"),            # Operators and semicolon
]

def lexer(code):
    tokens = []
    words = re.findall(r'\"[^\"]*\"|\b\w+\b|[=;+]', code)  # Tokenize by words and symbols
    
    for word in words:
        if word in KEYWORDS:
            tokens.append(("KEYWORD", KEYWORDS[word]))  # Recognize keywords
        elif re.match(r'\b\d+\b', word):
            tokens.append(("NUMBER", word))  # Recognize numbers
        elif re.match(r'\"[^\"]*\"', word):
            tokens.append(("STRING", word))  # Recognize strings
        elif re.match(r'\b[a-zA-Z_]\w*\b', word):
            tokens.append(("IDENTIFIER", word))  # Recognize identifiers
        elif word in "=;+":
            tokens.append(("SYMBOL", word))  # Recognize operators
        else:
            tokens.append(("UNKNOWN", word))  # Catch unknown tokens

    return tokens

# Test case
if __name__ == "__main__":
    code = 'ezhuthu "Vanakkam"; varuval x = 10;'
    print(lexer(code))
