# Author: Jozef Makiš
# License: GPLv3
# File: variator.py

from csgparser.tonesPlayer import TonesPlayer
from csgparser.argParser import ArgParser
from csgparser.csgParser import SCGparser
from csgparser.xmlGenerator import Generator
import sys


def main():
    arg_parser = ArgParser(sys.argv)
    arg_parser.parse()  # parsing arguments
    csgparse = SCGparser(arg_parser.get_theme(), arg_parser.get_variations())
    csgparse.variator()   # Syntax analysis of variations
    variations = csgparse.get_result()  # save result
    volume = arg_parser.get_volume()
    if volume is not None:
        synthesizer = TonesPlayer(variations, volume)  # initialization of synthesizer class
    else:
        synthesizer = TonesPlayer(variations, 0.2)  # initialization of synthesizer class

    if arg_parser.do_play():
        synthesizer.play()
    if arg_parser.do_save():
        file_name = arg_parser.get_file()[:-3]  # remove last 3 chars and add wav sufix
        synthesizer.save(file_name + 'wav')

    xml_generator = Generator(variations, arg_parser.get_time_sig())  # generating output xml format
    xml_generator.generate()


if __name__ == '__main__':
    main()
