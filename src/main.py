from player.tonesPlayer import TonesPlayer
from player.argParser import ArgParser
import sys


def main():
    ArgParser(sys.argv).parse()
    """callit = TonesPlayer(0.5, 44100, 1.0)
    callit.play()"""

if __name__ == '__main__':
    main()
