import argparse as ap
import textwrap
from os import path
from player.inputExtractor import InputExtractor


class ArgParser:
    __repetition = False
    __transposition = False
    __sequence = False
    __contrary_motion = False
    __retro_gradation = False
    __augmentation = False
    __diminution = False
    __input_file = None
    __theme = None

    def __init__(self, argv):
        self.__argv = argv

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
        arg_parser.add_argument("-s", "--sequence", action='store_true', help="Option to add sequence variation.")
        arg_parser.add_argument("-c", "--contrary_motion", action='store_true', help="Option to add contrary_motion "
                                                                                     "variation.")
        arg_parser.add_argument("-R", "--retro_gradation", action='store_true', help="Option to add retro_gradation "
                                                                                     "variation.")
        arg_parser.add_argument("-a", "--augmentation", action='store_true', help="Option to add augmentation "
                                                                                  "variation.")
        arg_parser.add_argument("-d", "--diminution", action='store_true', help="Option to add diminution variation.")
        arg_parser.add_argument("-p", "--play", action='store_true', help="Output is being played.")

        try:
            args = arg_parser.parse_args()
            self.__repetition = args.repetition
            self.__transposition = args.transposition
            self.__sequence = args.sequence
            self.__contrary_motion = args.contrary_motion
            self.__retro_gradation = args.retro_gradation
            self.__augmentation = args.augmentation
            self.__diminution = args.diminution
            self.__input_file = args.input
        except ap.ArgumentError:
            print("Parsing of arguments has failed.")

        if self.__input_file is None:
            print("Input file is missing.")
            exit(1)

        if not path.isfile(self.__input_file):
            print("Theme file doest not exists.")
            exit(1)

        input_e = InputExtractor(self.__input_file)
        input_e.read_input()
        self.__theme = input_e.get_theme()

    def get_theme(self):
        return self.__theme
