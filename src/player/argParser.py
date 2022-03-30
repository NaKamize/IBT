import argparse
import argparse as ap
import textwrap


class ArgParser:
    __repetition = False
    __transposition = False
    __sequence = False
    __contrary_motion = False
    __retro_gradation = False
    __augmentation = False
    __diminution = False

    def __init__(self, argv):
        self.__argv = argv

    def parse(self):
        arg_parser = ap.ArgumentParser(prog="musicgen",
                                       formatter_class=argparse.RawDescriptionHelpFormatter,
                                       description=textwrap.dedent('''\
                                            Program runs syntax analysis and apply grammar rules on the result of it.
                                            Based on arguments, that are given by user it generates music structure.
                                            This music structure is called theme and variations.
                                        '''))
        arg_parser.add_argument("-r", "--repetition", action='store_true', help="")
        arg_parser.add_argument("-t", "--transposition", action='store_true', help="")
        arg_parser.add_argument("-s", "--sequence", action='store_true', help="")
        arg_parser.add_argument("-c", "--contrary_motion", action='store_true', help="")
        arg_parser.add_argument("-R", "--retro_gradation", action='store_true', help="")
        arg_parser.add_argument("-a", "--augmentation", action='store_true', help="")
        arg_parser.add_argument("-d", "--diminution", action='store_true', help="")
        
        try:
            args = arg_parser.parse_args()
            self.__repetition = args.repetition
            self.__transposition = args.transposition
            self.__sequence = args.sequence
            self.__contrary_motion = args.contrary_motion
            self.__retro_gradation = args.retro_gradation
            self.__augmentation = args.augmentation
            self.__diminution = args.diminution
        except argparse.ArgumentError:
            print("Parsing of arguments has failed.")
