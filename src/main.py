from player.tonesPlayer import TonesPlayer
from player.argParser import ArgParser
from csgparser.csgparse import *
import sys


def main():
    arg_parser = ArgParser(sys.argv)
    arg_parser.parse()  # parsing arguments
    csgparse = SCGparser(arg_parser.get_theme(), arg_parser.get_variations())
    csgparse.syntax_analysis()   # Syntax analysis of variations
    variations = csgparse.get_result()  # save result
    synthesizer = TonesPlayer(variations, 0.5)  # initialization of synthesizer class

    if arg_parser.do_play():
        synthesizer.play()
    if arg_parser.do_save():
        file_name = arg_parser.get_file()[:-3]  # remove last 3 chars and add wav sufix
        synthesizer.save(file_name + 'wav')


if __name__ == '__main__':
    main()
