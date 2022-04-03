from player.tonesPlayer import TonesPlayer
from player.argParser import ArgParser
from csgparser.csgparse import *
import sys


def main():
    arg_parser = ArgParser(sys.argv)
    arg_parser.parse()
    csparse = SCGparser(arg_parser.get_theme())
    csparse.syntax_analysis()

    """callit = TonesPlayer(0.5, 44100, 1.0)
    callit.play()"""


if __name__ == '__main__':
    main()
