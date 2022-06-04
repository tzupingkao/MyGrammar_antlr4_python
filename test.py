import sys
from antlr4 import *
from MyGrammar.MyGrammarLexer import MyGrammarLexer
from MyGrammar.MyGrammarParser import MyGrammarParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    tree = parser.expr()
 
if __name__ == '__main__':
    main(sys.argv)


