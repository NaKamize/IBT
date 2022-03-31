import xml.etree.ElementTree as ET


class InputExtractor:
    def __init__(self, file_name):
        self.__content_list = []
        self.__time_sig = None
        self.__file_name = file_name

    def __fill_list(self, measure):
        for tone in measure:
            if tone.tag != "tone":
                print("Wrong tone element.")
                exit(1)
            self.__content_list.append({tone.attrib['note']: tone.text})

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

        for measure in root:
            if measure.tag != "measure":
                print("Wrong measure element.")
                exit(1)
            self.__fill_list(measure)

    def get_theme(self):
        return self.__content_list

    def get_time_sig(self):
        return self.__time_sig
