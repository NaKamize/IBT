class SCGparser:
    __T_FULL = 0
    __T_HALF = 1
    __T_QUARTER = 2

    __T_C1 = 3
    __T_D1 = 4
    __T_E1 = 5
    __T_F1 = 6
    __T_G1 = 7
    __T_A1 = 8
    __T_H1 = 9
    __T_C2 = 10
    __T_D2 = 11
    __T_E2 = 12
    __T_F2 = 13
    __T_G2 = 14
    __T_A2 = 15
    __T_H2 = 16
    __T_C3 = 16
    __T_LEFT_BR = 17
    __T_RIGHT_BR = 18

    __N_SHARP = 19
    __N_S = 20

    def __init__(self, theme):
        self.__theme = theme

    def __lex_analysis(self):
        tokens = []
        for note in self.__theme:
            if note.get('c1'):
                tokens.append(self.__T_C1)
                if note.get('c1') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('c1') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('c1') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("C1 token error.")
                    exit(1)
            elif note.get('d1'):
                tokens.append(self.__T_D1)
                if note.get('d1') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('d1') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('d1') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("D1 token error.")
                    exit(1)
            elif note.get('e1'):
                tokens.append(self.__T_E1)
                if note.get('e1') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('e1') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('e1') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("E1 token error.")
                    exit(1)
            elif note.get('f1'):
                tokens.append(self.__T_F1)
                if note.get('f1') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('f1') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('f1') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("F1 token error.")
                    exit(1)
            elif note.get('g1'):
                tokens.append(self.__T_G1)
                if note.get('g1') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('g1') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('g1') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("G1 token error.")
                    exit(1)
            elif note.get('a1'):
                tokens.append(self.__T_A1)
                if note.get('a1') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('a1') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('a1') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("A1 token error.")
                    exit(1)
            elif note.get('h1'):
                tokens.append(self.__T_H1)
                if note.get('h1') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('h1') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('h1') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("H1 token error.")
                    exit(1)
            elif note.get('c2'):
                tokens.append(self.__T_C2)
                if note.get('c2') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('c2') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('c2') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("C2 token error.")
                    exit(1)
            elif note.get('d2'):
                tokens.append(self.__T_D2)
                if note.get('d2') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('d2') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('d2') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("D2 token error.")
                    exit(1)
            elif note.get('e2'):
                tokens.append(self.__T_E2)
                if note.get('e2') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('e2') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('e2') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("E2 token error.")
                    exit(1)
            elif note.get('f2'):
                tokens.append(self.__T_F2)
                if note.get('f2') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('f2') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('f2') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("F2 token error.")
                    exit(1)
            elif note.get('g2'):
                tokens.append(self.__T_G2)
                if note.get('g2') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('g2') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('g2') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("G2 token error.")
                    exit(1)
            elif note.get('a2'):
                tokens.append(self.__T_A2)
                if note.get('a2') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('a2') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('a2') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("A2 token error.")
                    exit(1)
            elif note.get('h2'):
                tokens.append(self.__T_H2)
                if note.get('h2') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('h2') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('h2') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("H2 token error.")
                    exit(1)
            elif note.get('c3'):
                tokens.append(self.__T_C3)
                if note.get('c3') == 'full':
                    tokens.append(self.__T_FULL)
                elif note.get('c3') == 'half':
                    tokens.append(self.__T_HALF)
                elif note.get('c3') == 'quarter':
                    tokens.append(self.__T_QUARTER)
                else:
                    print("C3 token error.")
                    exit(1)
        tokens.append('$')
        return tokens

    def syntax_analysis(self):
        print(self.__lex_analysis())
