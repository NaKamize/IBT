import xml.etree.ElementTree as ET


class InputExtractor:
    """ Class constructor with input file. """
    def __init__(self, file_name):
        self.__content_list = []
        self.__time_sig = None
        self.__file_name = file_name

    """ Form input file is extracted xml format and reformatted to small maps
        that are in format of TONE_NAME: LENGTH. Returns measure length to check it."""
    def __fill_list(self, measure):
        duration = 0
        cur_duration = 0
        # time signature checks
        if self.__time_sig == '4/4':
            duration = 4
        elif self.__time_sig == '2/4':
            duration = 2
        else:
            print("Wrong time signature.")
            exit(1)

        # List through measures and get their tones
        for tone in measure:
            if tone.tag != "tone":
                print("Wrong tone element.")
                exit(1)
            if tone.attrib['note'] == 'half':
                cur_duration += 2
            elif tone.attrib['note'] == 'full':
                cur_duration += 4
            else:
                cur_duration += 1
            self.__content_list.append({tone.text: tone.attrib['note']})
        return cur_duration

    """ Starts reading input file with basic node checks. """
    def read_input(self):
        tree = ET.parse(self.__file_name)
        root = tree.getroot()

        if root.tag != "theme":
            print("Wrong theme element")
            exit(1)

        if root.attrib['time_signature']:
            self.__time_sig = root.attrib['time_signature']
        else:
            print("Tiem signature in theme is missing.")
            exit(1)

        if self.__time_sig != '4/4' and self.__time_sig != '2/4':
            print("Wrong time signature.")
            exit(1)

        for measure in root:
            if measure.tag != "measure":
                print("Wrong measure element.")
                exit(1)
            measure = self.__fill_list(measure)
            if (measure != 4 and self.__time_sig == '4/4') and (measure != 2 and self.__time_sig == '2/4'):
                print("Wrong measure duration !")
                exit(1)

    """ Returns theme extracted from xml format. """
    def get_theme(self):
        return self.__content_list

    """ Returns time signature of a theme. """
    def get_time_sig(self):
        return self.__time_sig
