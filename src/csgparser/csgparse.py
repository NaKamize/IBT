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

    __T_D2_FULL = 28
    __T_D2_HALF = 29
    __T_D2_QUARTER = 30
    __T_E2_FULL = 31
    __T_E2_HALF = 32
    __T_E2_QUARTER = 33
    __T_F2_FULL = 34
    __T_F2_HALF = 35
    __T_F2_QUARTER = 36
    __T_G2_FULL = 37
    __T_G2_HALF = 38
    __T_G2_QUARTER = 39
    __T_A2_FULL = 40
    __T_A2_HALF = 41
    __T_A2_QUARTER = 42
    __T_H2_FULL = 43
    __T_H2_HALF = 44
    __T_H2_QUARTER = 45
    __T_C3_FULL = 46
    __T_C3_HALF = 47
    __T_C3_QUARTER = 48
    __T_H_FULL = 49
    __T_H_HALF = 50
    __T_H_QUARTER = 51

    __N_R = 52

    # C1F, C1H, C1Q, D1F, D1H, D1Q, E1F, E1H, E1Q, F1F, F1H, F1Q, G1F, G1H, G1Q, A1F, A1H, A1Q, H1F, H1H, H1Q, C2F, C2H, C2Q, |
    __table = [
        [{'else': 0, 'grad': 130}, {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130},
         {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130},
         {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130},
         {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130},
         {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130},
         {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130}, {'else': 0, 'grad': 130},
         {'else': 0, 'grad': 130}],  # S
        [{'rep': 1, 'aug': 1, 'trans': 42, 'seq+': 66, 'seq-': 90, 'dimi': 114},
         {'rep': 2, 'aug': 26, 'trans': 43, 'seq+': 67, 'seq-': 91, 'dimi': 115},
         {'rep': 3, 'aug': 27, 'trans': 44, 'seq+': 68, 'seq-': 92, 'dimi': 3},
         {'rep': 4, 'aug': 4, 'trans': 45, 'seq+': 69, 'seq-': 93, 'dimi': 116},
         {'rep': 5, 'aug': 28, 'trans': 46, 'seq+': 70, 'seq-': 94, 'dimi': 117},
         {'rep': 6, 'aug': 29, 'trans': 47, 'seq+': 71, 'seq-': 95, 'dimi': 6},
         {'rep': 7, 'aug': 7, 'trans': 48, 'seq+': 72, 'seq-': 96, 'dimi': 118},
         {'rep': 8, 'aug': 30, 'trans': 49, 'seq+': 73, 'seq-': 97, 'dimi': 119},
         {'rep': 9, 'aug': 31, 'trans': 50, 'seq+': 74, 'seq-': 98, 'dimi': 9},
         {'rep': 10, 'aug': 10, 'trans': 51, 'seq+': 75, 'seq-': 99, 'dimi': 120},
         {'rep': 11, 'aug': 32, 'trans': 52, 'seq+': 76, 'seq-': 100, 'dimi': 121},
         {'rep': 12, 'aug': 33, 'trans': 53, 'seq+': 77, 'seq-': 101, 'dimi': 12},
         {'rep': 13, 'aug': 13, 'trans': 54, 'seq+': 78, 'seq-': 102, 'dimi': 122},
         {'rep': 14, 'aug': 34, 'trans': 55, 'seq+': 79, 'seq-': 103, 'dimi': 123},
         {'rep': 15, 'aug': 35, 'trans': 56, 'seq+': 80, 'seq-': 104, 'dimi': 15},
         {'rep': 16, 'aug': 16, 'trans': 57, 'seq+': 81, 'seq-': 105, 'dimi': 124},
         {'rep': 17, 'aug': 36, 'trans': 58, 'seq+': 82, 'seq-': 106, 'dimi': 125},
         {'rep': 18, 'aug': 37, 'trans': 59, 'seq+': 83, 'seq-': 107, 'dimi': 18},
         {'rep': 19, 'aug': 19, 'trans': 60, 'seq+': 84, 'seq-': 108, 'dimi': 126},
         {'rep': 20, 'aug': 38, 'trans': 61, 'seq+': 85, 'seq-': 109, 'dimi': 127},
         {'rep': 21, 'aug': 39, 'trans': 62, 'seq+': 86, 'seq-': 110, 'dimi': 21},
         {'rep': 22, 'aug': 22, 'trans': 63, 'seq+': 87, 'seq-': 111, 'dimi': 128},
         {'rep': 23, 'aug': 40, 'trans': 64, 'seq+': 88, 'seq-': 112, 'dimi': 129},
         {'rep': 24, 'aug': 41, 'trans': 65, 'seq+': 89, 'seq-': 113, 'dimi': 24},
         {'rep': 25, 'aug': 25, 'trans': 25, 'seq+': 25, 'seq-': 25, 'dimi': 25}],  # X
        [{'grad': 131}, {'grad': 132}, {'grad': 133}, {'grad': 134}, {'grad': 135}, {'grad': 136}, {'grad': 137},
         {'grad': 138}, {'grad': 139}, {'grad': 140}, {'grad': 141}, {'grad': 142}, {'grad': 143}, {'grad': 144},
         {'grad': 145}, {'grad': 146}, {'grad': 147}, {'grad': 148}, {'grad': 149}, {'grad': 150}, {'grad': 151},
         {'grad': 152},
         {'grad': 153}, {'grad': 154}, {'grad': 155}]  # R
    ]

    __rules = [
        [__N_S, '->', (__N_X, __N_X)],  # 0
        [(__N_X, __N_X), '->', ((__T_C1_FULL, __N_X), (__T_C1_FULL, __N_X))],  # 1 # repetition start
        [(__N_X, __N_X), '->', ((__T_C1_HALF, __N_X), (__T_C1_HALF, __N_X))],  # 2
        [(__N_X, __N_X), '->', ((__T_C1_QUARTER, __N_X), (__T_C1_QUARTER, __N_X))],  # 3
        [(__N_X, __N_X), '->', ((__T_D1_FULL, __N_X), (__T_D1_FULL, __N_X))],  # 4
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_D1_HALF, __N_X))],  # 5
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_D1_QUARTER, __N_X))],  # 6
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_E1_FULL, __N_X))],  # 7
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_E1_HALF, __N_X))],  # 8
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],  # 9
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_F1_FULL, __N_X))],  # 10
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_F1_HALF, __N_X))],  # 11
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_F1_QUARTER, __N_X))],  # 12
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_G1_FULL, __N_X))],  # 13
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_G1_HALF, __N_X))],  # 14
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],  # 15
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_A1_FULL, __N_X))],  # 16
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_A1_HALF, __N_X))],  # 17
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_A1_QUARTER, __N_X))],  # 18
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_H1_FULL, __N_X))],  # 19
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_H1_HALF, __N_X))],  # 20
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_H1_QUARTER, __N_X))],  # 21
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 22
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 23
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 24
        [(__N_X, __N_X), '->', (__T_END, __T_END)],  # 25
        [(__N_X, __N_X), '->', ((__T_C1_HALF, __N_X), (__T_C1_FULL, __N_X))],  # 26 # augmentation start
        [(__N_X, __N_X), '->', ((__T_C1_QUARTER, __N_X), (__T_C1_HALF, __N_X))],  # 27
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_D1_FULL, __N_X))],  # 28
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_D1_HALF, __N_X))],  # 29
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_E1_FULL, __N_X))],  # 30
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_E1_HALF, __N_X))],  # 31
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_F1_FULL, __N_X))],  # 32
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_F1_HALF, __N_X))],  # 33
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_G1_FULL, __N_X))],  # 34
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_G1_HALF, __N_X))],  # 35
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_A1_FULL, __N_X))],  # 36
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_A1_HALF, __N_X))],  # 37
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_H1_FULL, __N_X))],  # 38
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_H1_HALF, __N_X))],  # 39
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_C2_FULL, __N_X))],  # 40
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_C2_HALF, __N_X))],  # 41
        [(__N_X, __N_X), '->', ((__T_C1_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 42 # transposition start
        [(__N_X, __N_X), '->', ((__T_C1_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 43
        [(__N_X, __N_X), '->', ((__T_C1_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 44
        [(__N_X, __N_X), '->', ((__T_D1_FULL, __N_X), (__T_D2_FULL, __N_X))],  # 45
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_D2_HALF, __N_X))],  # 46
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_D2_QUARTER, __N_X))],  # 47
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_E2_FULL, __N_X))],  # 48
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_E2_HALF, __N_X))],  # 49
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_E2_QUARTER, __N_X))],  # 50
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_F2_FULL, __N_X))],  # 51
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_F2_HALF, __N_X))],  # 52
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_F2_QUARTER, __N_X))],  # 53
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_G2_FULL, __N_X))],  # 54
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_G2_HALF, __N_X))],  # 55
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_G2_QUARTER, __N_X))],  # 56
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_A2_FULL, __N_X))],  # 57
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_A2_HALF, __N_X))],  # 58
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_A2_QUARTER, __N_X))],  # 59
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_H2_FULL, __N_X))],  # 60
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_H2_HALF, __N_X))],  # 61
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_H2_QUARTER, __N_X))],  # 62
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_C3_FULL, __N_X))],  # 63
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_C3_HALF, __N_X))],  # 64
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_C3_QUARTER, __N_X))],  # 65
        [(__N_X, __N_X), '->', ((__T_C1_FULL, __N_X), (__T_D1_FULL, __N_X))],  # 66 # sequence+ start
        [(__N_X, __N_X), '->', ((__T_C1_HALF, __N_X), (__T_D1_HALF, __N_X))],  # 67
        [(__N_X, __N_X), '->', ((__T_C1_QUARTER, __N_X), (__T_D1_QUARTER, __N_X))],  # 68
        [(__N_X, __N_X), '->', ((__T_D1_FULL, __N_X), (__T_E1_FULL, __N_X))],  # 69
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_E1_HALF, __N_X))],  # 70
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],  # 71
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_F1_FULL, __N_X))],  # 72
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_F1_HALF, __N_X))],  # 73
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_F1_QUARTER, __N_X))],  # 74
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_G1_FULL, __N_X))],  # 75
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_G1_HALF, __N_X))],  # 76
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],  # 77
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_A1_FULL, __N_X))],  # 78
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_A1_HALF, __N_X))],  # 79
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_A1_QUARTER, __N_X))],  # 80
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_H1_FULL, __N_X))],  # 81
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_H1_HALF, __N_X))],  # 82
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_H1_QUARTER, __N_X))],  # 83
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 84
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 85
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 86
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_D2_FULL, __N_X))],  # 87
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_D2_HALF, __N_X))],  # 88
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_D2_QUARTER, __N_X))],  # 89
        [(__N_X, __N_X), '->', ((__T_C1_FULL, __N_X), (__T_H_FULL, __N_X))],  # 90 # sequence- start
        [(__N_X, __N_X), '->', ((__T_C1_HALF, __N_X), (__T_H_HALF, __N_X))],  # 91
        [(__N_X, __N_X), '->', ((__T_C1_QUARTER, __N_X), (__T_H_QUARTER, __N_X))],  # 92
        [(__N_X, __N_X), '->', ((__T_D1_FULL, __N_X), (__T_C1_FULL, __N_X))],  # 93
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_C1_HALF, __N_X))],  # 94
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_C1_QUARTER, __N_X))],  # 95
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_D1_FULL, __N_X))],  # 96
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_D1_HALF, __N_X))],  # 97
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_D1_QUARTER, __N_X))],  # 98
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_E1_FULL, __N_X))],  # 99
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_E1_HALF, __N_X))],  # 100
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],  # 101
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_F1_FULL, __N_X))],  # 102
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_F1_HALF, __N_X))],  # 103
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_F1_QUARTER, __N_X))],  # 104
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_G1_FULL, __N_X))],  # 105
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_G1_HALF, __N_X))],  # 106
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],  # 107
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_A1_FULL, __N_X))],  # 108
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_A1_HALF, __N_X))],  # 109
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_A1_QUARTER, __N_X))],  # 110
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_H1_FULL, __N_X))],  # 111
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_H1_HALF, __N_X))],  # 112
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_H2_QUARTER, __N_X))],  # 113
        [(__N_X, __N_X), '->', ((__T_C1_FULL, __N_X), (__T_C1_HALF, __N_X))],  # 114 # diminution start
        [(__N_X, __N_X), '->', ((__T_C1_HALF, __N_X), (__T_C1_QUARTER, __N_X))],  # 115
        [(__N_X, __N_X), '->', ((__T_D1_FULL, __N_X), (__T_D1_HALF, __N_X))],  # 116
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_D1_QUARTER, __N_X))],  # 117
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_E1_HALF, __N_X))],  # 118
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_E1_QUARTER, __N_X))],  # 119
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_F1_HALF, __N_X))],  # 120
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_F1_QUARTER, __N_X))],  # 121
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_G1_HALF, __N_X))],  # 122
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_G1_QUARTER, __N_X))],  # 123
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_A1_HALF, __N_X))],  # 124
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_A1_QUARTER, __N_X))],  # 125
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_H1_HALF, __N_X))],  # 126
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_H1_QUARTER, __N_X))],  # 127
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_C2_HALF, __N_X))],  # 128
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_C2_QUARTER, __N_X))],  # 129
        [__N_S, '->', __N_R],  # 130
        [__N_R, '->', (__T_C1_FULL, __N_R, __T_C1_FULL)],  # 131
        [__N_R, '->', (__T_C1_HALF, __N_R, __T_C1_HALF)],  # 132
        [__N_R, '->', (__T_C1_QUARTER, __N_R, __T_C1_QUARTER)],  # 133
        [__N_R, '->', (__T_D1_FULL, __N_R, __T_D1_FULL)],  # 134
        [__N_R, '->', (__T_D1_HALF, __N_R, __T_D1_HALF)],  # 135
        [__N_R, '->', (__T_D1_QUARTER, __N_R, __T_D1_QUARTER)],  # 136
        [__N_R, '->', (__T_E1_FULL, __N_R, __T_E1_FULL)],  # 137
        [__N_R, '->', (__T_E1_HALF, __N_R, __T_E1_HALF)],  # 138
        [__N_R, '->', (__T_E1_QUARTER, __N_R, __T_E1_QUARTER)],  # 139
        [__N_R, '->', (__T_F1_FULL, __N_R, __T_F1_FULL)],  # 140
        [__N_R, '->', (__T_F1_HALF, __N_R, __T_F1_HALF)],  # 141
        [__N_R, '->', (__T_F1_QUARTER, __N_R, __T_F1_QUARTER)],  # 142
        [__N_R, '->', (__T_G1_FULL, __N_R, __T_G1_FULL)],  # 143
        [__N_R, '->', (__T_G1_HALF, __N_R, __T_G1_HALF)],  # 144
        [__N_R, '->', (__T_G1_QUARTER, __N_R, __T_G1_QUARTER)],  # 145
        [__N_R, '->', (__T_A1_FULL, __N_R, __T_A1_FULL)],  # 146
        [__N_R, '->', (__T_A1_HALF, __N_R, __T_A1_HALF)],  # 147
        [__N_R, '->', (__T_A1_QUARTER, __N_R, __T_A1_QUARTER)],  # 148
        [__N_R, '->', (__T_H1_FULL, __N_R, __T_H1_FULL)],  # 149
        [__N_R, '->', (__T_H1_HALF, __N_R, __T_H1_HALF)],  # 150
        [__N_R, '->', (__T_H1_QUARTER, __N_R, __T_H1_QUARTER)],  # 151
        [__N_R, '->', (__T_C2_FULL, __N_R, __T_C2_FULL)],  # 152
        [__N_R, '->', (__T_C2_HALF, __N_R, __T_C2_HALF)],  # 153
        [__N_R, '->', (__T_C2_QUARTER, __N_R, __T_C2_QUARTER)],  # 154
        [__N_R, '->', __T_END]  # 155
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
        tokens.append(self.__THEME_END)
        return tokens

    def __get_rule(self, input_s, stack_s):
        if stack_s == self.__N_S:
            return self.__table[0][input_s]
        elif stack_s == self.__N_X:
            return self.__table[1][input_s]
        elif stack_s == self.__N_R:
            return self.__table[2][input_s]
        else:
            print("Wrong stack symbol.")
            exit(1)

    def __get_right_side(self, rule_number):
        return self.__rules[rule_number][2]

    def __reverse_push(self, items, deep, nonterminal):
        # reversing of tuples
        if type(items) != tuple:
            # last step needs to be pushed not inserted
            if deep:
                result = self.__dll.insert(nonterminal, items)
            elif items != self.__N_R:  # condition to not put twice __N_R into stack after start symbol
                result = 0
                self.__dll.push(items)
            else:
                result = 0

            if items == self.__N_X and deep:
                self.__aux_array.append(result)
            # if it is retrogradation variation
            if items == self.__N_R:
                self.__dll.push(items)
                self.__aux_array.append(self.__dll.head)
        else:
            for item in items[::-1]:
                if not deep:
                    self.__dll.push(item)
                    # if it is nonterminal, then append it into aux array
                    if item == self.__N_X or item == self.__N_S and len(self.__aux_array) == 1:
                        self.__aux_array.append(self.__dll.head)
                    # v strede pravidla je neterminal R
                    if item == self.__N_R:
                        self.__aux_array.append(self.__dll.head)
                else:
                    # receive inserted symbol and save it to aux array if it is nonterminal
                    result = self.__dll.insert(nonterminal, item)
                    if item == self.__N_X:
                        self.__aux_array.append(result)

    def __get_key(self, dictionary, variation):
        # if variation exists in LL table, then return it, otherwise it is else
        for key in dictionary.keys():
            if variation == key:
                return key
        return 'else'

    def __get_rule_number(self, rule, variation):
        return rule[self.__get_key(rule, variation)]

    def __save_result(self):
        variation = []
        node = self.__dll.head
        while node and node.data != self.__THEME_END:
            variation.append(node.data)
            self.__dll.pop()
            node = node.next
        self.__res_variation.append(variation)

    def get_result(self):
        return self.__res_variation

    """ https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python 6 april """
    def __remove_extra_bline(self, variation_count):
        if self.__var_position - 2 == 0:  # only one variation, then pop bar line
            if self.__variations[self.__var_position - 2] != 'grad':
                self.__dll.pop()
        elif 0 <= self.__var_position - 1 <= variation_count:  # if there is more variations cut extra bar line
            if self.__variations[self.__var_position - 1] != 'grad':
                self.__dll.pop()

    def syntax_analysis(self):
        variation_count = len(self.__variations) - 1
        # Pushdown initialization
        self.__dll.push(self.__THEME_END)
        self.__dll.push(self.__N_S)
        # save nonterminal into aux array
        self.__aux_array.append(self.__dll.head)
        # receive tokens
        tokens = self.__lex_analysis()
        while self.__dll.not_empty():
            cur_token = tokens[self.__position]  # get token
            if self.__dll.head.data == self.__T_END:
                self.__var_position += 1
                if cur_token == self.__THEME_END and self.__var_position > variation_count:
                    # end of variation save result
                    self.__remove_extra_bline(variation_count)
                    self.__save_result()
                    self.__dll.pop()
                elif cur_token == self.__T_END and self.__var_position > variation_count:
                    # variation is coming to end, move to last symbol
                    self.__position += 1
                else:
                    # save result and set pointer to next variation
                    self.__remove_extra_bline(variation_count)
                    self.__save_result()
                    self.__aux_position = 0
                    self.__position = 0
                    self.__dll.push(self.__N_S)
                    self.__aux_array.append(self.__dll.head)
            elif 0 <= self.__dll.head.data < 25:  # terminal
                # if on the top of the pushdown is terminal pop it, and move position to next input symbol
                if self.__dll.head.data == cur_token:
                    self.__dll.pop()
                    self.__position += 1
                else:
                    print("Wrong stack symbol.")
                    exit(1)
            elif 25 <= self.__dll.head.data < 27 or self.__dll.head.data == self.__N_R:  # nonterminal
                rule = self.__get_rule(cur_token, self.__dll.head.data)  # find rule in LL table
                cur_varia = self.__variations[self.__var_position]  # get variation
                # if top of the pushdown and aux array item is same and rule is dictionary from LL table
                if self.__dll.head.data == self.__N_S:
                    non_terminal = self.__aux_array[0]
                    popped = self.__dll.pop()
                    self.__aux_array.remove(popped)
                    self.__reverse_push(self.__get_right_side(self.__get_rule_number(rule, cur_varia)), False, non_terminal)
                    self.__rules_applied.append(rule)
                else:
                    non_terminal = self.__aux_array[0]
                    popped = self.__dll.pop()  # get nonterminal from top of the pushdown
                    self.__aux_array.remove(popped)  # remove pointer form aux array
                    # get whole right-side of the rule
                    right_side = self.__get_right_side(self.__get_rule_number(rule, cur_varia))
                    if cur_varia != 'grad':
                        self.__reverse_push(right_side[0], False, non_terminal)  # push it in reverse on the top
                        deep_non_terminal = self.__aux_array[0]  # get second pointer to non-terminal
                        self.__aux_array.remove(deep_non_terminal)  # remove second pointer to non-terminal
                        self.__reverse_push(right_side[1], True, deep_non_terminal)  # deep rule push
                        self.__dll.remove(deep_non_terminal)  # remove second non-terminal from pushdown
                        self.__rules_applied.append(rule)  # save applied rule
                    else:
                        self.__reverse_push(right_side, False, non_terminal)
                    self.__dll.printList(self.__dll.head)
            else:
                print("Wrong symbol.")
                exit(1)
