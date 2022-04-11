from csgparser.tonesPlayer import TonesPlayer
from csgparser.argParser import ArgParser
from csgparser.csgparse import *
from csgparser.xmlGenerator import Generator
import sys


def main():
    arg_parser = ArgParser(sys.argv)
    arg_parser.parse()  # parsing arguments
    csgparse = SCGparser(arg_parser.get_theme(), arg_parser.get_variations())
    csgparse.syntax_analysis()   # Syntax analysis of variations
    variations = csgparse.get_result()  # save result
    print(variations)
    synthesizer = TonesPlayer(variations, 0.5)  # initialization of synthesizer class

    if arg_parser.do_play():
        synthesizer.play()
    if arg_parser.do_save():
        file_name = arg_parser.get_file()[:-3]  # remove last 3 chars and add wav sufix
        synthesizer.save(file_name + 'wav')
    xml_generator = Generator(variations)
    xml_generator.generate()

if __name__ == '__main__':
    main()
