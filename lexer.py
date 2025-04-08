import re

KEYWORDS = {
    "ezhuthu": "PRINT"
}

TOKEN_REGEX = [
    (r'\b\d+\b', "NUMBER"),          # Numbers
    (r'\"[^\"]*\"', "STRING"),       # Strings inside quotes
    (r'\b[a-zA-Z_]\w*\b', "IDENTIFIER"),  # Variable names
    (r'[=;+*/-]', "SYMBOL"),            # Operators and punctuation
]

def lexer(code):
    tokens = []
    words = re.findall(r'\"[^\"]*\"|\b\w+\b|[=;+*/-]', code)

    for word in words:
        if word in KEYWORDS:
            tokens.append(("KEYWORD", KEYWORDS[word]))
        elif re.match(r'\b\d+\b', word):
            tokens.append(("NUMBER", word))
        elif re.match(r'\"[^\"]*\"', word):
            tokens.append(("STRING", word))
        elif re.match(r'\b[a-zA-Z_]\w*\b', word):
            tokens.append(("IDENTIFIER", word))
        elif word in "=;+*/-":
            tokens.append(("SYMBOL", word))
        else:
            tokens.append(("UNKNOWN", word))
    return tokens

# Test
if __name__ == "__main__":
    code = 'ezhuthu "Vanakkam"; a = 10; ezhuthu a;'
    print(lexer(code))
