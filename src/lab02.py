# Add Your Names Here

from sly import Lexer, Parser

class MyLexer(Lexer):
    # TODO: add tokens and definitions

class MyParser(Parser):
    tokens = CalcLexer.tokens

    # TODO: add rules

if __name__ == '__main__':
    lexer = MyLexer()
    parser = MyParser()
