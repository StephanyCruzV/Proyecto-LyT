import sys                      #
from antlr4 import *            #
from SCVLexer import SCVLexer   #
from SCVParser import SCVParser #
from interpreter import *       #
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = SCVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SCVParser(stream)
    tree = parser.program()

    interpreter = Interpreter()
    walker = ParseTreeWalker()
    walker.walk(interpreter, tree)

 
if __name__ == '__main__':
    main(sys.argv)