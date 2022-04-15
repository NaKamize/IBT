import argparse as ap
import textwrap
from os import path
import re
from csgparser.inputExtractor import InputExtractor


class ArgParser:
    __repetition = False
    __transposition = False
    __sequence_up = False
    __sequence_down = False
    __contrary_motion = False
    __retro_gradation = False
    __augmentation = False
    __diminution = False
    __input_file = None
    __theme = None
    __play = False
    __save = False
    __variations = []
    __time_sig = None

    """ Class contructor with arguments. """
    def __init__(self, argv):
        self.__argv = argv

    """ Creating argument parser and adding arguments into it.
        Then extracts variation flags and theme. """
    def parse(self):
        arg_parser = ap.ArgumentParser(prog="musicgen",
                                       formatter_class=ap.RawDescriptionHelpFormatter,
                                       description=textwrap.dedent('''\
                                            Program runs syntax analysis and apply grammar rules on the result of it.
                                            Based on arguments, that are given by user it generates music structure.
                                            This music structure is called theme and variations.
                                        '''))
        arg_parser.add_argument("-i", "--input", help="Input file, that contains theme.", required=True)
        arg_parser.add_argument("-r", "--repetition", action='store_true', help="Option to add repetition variation.")
        arg_parser.add_argument("-t", "--transposition", action='store_true', help="Option to add transposition "
                                                                                   "variation.")
        arg_parser.add_argument("-S", "--sequence-up", action='store_true',
                                help="Option to add down sequence variation.")
        arg_parser.add_argument("-s", "--sequence-down", action='store_true',
                                help="Option to add up sequence variation.")
        arg_parser.add_argument("-c", "--contrary_motion", action='store_true', help="Option to add contrary_motion "
                                                                                     "variation.")
        arg_parser.add_argument("-R", "--retro_gradation", action='store_true', help="Option to add retro_gradation "
                                                                                     "variation.")
        arg_parser.add_argument("-a", "--augmentation", action='store_true', help="Option to add augmentation "
                                                                                  "variation.")
        arg_parser.add_argument("-d", "--diminution", action='store_true', help="Option to add diminution variation.")
        arg_parser.add_argument("-p", "--play", action='store_true', help="Output is being played.")
        arg_parser.add_argument("--save", action='store_true', help="Save sound of the output next to input file.")

        try:
            args = arg_parser.parse_args()
            self.__repetition = args.repetition
            self.__transposition = args.transposition
            self.__sequence_up = args.sequence_up
            self.__sequence_down = args.sequence_down
            self.__contrary_motion = args.contrary_motion
            self.__retro_gradation = args.retro_gradation
            self.__augmentation = args.augmentation
            self.__diminution = args.diminution
            self.__input_file = args.input
            self.__play = args.play
            self.__save = args.save
        except ap.ArgumentError:
            print("Parsing of arguments has failed.")

        """ If no variation type was inputted, then it is error"""
        if not self.__repetition and not self.__transposition and not self.__sequence_up and not self.__sequence_down \
                and not self.__contrary_motion and not self.__retro_gradation \
                and not self.__augmentation and not self.__diminution:
            print("Variation type was not selected.")
            exit(1)

        if self.__input_file is None:
            print("Input file is missing.")
            exit(1)

        if not path.isfile(self.__input_file):
            print("Theme file doest not exists.")
            exit(1)

        if not re.match(r'.*xml', self.__input_file):
            print("File has wrong format.")
            exit(1)

        input_e = InputExtractor(self.__input_file)
        input_e.read_input()
        if self.__repetition:
            self.__variations.append('rep')
        if self.__transposition:
            self.__variations.append('trans')
        if self.__sequence_up:
            self.__variations.append('seq+')
        if self.__sequence_down:
            self.__variations.append('seq-')
        if self.__contrary_motion:
            self.__variations.append('con')
        if self.__retro_gradation:
            self.__variations.append('grad')
        if self.__augmentation:
            self.__variations.append('aug')
        if self.__diminution:
            self.__variations.append('dimi')
        self.__theme = input_e.get_theme()
        self.__time_sig = input_e.get_time_sig()

    """ Return input theme content. """
    def get_theme(self):
        return self.__theme

    """ Return variation that have to be done. """
    def get_variations(self):
        return self.__variations

    """ Returns filename. """
    def get_file(self):
        return self.__input_file

    """ Play result of syntax analysis. """
    def do_play(self):
        return self.__play

    """ Save wav file. """
    def do_save(self):
        return self.__save

    def get_time_sig(self):
        return self.__time_sig
