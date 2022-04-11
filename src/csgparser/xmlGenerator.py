from xml.dom import minidom


class Generator:
    __root = None
    __xml = None

    def __init__(self, variations):
        self.__variations = variations

    def createToneNode(self, text, attrib, variationelement):
        toneElement = self.__root.createElement("tone")
        toneElement.setAttribute('note', attrib)
        variationelement.appendChild(toneElement)

        textnode = self.__root.createTextNode(text)
        toneElement.appendChild(textnode)

    def generate_measures(self, variation, variationelement):
        for tone in variation:
            if tone == 0:
                self.createToneNode('c1', 'full', variationelement)
            elif tone == 1:
                self.createToneNode('c1', 'half', variationelement)
            elif tone == 2:
                self.createToneNode('c1', 'quarter', variationelement)
            elif tone == 3:
                self.createToneNode('d1', 'full', variationelement)
            elif tone == 4:
                self.createToneNode('d1', 'half', variationelement)
            elif tone == 5:
                self.createToneNode('d1', 'quarter', variationelement)
            elif tone == 6:
                self.createToneNode('e1', 'full', variationelement)
            elif tone == 7:
                self.createToneNode('e1', 'half', variationelement)
            elif tone == 8:
                self.createToneNode('e1', 'quarter', variationelement)
            elif tone == 9:
                self.createToneNode('f1', 'full', variationelement)
            elif tone == 10:
                self.createToneNode('f1', 'half', variationelement)
            elif tone == 11:
                self.createToneNode('f1', 'quarter', variationelement)
            elif tone == 12:
                self.createToneNode('g1', 'full', variationelement)
            elif tone == 13:
                self.createToneNode('g1', 'half', variationelement)
            elif tone == 14:
                self.createToneNode('g1', 'quarter', variationelement)
            elif tone == 15:
                self.createToneNode('a1', 'full', variationelement)
            elif tone == 16:
                self.createToneNode('a1', 'half', variationelement)
            elif tone == 17:
                self.createToneNode('a1', 'quarter', variationelement)
            elif tone == 18:
                self.createToneNode('h1', 'full', variationelement)
            elif tone == 19:
                self.createToneNode('h1', 'half', variationelement)
            elif tone == 20:
                self.createToneNode('h1', 'quarter', variationelement)
            elif tone == 21:
                self.createToneNode('c2', 'full', variationelement)
            elif tone == 22:
                self.createToneNode('c2', 'half', variationelement)
            elif tone == 23:
                self.createToneNode('c2', 'quarter', variationelement)
            elif tone == 24:
                pass
            elif tone == 28:
                self.createToneNode('d2', 'full', variationelement)
            elif tone == 29:
                self.createToneNode('d2', 'half', variationelement)
            elif tone == 30:
                self.createToneNode('d2', 'quarter', variationelement)
            elif tone == 31:
                self.createToneNode('e2', 'full', variationelement)
            elif tone == 32:
                self.createToneNode('e2', 'half', variationelement)
            elif tone == 33:
                self.createToneNode('e2', 'quarter', variationelement)
            elif tone == 34:
                self.createToneNode('f2', 'full', variationelement)
            elif tone == 35:
                self.createToneNode('f2', 'half', variationelement)
            elif tone == 36:
                self.createToneNode('f2', 'quarter', variationelement)
            elif tone == 37:
                self.createToneNode('g2', 'full', variationelement)
            elif tone == 38:
                self.createToneNode('g2', 'half', variationelement)
            elif tone == 39:
                self.createToneNode('g2', 'quarter', variationelement)
            elif tone == 40:
                self.createToneNode('a2', 'full', variationelement)
            elif tone == 41:
                self.createToneNode('a2', 'half', variationelement)
            elif tone == 42:
                self.createToneNode('a2', 'quarter', variationelement)
            elif tone == 43:
                self.createToneNode('h2', 'full', variationelement)
            elif tone == 44:
                self.createToneNode('h2', 'half', variationelement)
            elif tone == 45:
                self.createToneNode('h2', 'quarter', variationelement)
            elif tone == 46:
                self.createToneNode('c3', 'full', variationelement)
            elif tone == 47:
                self.createToneNode('c3', 'half', variationelement)
            elif tone == 48:
                self.createToneNode('c3', 'quarter', variationelement)
            elif tone == 49:
                self.createToneNode('h', 'full', variationelement)
            elif tone == 50:
                self.createToneNode('h', 'half', variationelement)
            elif tone == 51:
                self.createToneNode('h', 'quarter', variationelement)
            else:
                print("Wrong tone element.")
                exit(1)

    
    def generate(self):
        self.__root = minidom.Document()
        self.__xml = self.__root.createElement("variations")
        self.__root.appendChild(self.__xml)

        for variation in self.__variations:
            variationElement = self.__root.createElement("variation")
            self.__xml.appendChild(variationElement)
            self.generate_measures(variation, variationElement)

        xml_str = self.__root.toprettyxml(indent="\t")
        print(xml_str)
