from player.tonesPlayer import TonesPlayer
from player.argParser import ArgParser
from csgparser.csgparse import *
import sys


def main():
    arg_parser = ArgParser(sys.argv)
    arg_parser.parse()
    print(arg_parser.get_file())
    csgparse = SCGparser(arg_parser.get_theme(), arg_parser.get_variations())
    csgparse.syntax_analysis()
    variations = csgparse.get_result()
    print(variations)
    callit = TonesPlayer(variations, 0.5)
    #callit.play()


if __name__ == '__main__':
    main()
