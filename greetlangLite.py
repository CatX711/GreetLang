import re

class Lexer:
    def __init__(self, file_path):
        self.tokens = []
        self.file_path = file_path
    
    def tokenize(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                self.tokens.extend(self._tokenize_line(line))
        
        return self.tokens
    
    def _tokenize_line(self, line):
        tokens = []
        
        output_pattern = re.compile(r'op\("([^"]*)"\);')
        
        while line:
            if match := output_pattern.match(line):
                string = match.group(1)
                tokens.append(('OUTPUT', string))
                line = line[len(match.group()):]
            elif line[0] == ' ':
                line = line[1:]
            else:
                raise ValueError(f"Invalid character: {line[0]}")
        
        return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()
    
    def next_token(self):
        if self.tokens:
            self.current_token = self.tokens.pop(0)
        else:
            self.current_token = None
    
    def parse(self):
        if self.current_token is None:
            raise ValueError("Unexpected end of input")

        while self.current_token is not None:  # Modified condition
            if self.current_token[0] == 'OUTPUT':
                self.parse_output()
            else:
                raise ValueError(f"Invalid token: {self.current_token[1]}")
        
    def parse_output(self):
        if self.current_token[0] == 'OUTPUT':
            string = self.current_token[1]
            print(string)  # Output the string
            self.next_token()
        else:
            raise ValueError(f"Invalid token: {self.current_token[1]}")

# Usage example
lexer = Lexer("hello.gll")  # Replace with the path to your file
tokens = lexer.tokenize()
parser = Parser(tokens)
parser.parse()

