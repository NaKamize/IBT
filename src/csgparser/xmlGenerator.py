# Author: Jozef Makiš
# License: GPLv3
# File: xmlGenerator.py

from xml.dom import minidom


class Generator:
    """ Generator generates output in xml format. It was two class variables for root element and variation element."""
    __root = None
    __xml = None
    __is_crossed = False
    """ Class constructor with resulting variations. """
    def __init__(self, variations, measure):
        self.__variations = variations
        self.__measure = measure

    """ Method creates text node with tone name. 
        text ic tone name
        tone_element is element which is named by text """
    def __create_text_node(self, text, tone_element):
        text_node = self.__root.createTextNode(text)
        tone_element.appendChild(text_node)

    """ Method creates tone element with length attribute.
        text is name of a tone
        attrib is length of a tone
        variation_element is element, which contains all tones """
    def __creat_note_node(self, text, attrib, variation_element):
        tone_element = self.__root.createElement("tone")
        tone_element.setAttribute('note', attrib)
        variation_element.appendChild(tone_element)
        self.__create_text_node(text, tone_element)

    """ Method creates note element based on tokens from resulting variation. """
    def __generate_measures(self, variation, variation_element):
        max_length = int(self.__measure[0])  # get measure count
        current_length = max_length  # begin with creating measure element
        measure_element = None
        for tone in variation:
            if current_length == max_length:
                measure_element = self.__root.createElement("measure")
                variation_element.appendChild(measure_element)
                current_length = 0
            elif current_length > max_length and current_length == 4:
                measure_element = self.__root.createElement("measure")
                variation_element.appendChild(measure_element)
                current_length = 0
                self.__is_crossed = True
            if tone == 0:
                self.__creat_note_node('c1', 'full', measure_element)
                current_length += 4
            elif tone == 1:
                self.__creat_note_node('c1', 'half', measure_element)
                current_length += 2
            elif tone == 2:
                self.__creat_note_node('c1', 'quarter', measure_element)
                current_length += 1
            elif tone == 3:
                self.__creat_note_node('c1', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 4:
                self.__creat_note_node('d1', 'full', measure_element)
                current_length += 4
            elif tone == 5:
                self.__creat_note_node('d1', 'half', measure_element)
                current_length += 2
            elif tone == 6:
                self.__creat_note_node('d1', 'quarter', measure_element)
                current_length += 1
            elif tone == 7:
                self.__creat_note_node('d1', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 8:
                self.__creat_note_node('e1', 'full', measure_element)
                current_length += 4
            elif tone == 9:
                self.__creat_note_node('e1', 'half', measure_element)
                current_length += 2
            elif tone == 10:
                self.__creat_note_node('e1', 'quarter', measure_element)
                current_length += 1
            elif tone == 11:
                self.__creat_note_node('e1', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 12:
                self.__creat_note_node('f1', 'full', measure_element)
                current_length += 4
            elif tone == 13:
                self.__creat_note_node('f1', 'half', measure_element)
                current_length += 2
            elif tone == 14:
                self.__creat_note_node('f1', 'quarter', measure_element)
                current_length += 1
            elif tone == 15:
                self.__creat_note_node('f1', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 16:
                self.__creat_note_node('g1', 'full', measure_element)
                current_length += 4
            elif tone == 17:
                self.__creat_note_node('g1', 'half', measure_element)
                current_length += 2
            elif tone == 18:
                self.__creat_note_node('g1', 'quarter', measure_element)
                current_length += 1
            elif tone == 19:
                self.__creat_note_node('g1', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 20:
                self.__creat_note_node('a1', 'full', measure_element)
                current_length += 4
            elif tone == 21:
                self.__creat_note_node('a1', 'half', measure_element)
                current_length += 2
            elif tone == 22:
                self.__creat_note_node('a1', 'quarter', measure_element)
                current_length += 1
            elif tone == 23:
                self.__creat_note_node('a1', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 24:
                self.__creat_note_node('h1', 'full', measure_element)
                current_length += 4
            elif tone == 25:
                self.__creat_note_node('h1', 'half', measure_element)
                current_length += 2
            elif tone == 26:
                self.__creat_note_node('h1', 'quarter', measure_element)
                current_length += 1
            elif tone == 27:
                self.__creat_note_node('h1', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 28:
                self.__creat_note_node('c2', 'full', measure_element)
                current_length += 4
            elif tone == 29:
                self.__creat_note_node('c2', 'half', measure_element)
                current_length += 2
            elif tone == 30:
                self.__creat_note_node('c2', 'quarter', measure_element)
                current_length += 1
            elif tone == 31:
                self.__creat_note_node('c2', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 32:
                self.__creat_note_node('d2', 'full', measure_element)
                current_length += 4
            elif tone == 33:
                self.__creat_note_node('d2', 'half', measure_element)
                current_length += 2
            elif tone == 34:
                self.__creat_note_node('d2', 'quarter', measure_element)
                current_length += 1
            elif tone == 35:
                self.__creat_note_node('d2', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 36:
                self.__creat_note_node('e2', 'full', measure_element)
                current_length += 4
            elif tone == 37:
                self.__creat_note_node('e2', 'half', measure_element)
                current_length += 2
            elif tone == 38:
                self.__creat_note_node('e2', 'quarter', measure_element)
                current_length += 1
            elif tone == 39:
                self.__creat_note_node('e2', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 40:
                self.__creat_note_node('f2', 'full', measure_element)
                current_length += 4
            elif tone == 41:
                self.__creat_note_node('f2', 'half', measure_element)
                current_length += 2
            elif tone == 42:
                self.__creat_note_node('f2', 'quarter', measure_element)
                current_length += 1
            elif tone == 43:
                self.__creat_note_node('f2', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 44:
                self.__creat_note_node('g2', 'full', measure_element)
                current_length += 4
            elif tone == 45:
                self.__creat_note_node('g2', 'half', measure_element)
                current_length += 2
            elif tone == 46:
                self.__creat_note_node('g2', 'quarter', measure_element)
                current_length += 1
            elif tone == 47:
                self.__creat_note_node('g2', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 48:
                self.__creat_note_node('a2', 'full', measure_element)
                current_length += 4
            elif tone == 49:
                self.__creat_note_node('a2', 'half', measure_element)
                current_length += 2
            elif tone == 50:
                self.__creat_note_node('a2', 'quarter', measure_element)
                current_length += 1
            elif tone == 51:
                self.__creat_note_node('a2', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 52:
                self.__creat_note_node('h2', 'full', measure_element)
                current_length += 4
            elif tone == 53:
                self.__creat_note_node('h2', 'half', measure_element)
                current_length += 2
            elif tone == 54:
                self.__creat_note_node('h2', 'quarter', measure_element)
                current_length += 1
            elif tone == 55:
                self.__creat_note_node('h2', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 56:
                self.__creat_note_node('c3', 'full', measure_element)
                current_length += 4
            elif tone == 57:
                self.__creat_note_node('c3', 'half', measure_element)
                current_length += 2
            elif tone == 58:
                self.__creat_note_node('c3', 'quarter', measure_element)
                current_length += 1
            elif tone == 59:
                self.__creat_note_node('c3', 'eighth', measure_element)
                current_length += 0.5
            elif tone == 60:
                pass  # bar line
            else:
                print("Wrong tone element.")
                exit(1)

    """ Method generates output. """
    def generate(self):
        self.__root = minidom.Document()
        self.__xml = self.__root.createElement("variations")
        self.__root.appendChild(self.__xml)

        for variation in self.__variations:
            variation_element = self.__root.createElement("variation")
            self.__xml.appendChild(variation_element)
            self.__generate_measures(variation, variation_element)

        xml_str = self.__root.toprettyxml(indent="\t")
        print(xml_str)
        if self.__is_crossed:
            print("Some measures crossed time signature.")
