import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from calculatorLexer import calculatorLexer
from calculatorParser import calculatorParser
from MyVisitor import MyVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = calculatorLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = calculatorParser(token_stream)
    tree = parser.prog()

    visitor = MyVisitor()
    visitor.visit(tree)
