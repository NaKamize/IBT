from csgparser.DLL import *


class SCGparser:
    __T_C1_FULL = 0
    __T_C1_HALF = 1
    __T_C1_QUARTER = 2
    __T_D1_FULL = 3
    __T_D1_HALF = 4
    __T_D1_QUARTER = 5
    __T_E1_FULL = 6
    __T_E1_HALF = 7
    __T_E1_QUARTER = 8
    __T_F1_FULL = 9
    __T_F1_HALF = 10
    __T_F1_QUARTER = 11
    __T_G1_FULL = 12
    __T_G1_HALF = 13
    __T_G1_QUARTER = 14
    __T_A1_FULL = 15
    __T_A1_HALF = 16
    __T_A1_QUARTER = 17
    __T_H1_FULL = 18
    __T_H1_HALF = 19
    __T_H1_QUARTER = 20
    __T_C2_FULL = 21
    __T_C2_HALF = 22
    __T_C2_QUARTER = 23
    __T_END = 24

    __N_X = 25
    __N_S = 26

    __THEME_END = 27
    # C1F, C1H, C1Q, D1F, D1H, D1Q, E1F, E1H, E1Q, F1F, F1H, F1Q, G1F, G1H, G1Q, A1F, A1H, A1Q, H1F, H1H, H1Q, C2F, C2H, C2Q, |
    __table = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # S
        [{'rep': 1}, {'rep': 2}, {'rep': 3}, {'rep': 4}, {'rep': 5}, {'rep': 6}, {'rep': 7}, {'rep': 8}, {'rep': 9},
         {'rep': 10}, {'rep': 11},
         {'rep': 12}, {'rep': 13}, {'rep': 14}, {'rep': 15}, {'rep': 16}, {'rep': 17}, {'rep': 18}, {'rep': 19},
         {'rep': 20}, {'rep': 21},
         {'rep': 22}, {'rep': 23}, {'rep': 24}, {'rep': 25}]  # X
    ]

    __rules = [
        [__N_S, '->', (__N_X, __N_X)],
        [(__N_X, __N_X), '->', ((__T_C1_FULL, __N_X), (__T_C1_FULL, __N_X))],
        [(__N_X, __N_X), '->', ((__T_C1_HALF, __N_X), (__T_C1_HALF, __N_X))],
        [(__N_X, __N_X), '->', ((__T_C1_QUARTER, __N_X), (__T_C1_QUARTER, __N_X))],
        [(__N_X, __N_X), '->', ((__T_D1_FULL, __N_X), (__T_D1_FULL, __N_X))],
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_D1_HALF, __N_X))],
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_D1_QUARTER, __N_X))],
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_E1_FULL, __N_X))],
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_E1_HALF, __N_X))],
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_F1_FULL, __N_X))],
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_F1_HALF, __N_X))],
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_F1_QUARTER, __N_X))],
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_G1_FULL, __N_X))],
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_G1_HALF, __N_X))],
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_A1_FULL, __N_X))],
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_A1_HALF, __N_X))],
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_A1_QUARTER, __N_X))],
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_H1_FULL, __N_X))],
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_H1_HALF, __N_X))],
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_H1_QUARTER, __N_X))],
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_C2_FULL, __N_X))],
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_C2_HALF, __N_X))],
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],
        [(__N_X, __N_X), '->', (__T_END, __T_END)]
    ]

    __aux_array = []
    __aux_position = 0
    __position = 0
    __var_position = 0
    __rules_applied = []

    __res_variation = []

    def __init__(self, theme, variations):
        self.__theme = theme
        self.__variations = variations
        self.__dll = DLL()  # pushdown declaration as a doubly linked list

    def __lex_analysis(self):
        tokens = []
        for note in self.__theme:
            if note.get('c1'):
                if note.get('c1') == 'full':
                    tokens.append(self.__T_C1_FULL)
                elif note.get('c1') == 'half':
                    tokens.append(self.__T_C1_HALF)
                elif note.get('c1') == 'quarter':
                    tokens.append(self.__T_C1_QUARTER)
                else:
                    print("C1 token error.")
                    exit(1)
            elif note.get('d1'):
                if note.get('d1') == 'full':
                    tokens.append(self.__T_D1_FULL)
                elif note.get('d1') == 'half':
                    tokens.append(self.__T_D1_HALF)
                elif note.get('d1') == 'quarter':
                    tokens.append(self.__T_D1_QUARTER)
                else:
                    print("D1 token error.")
                    exit(1)
            elif note.get('e1'):
                if note.get('e1') == 'full':
                    tokens.append(self.__T_E1_FULL)
                elif note.get('e1') == 'half':
                    tokens.append(self.__T_E1_HALF)
                elif note.get('e1') == 'quarter':
                    tokens.append(self.__T_E1_QUARTER)
                else:
                    print("E1 token error.")
                    exit(1)
            elif note.get('f1'):
                if note.get('f1') == 'full':
                    tokens.append(self.__T_F1_FULL)
                elif note.get('f1') == 'half':
                    tokens.append(self.__T_F1_HALF)
                elif note.get('f1') == 'quarter':
                    tokens.append(self.__T_F1_QUARTER)
                else:
                    print("F1 token error.")
                    exit(1)
            elif note.get('g1'):
                if note.get('g1') == 'full':
                    tokens.append(self.__T_G1_FULL)
                elif note.get('g1') == 'half':
                    tokens.append(self.__T_G1_HALF)
                elif note.get('g1') == 'quarter':
                    tokens.append(self.__T_G1_QUARTER)
                else:
                    print("G1 token error.")
                    exit(1)
            elif note.get('a1'):
                if note.get('a1') == 'full':
                    tokens.append(self.__T_A1_FULL)
                elif note.get('a1') == 'half':
                    tokens.append(self.__T_A1_HALF)
                elif note.get('a1') == 'quarter':
                    tokens.append(self.__T_A1_QUARTER)
                else:
                    print("A1 token error.")
                    exit(1)
            elif note.get('h1'):
                if note.get('h1') == 'full':
                    tokens.append(self.__T_H1_FULL)
                elif note.get('h1') == 'half':
                    tokens.append(self.__T_H1_HALF)
                elif note.get('h1') == 'quarter':
                    tokens.append(self.__T_H1_QUARTER)
                else:
                    print("H1 token error.")
                    exit(1)
            elif note.get('c2'):
                if note.get('c2') == 'full':
                    tokens.append(self.__T_C2_FULL)
                elif note.get('c2') == 'half':
                    tokens.append(self.__T_C2_HALF)
                elif note.get('c2') == 'quarter':
                    tokens.append(self.__T_C2_QUARTER)
                else:
                    print("C2 token error.")
                    exit(1)
        tokens.append(self.__T_END)
        return tokens

    """ """

    def get_rule(self, input_s, stack_s):
        if stack_s == self.__N_S:
            return self.__table[0][input_s]
        elif stack_s == self.__N_X:
            return self.__table[1][input_s]
        else:
            print("Wrong stack symbol.")
            exit(1)

    def get_right_side(self, rule_number):
        print(rule_number)
        return self.__rules[rule_number][2]

    def reverse_push(self, items, deep, nonterminal):
        # reversing of tuples
        if type(items) != tuple:
            print(items)
            print(deep)
            print(nonterminal)
            result = self.__dll.insert(nonterminal, items)
            if items == self.__N_X:
                self.__aux_array.append(result)
        else:
            for item in items[::-1]:
                if not deep:
                    self.__dll.push(item)
                    # if it is nonterminal, then append it into aux array
                    if item == self.__N_X or item == self.__N_S and len(self.__aux_array) == 1:
                        self.__aux_array.append(self.__dll.head)
                else:
                    # receive inserted symbol and save it to aux array if it is nonterminal
                    result = self.__dll.insert(nonterminal, item)
                    if item == self.__N_X:
                        self.__aux_array.append(result)
        self.__dll.printList(self.__dll.head)

    def get_key(self, dictionary):
        for key in dictionary.keys():
            return key

    def get_rule_number(self, rule):
        return rule[self.get_key(rule)]

    def __save_result(self):
        variation = []
        node = self.__dll.head
        while node and node.data != self.__THEME_END:
            variation.append(node.data)
            self.__dll.pop()
            node = node.next
        self.__res_variation.append(variation)

    """ https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python 6 april """

    def syntax_analysis(self):
        print(self.__lex_analysis())
        print(self.__variations)
        variation_count = len(self.__variations) - 1
        """ Pushdown initialization """
        self.__dll.push(self.__THEME_END)
        self.__dll.push(self.__N_S)
        self.__aux_array.append(self.__dll.head)
        """ Getting tokens """
        tokens = self.__lex_analysis()
        while self.__dll.not_empty():
            cur_token = tokens[self.__position]  # get one token
            cur_varia = self.__variations[self.__var_position]  # get variation
            if self.__dll.head.data == self.__THEME_END:  # end of input sequence of tokens
                # if it is not empty and some variations are left
                if self.__dll.not_empty() and variation_count != self.__var_position:
                    print("Syntax analysis failed")
                    exit(1)
                else:  # every variation was successfully applied and stack is empty
                    self.__dll.pop()
                    print("OK")
                    self.__dll.printList(self.__dll.head)
            elif 0 <= self.__dll.head.data < 25:  # terminal
                if self.__dll.head.data == cur_token:
                    self.__dll.pop()
                    self.__position += 1
                else:
                    # end of variation
                    self.__save_result()
                    self.__var_position += 1
            elif 25 <= self.__dll.head.data < 27:  # nonterminal
                rule = self.get_rule(cur_token, self.__dll.head.data)  # find rule in LL table
                # if top of the pushdown and aux array item is same and rule is dictionary from LL table
                nonterminal = self.__aux_array[self.__aux_position]
                print(nonterminal)
                print(self.__dll.head)
                if nonterminal != self.__dll.head and type(rule) == dict:
                    # if rule in LL table is same variation as variation requested from user
                    if self.get_key(rule) == cur_varia:
                        try:
                            self.__aux_array.remove(nonterminal)
                        except:
                            print("Node is not in the array.")
                            exit(1)
                        # apply first part of the right side part of the rule on the pushdown top
                        self.reverse_push(self.get_right_side(self.get_rule_number(rule))[1], True, nonterminal)
                        self.__dll.remove(nonterminal)
                        self.__rules_applied.append(rule)
                    else:
                        print("Wrong variation.")
                        exit(1)
                # if top of the pushdown and aux array item is same and it is start symbol S
                elif nonterminal == self.__dll.head and type(rule) != dict:
                    popped = self.__dll.pop()
                    self.__aux_array.remove(popped)
                    self.reverse_push(self.get_right_side(rule), False, None)
                    self.__rules_applied.append(rule)
                elif nonterminal == self.__dll.head and type(rule) == dict:
                    popped = self.__dll.pop()
                    self.__aux_array.remove(popped)
                    self.reverse_push(self.get_right_side(self.get_rule_number(rule))[0], False, nonterminal)
            else:
                print("Auxiliarry array overflow.")
                exit(1)
        print(self.__rules_applied)
