from csgparser.DLL import *


class SCGparser:
    """ Terminals. """
    __T_C1_FULL = 0
    __T_C1_HALF = 1
    __T_C1_QUARTER = 2
    __T_C1_EIGHT = 3

    __T_D1_FULL = 4
    __T_D1_HALF = 5
    __T_D1_QUARTER = 6
    __T_D1_EIGHT = 7

    __T_E1_FULL = 8
    __T_E1_HALF = 9
    __T_E1_QUARTER = 10
    __T_E1_EIGHT = 11

    __T_F1_FULL = 12
    __T_F1_HALF = 13
    __T_F1_QUARTER = 14
    __T_F1_EIGHT = 15

    __T_G1_FULL = 16
    __T_G1_HALF = 17
    __T_G1_QUARTER = 18
    __T_G1_EIGHT = 19

    __T_A1_FULL = 20
    __T_A1_HALF = 21
    __T_A1_QUARTER = 22
    __T_A1_EIGHT = 23

    __T_H1_FULL = 24
    __T_H1_HALF = 25
    __T_H1_QUARTER = 26
    __T_H1_EIGHT = 27

    __T_C2_FULL = 28
    __T_C2_HALF = 29
    __T_C2_QUARTER = 30
    __T_C2_EIGHT = 31

    __T_D2_FULL = 32
    __T_D2_HALF = 33
    __T_D2_QUARTER = 34
    __T_D2_EIGHT = 35

    __T_E2_FULL = 36
    __T_E2_HALF = 37
    __T_E2_QUARTER = 38
    __T_E2_EIGHT = 39

    __T_F2_FULL = 40
    __T_F2_HALF = 41
    __T_F2_QUARTER = 42
    __T_F2_EIGHT = 43

    __T_G2_FULL = 44
    __T_G2_HALF = 45
    __T_G2_QUARTER = 46
    __T_G2_EIGHT = 47

    __T_A2_FULL = 48
    __T_A2_HALF = 49
    __T_A2_QUARTER = 50
    __T_A2_EIGHT = 51

    __T_H2_FULL = 52
    __T_H2_HALF = 53
    __T_H2_QUARTER = 54
    __T_H2_EIGHT = 55

    __T_C3_FULL = 56
    __T_C3_HALF = 57
    __T_C3_QUARTER = 58
    __T_C3_EIGHT = 59

    __T_END = 60

    """ Nonterminals """
    __N_X = 61
    __N_S = 62

    """ Last pushdown item """
    __THEME_END = 63

    """ Nonterminal from context-free part """
    __N_R = 64

    """ LL table """
    # C1F, C1H, C1Q, C1E, D1F, D1H, D1Q, D1E, E1F, E1H, E1Q, E1E, F1F, F1H, F1Q, F1E, G1F, G1H, G1Q, G1E, A1F, A1H, A1Q,
    # A1E, H1F, H1H, H1Q, H1E, C2F, C2H, C2Q, C2E, D2F, D2H, D2Q, D2E, E2F, E2H, E2Q, E2E, F2F, F2H, F2Q, F2E, G2F, G2H,
    # G2Q, G2E, A2F, A2H, A2Q, A2E, H2F, H2H, H2Q, H2E, C3F, C3H, C3Q, C3E, |
    __table = [
        [{'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687}, {'else': 0, 'grad': 687},
         {'else': 0, 'grad': 687}],  # S
        [{'rep': 1, 'aug': 1, 'trans': 151, 'seq+': 183, 'seq-': 1, 'dimi': 106, 'con': {0: 1}},
         {'rep': 2, 'aug': 61, 'trans': 152, 'seq+': 184, 'seq-': 2, 'dimi': 107, 'con': {0: 2}},
         {'rep': 3, 'aug': 62, 'trans': 153, 'seq+': 185, 'seq-': 3, 'dimi': 108, 'con': {0: 3}},
         {'rep': 4, 'aug': 63, 'trans': 154, 'seq+': 186, 'seq-': 4, 'dimi': 4, 'con': {0: 4}},
         {'rep': 5, 'aug': 5, 'trans': 155, 'seq+': 187, 'seq-': 239, 'dimi': 109, 'con': {0: 5, 1: 295, -1: 299}},
         {'rep': 6, 'aug': 64, 'trans': 156, 'seq+': 188, 'seq-': 240, 'dimi': 110, 'con': {0: 6, 1: 296, -1: 300}},
         {'rep': 7, 'aug': 65, 'trans': 157, 'seq+': 189, 'seq-': 241, 'dimi': 111, 'con': {0: 7, 1: 297, -1: 301}},
         {'rep': 8, 'aug': 66, 'trans': 158, 'seq+': 190, 'seq-': 242, 'dimi': 8, 'con': {0: 8, 1: 298, -1: 302}},
         {'rep': 9, 'aug': 9, 'trans': 159, 'seq+': 191, 'seq-': 243, 'dimi': 112,
          'con': {0: 9, 1: 303, 2: 307, -1: 311, -2: 315}},
         {'rep': 10, 'aug': 67, 'trans': 160, 'seq+': 192, 'seq-': 244, 'dimi': 113,
          'con': {0: 10, 1: 304, 2: 308, -1: 312, -2: 316}},
         {'rep': 11, 'aug': 68, 'trans': 161, 'seq+': 193, 'seq-': 245, 'dimi': 114,
          'con': {0: 11, 1: 305, 2: 309, -1: 313, -2: 317}},
         {'rep': 12, 'aug': 69, 'trans': 162, 'seq+': 194, 'seq-': 246, 'dimi': 12,
          'con': {0: 12, 1: 306, 2: 310, -1: 314, -2: 318}},
         {'rep': 13, 'aug': 13, 'trans': 163, 'seq+': 195, 'seq-': 247, 'dimi': 115,
          'con': {0: 13, 1: 319, 2: 323, 3: 327, -1: 331, -2: 335, -3: 339}},
         {'rep': 14, 'aug': 70, 'trans': 164, 'seq+': 196, 'seq-': 248, 'dimi': 116,
          'con': {0: 14, 1: 320, 2: 324, 3: 328, -1: 332, -2: 336, -3: 340}},
         {'rep': 15, 'aug': 71, 'trans': 165, 'seq+': 197, 'seq-': 249, 'dimi': 117,
          'con': {0: 15, 1: 321, 2: 325, 3: 329, -1: 333, -2: 337, -3: 341}},
         {'rep': 16, 'aug': 72, 'trans': 166, 'seq+': 198, 'seq-': 250, 'dimi': 16,
          'con': {0: 16, 1: 322, 2: 346, 3: 330, -1: 334, -2: 338, -3: 342}},
         {'rep': 17, 'aug': 17, 'trans': 167, 'seq+': 199, 'seq-': 251, 'dimi': 118,
          'con': {0: 17, 1: 343, 2: 347, 3: 351, 4: 355, -1: 359, -2: 363, -3: 367, -4: 371}},
         {'rep': 18, 'aug': 73, 'trans': 168, 'seq+': 200, 'seq-': 252, 'dimi': 119,
          'con': {0: 18, 1: 344, 2: 348, 3: 352, 4: 356, -1: 360, -2: 364, -3: 368, -4: 372}},
         {'rep': 19, 'aug': 74, 'trans': 169, 'seq+': 201, 'seq-': 253, 'dimi': 120,
          'con': {0: 19, 1: 345, 2: 349, 3: 353, 4: 357, -1: 361, -2: 365, -3: 369, -4: 373}},
         {'rep': 20, 'aug': 75, 'trans': 170, 'seq+': 202, 'seq-': 254, 'dimi': 20,
          'con': {0: 20, 1: 346, 2: 350, 3: 354, 4: 358, -1: 362, -2: 366, -3: 370, -4: 374}},
         {'rep': 21, 'aug': 21, 'trans': 171, 'seq+': 203, 'seq-': 255, 'dimi': 121,
          'con': {0: 21, 1: 375, 2: 379, 3: 383, 4: 387, 5: 391, -1: 395, -2: 399, -3: 403, -4: 407, -5: 411}},
         {'rep': 22, 'aug': 76, 'trans': 172, 'seq+': 204, 'seq-': 256, 'dimi': 122,
          'con': {0: 22, 1: 376, 2: 380, 3: 384, 4: 388, 5: 392, -1: 396, -2: 400, -3: 404, -4: 408, -5: 412}},
         {'rep': 23, 'aug': 77, 'trans': 173, 'seq+': 205, 'seq-': 257, 'dimi': 123,
          'con': {0: 23, 1: 377, 2: 381, 3: 385, 4: 389, 5: 393, -1: 397, -2: 401, -3: 405, -4: 409, -5: 413}},
         {'rep': 24, 'aug': 78, 'trans': 174, 'seq+': 206, 'seq-': 258, 'dimi': 24,
          'con': {0: 24, 1: 378, 2: 382, 3: 386, 4: 390, 5: 394, -1: 398, -2: 402, -3: 406, -4: 410, -5: 414}},
         {'rep': 25, 'aug': 25, 'trans': 175, 'seq+': 207, 'seq-': 259, 'dimi': 124,
          'con': {0: 25, 1: 415, 2: 419, 3: 423, 4: 427, 5: 431, 6: 435, -1: 439, -2: 443, -3: 447, -4: 451, -5: 455,
                  -6: 459}},
         {'rep': 26, 'aug': 79, 'trans': 176, 'seq+': 208, 'seq-': 260, 'dimi': 125,
          'con': {0: 26, 1: 416, 2: 420, 3: 424, 4: 428, 5: 432, 6: 436, -1: 440, -2: 444, -3: 448, -4: 452, -5: 456,
                  -6: 460}},
         {'rep': 27, 'aug': 80, 'trans': 177, 'seq+': 209, 'seq-': 261, 'dimi': 126,
          'con': {0: 27, 1: 417, 2: 421, 3: 425, 4: 429, 5: 433, 6: 437, -1: 441, -2: 445, -3: 449, -4: 453, -5: 457,
                  -6: 461}},
         {'rep': 28, 'aug': 81, 'trans': 178, 'seq+': 210, 'seq-': 262, 'dimi': 28,
          'con': {0: 28, 1: 418, 2: 422, 3: 426, 4: 430, 5: 434, 6: 438, -1: 442, -2: 446, -3: 450, -4: 454, -5: 458,
                  -6: 462}},
         {'rep': 29, 'aug': 29, 'trans': 179, 'seq+': 211, 'seq-': 263, 'dimi': 127,
          'con': {0: 29, 1: 463, 2: 467, 3: 471, 4: 475, 5: 479, 6: 483, 7: 487, -1: 491, -2: 495, -3: 499, -4: 503,
                  -5: 507, -6: 511, -7: 515}},
         {'rep': 30, 'aug': 82, 'trans': 180, 'seq+': 212, 'seq-': 264, 'dimi': 128,
          'con': {0: 30, 1: 464, 2: 468, 3: 472, 4: 476, 5: 480, 6: 484, 7: 488, -1: 492, -2: 496, -3: 500, -4: 504,
                  -5: 508, -6: 512, -7: 516}},
         {'rep': 31, 'aug': 83, 'trans': 181, 'seq+': 213, 'seq-': 265, 'dimi': 129,
          'con': {0: 31, 1: 465, 2: 469, 3: 473, 4: 477, 5: 481, 6: 485, 7: 489, -1: 493, -2: 497, -3: 501, -4: 505,
                  -5: 509, -6: 513, -7: 517}},
         {'rep': 32, 'aug': 84, 'trans': 182, 'seq+': 214, 'seq-': 266, 'dimi': 32,
          'con': {0: 32, 1: 466, 2: 470, 3: 474, 4: 478, 5: 482, 6: 486, 7: 490, -1: 494, -2: 498, -3: 502, -4: 506,
                  -5: 510, -6: 514, -7: 518}},
         {'rep': 33, 'aug': 33, 'trans': 33, 'seq+': 215, 'seq-': 267, 'dimi': 130,
          'con': {0: 33, 1: 543, 2: 547, 3: 551, 4: 555, 5: 559, 6: 563, -1: 519, -2: 523, -3: 527, -4: 531, -5: 535,
                  -6: 539}},
         {'rep': 34, 'aug': 85, 'trans': 34, 'seq+': 216, 'seq-': 268, 'dimi': 131,
          'con': {0: 34, 1: 544, 2: 548, 3: 552, 4: 556, 5: 560, 6: 564, -1: 520, -2: 524, -3: 528, -4: 532, -5: 536,
                  -6: 540}},
         {'rep': 35, 'aug': 86, 'trans': 35, 'seq+': 217, 'seq-': 269, 'dimi': 132,
          'con': {0: 35, 1: 545, 2: 549, 3: 553, 4: 557, 5: 561, 6: 565, -1: 521, -2: 525, -3: 529, -4: 533, -5: 537,
                  -6: 541}},
         {'rep': 36, 'aug': 87, 'trans': 36, 'seq+': 218, 'seq-': 270, 'dimi': 36,
          'con': {0: 36, 1: 546, 2: 550, 3: 554, 4: 558, 5: 562, 6: 566, -1: 522, -2: 526, -3: 530, -4: 534, -5: 538,
                  -6: 542}},
         {'rep': 37, 'aug': 37, 'trans': 37, 'seq+': 219, 'seq-': 271, 'dimi': 133,
          'con': {0: 37, 1: 587, 2: 591, 3: 595, 4: 599, 5: 603, -1: 567, -2: 571, -3: 575, -4: 579, -5: 583}},
         {'rep': 38, 'aug': 88, 'trans': 38, 'seq+': 220, 'seq-': 272, 'dimi': 134,
          'con': {0: 38, 1: 588, 2: 592, 3: 596, 4: 600, 5: 604, -1: 568, -2: 572, -3: 576, -4: 580, -5: 584}},
         {'rep': 39, 'aug': 89, 'trans': 39, 'seq+': 221, 'seq-': 273, 'dimi': 135,
          'con': {0: 39, 1: 589, 2: 593, 3: 597, 4: 601, 5: 605, -1: 569, -2: 573, -3: 577, -4: 581, -5: 585}},
         {'rep': 40, 'aug': 90, 'trans': 40, 'seq+': 222, 'seq-': 274, 'dimi': 40,
          'con': {0: 40, 1: 590, 2: 594, 3: 598, 4: 602, 5: 606, -1: 570, -2: 574, -3: 578, -4: 582, -5: 586}},
         {'rep': 41, 'aug': 41, 'trans': 41, 'seq+': 223, 'seq-': 275, 'dimi': 136,
          'con': {0: 41, 1: 623, 2: 627, 3: 631, 4: 635, -1: 607, -2: 611, -3: 615, -4: 619}},
         {'rep': 42, 'aug': 91, 'trans': 42, 'seq+': 224, 'seq-': 276, 'dimi': 137,
          'con': {0: 42, 1: 624, 2: 628, 3: 632, 4: 636, -1: 608, -2: 612, -3: 616, -4: 620}},
         {'rep': 43, 'aug': 92, 'trans': 43, 'seq+': 225, 'seq-': 277, 'dimi': 138,
          'con': {0: 43, 1: 625, 2: 629, 3: 633, 4: 637, -1: 609, -2: 613, -3: 617, -4: 621}},
         {'rep': 44, 'aug': 93, 'trans': 44, 'seq+': 226, 'seq-': 278, 'dimi': 44,
          'con': {0: 44, 1: 626, 2: 630, 3: 634, 4: 638, -1: 610, -2: 614, -3: 618, -4: 622}},
         {'rep': 45, 'aug': 45, 'trans': 45, 'seq+': 227, 'seq-': 279, 'dimi': 139,
          'con': {0: 45, 1: 651, 2: 655, 3: 659, -1: 639, -2: 643, -3: 647}},
         {'rep': 46, 'aug': 94, 'trans': 46, 'seq+': 228, 'seq-': 280, 'dimi': 140,
          'con': {0: 46, 1: 652, 2: 656, 3: 660, -1: 640, -2: 644, -3: 648}},
         {'rep': 47, 'aug': 95, 'trans': 47, 'seq+': 229, 'seq-': 281, 'dimi': 141,
          'con': {0: 47, 1: 653, 2: 657, 3: 661, -1: 641, -2: 645, -3: 649}},
         {'rep': 48, 'aug': 96, 'trans': 48, 'seq+': 230, 'seq-': 282, 'dimi': 48,
          'con': {0: 48, 1: 654, 2: 658, 3: 662, -1: 642, -2: 646, -3: 650}},
         {'rep': 49, 'aug': 49, 'trans': 49, 'seq+': 231, 'seq-': 283, 'dimi': 142,
          'con': {0: 49, 1: 671, 2: 675, -1: 663, -2: 667}},
         {'rep': 50, 'aug': 97, 'trans': 50, 'seq+': 232, 'seq-': 284, 'dimi': 143,
          'con': {0: 50, 1: 672, 2: 676, -1: 664, -2: 668}},
         {'rep': 51, 'aug': 98, 'trans': 51, 'seq+': 233, 'seq-': 285, 'dimi': 144,
          'con': {0: 51, 1: 673, 2: 677, -1: 665, -2: 669}},
         {'rep': 52, 'aug': 99, 'trans': 52, 'seq+': 234, 'seq-': 286, 'dimi': 52,
          'con': {0: 52, 1: 674, 2: 678, -1: 666, -2: 670}},
         {'rep': 53, 'aug': 53, 'trans': 53, 'seq+': 235, 'seq-': 287, 'dimi': 145, 'con': {0: 53, 1: 671, -1: 663}},
         {'rep': 54, 'aug': 100, 'trans': 54, 'seq+': 236, 'seq-': 288, 'dimi': 146, 'con': {0: 54, 1: 671, -1: 663}},
         {'rep': 55, 'aug': 101, 'trans': 55, 'seq+': 237, 'seq-': 289, 'dimi': 147, 'con': {0: 55, 1: 671, -1: 663}},
         {'rep': 56, 'aug': 102, 'trans': 56, 'seq+': 238, 'seq-': 290, 'dimi': 56, 'con': {0: 56, 1: 671, -1: 663}},
         {'rep': 57, 'aug': 57, 'trans': 57, 'seq+': 57, 'seq-': 291, 'dimi': 148, 'con': {0: 57}},
         {'rep': 58, 'aug': 103, 'trans': 58, 'seq+': 58, 'seq-': 292, 'dimi': 149, 'con': {0: 58}},
         {'rep': 59, 'aug': 104, 'trans': 59, 'seq+': 59, 'seq-': 293, 'dimi': 150, 'con': {0: 59}},
         {'rep': 60, 'aug': 105, 'trans': 60, 'seq+': 60, 'seq-': 294, 'dimi': 60, 'con': {0: 60}},
         {'rep': 749, 'aug': 749, 'trans': 749, 'seq+': 749, 'seq-': 749, 'dimi': 749, 'con': 749}],  # X
        [{'grad': 688}, {'grad': 689}, {'grad': 690}, {'grad': 691}, {'grad': 692}, {'grad': 693}, {'grad': 694},
         {'grad': 695}, {'grad': 696}, {'grad': 697}, {'grad': 698}, {'grad': 699}, {'grad': 700}, {'grad': 701},
         {'grad': 702}, {'grad': 703}, {'grad': 704}, {'grad': 705}, {'grad': 706}, {'grad': 707}, {'grad': 708},
         {'grad': 709}, {'grad': 710}, {'grad': 711}, {'grad': 712}, {'grad': 713}, {'grad': 714}, {'grad': 715},
         {'grad': 716}, {'grad': 717}, {'grad': 718}, {'grad': 719}, {'grad': 720}, {'grad': 721}, {'grad': 722},
         {'grad': 723}, {'grad': 724}, {'grad': 725}, {'grad': 726}, {'grad': 727}, {'grad': 728}, {'grad': 729},
         {'grad': 730}, {'grad': 731}, {'grad': 732}, {'grad': 733}, {'grad': 734}, {'grad': 735}, {'grad': 736},
         {'grad': 737}, {'grad': 738}, {'grad': 739}, {'grad': 740}, {'grad': 741}, {'grad': 742}, {'grad': 743},
         {'grad': 744}, {'grad': 745}, {'grad': 746}, {'grad': 747}, {'grad': 748}]  # R
    ]

    """ List of rules from scattered context grammar. """
    __rules = [
        [__N_S, '->', (__N_X, __N_X)],  # 0
        [(__N_X, __N_X), '->', ((__T_C1_FULL, __N_X), (__T_C1_FULL, __N_X))],  # 1 # repetition rule set
        [(__N_X, __N_X), '->', ((__T_C1_HALF, __N_X), (__T_C1_HALF, __N_X))],  # 2
        [(__N_X, __N_X), '->', ((__T_C1_QUARTER, __N_X), (__T_C1_QUARTER, __N_X))],  # 3
        [(__N_X, __N_X), '->', ((__T_C1_EIGHT, __N_X), (__T_C1_EIGHT, __N_X))],  # 4
        [(__N_X, __N_X), '->', ((__T_D1_FULL, __N_X), (__T_D1_FULL, __N_X))],  # 5
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_D1_HALF, __N_X))],  # 6
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_D1_QUARTER, __N_X))],  # 7
        [(__N_X, __N_X), '->', ((__T_D1_EIGHT, __N_X), (__T_D1_EIGHT, __N_X))],  # 8
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_E1_FULL, __N_X))],  # 9
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_E1_HALF, __N_X))],  # 10
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],  # 11
        [(__N_X, __N_X), '->', ((__T_E1_EIGHT, __N_X), (__T_E1_EIGHT, __N_X))],  # 12
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_F1_FULL, __N_X))],  # 13
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_F1_HALF, __N_X))],  # 14
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_F1_QUARTER, __N_X))],  # 15
        [(__N_X, __N_X), '->', ((__T_F1_EIGHT, __N_X), (__T_F1_EIGHT, __N_X))],  # 16
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_G1_FULL, __N_X))],  # 17
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_G1_HALF, __N_X))],  # 18
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],  # 19
        [(__N_X, __N_X), '->', ((__T_G1_EIGHT, __N_X), (__T_G1_EIGHT, __N_X))],  # 20
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_A1_FULL, __N_X))],  # 21
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_A1_HALF, __N_X))],  # 22
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_A1_QUARTER, __N_X))],  # 23
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_A1_EIGHT, __N_X))],  # 24
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_H1_FULL, __N_X))],  # 25
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_H1_HALF, __N_X))],  # 26
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_H1_QUARTER, __N_X))],  # 27
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_H1_EIGHT, __N_X))],  # 28
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 29
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 30
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 31
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_C2_EIGHT, __N_X))],  # 32
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_D2_FULL, __N_X))],  # 33
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_D2_HALF, __N_X))],  # 34
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_D2_QUARTER, __N_X))],  # 35
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_D2_EIGHT, __N_X))],  # 36
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_E2_FULL, __N_X))],  # 37
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_E2_HALF, __N_X))],  # 38
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_E2_QUARTER, __N_X))],  # 39
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_E2_EIGHT, __N_X))],  # 40
        [(__N_X, __N_X), '->', ((__T_F2_FULL, __N_X), (__T_F2_FULL, __N_X))],  # 41
        [(__N_X, __N_X), '->', ((__T_F2_HALF, __N_X), (__T_F2_HALF, __N_X))],  # 42
        [(__N_X, __N_X), '->', ((__T_F2_QUARTER, __N_X), (__T_F2_QUARTER, __N_X))],  # 43
        [(__N_X, __N_X), '->', ((__T_F2_EIGHT, __N_X), (__T_F2_EIGHT, __N_X))],  # 44
        [(__N_X, __N_X), '->', ((__T_G2_FULL, __N_X), (__T_G2_FULL, __N_X))],  # 45
        [(__N_X, __N_X), '->', ((__T_G2_HALF, __N_X), (__T_G2_HALF, __N_X))],  # 46
        [(__N_X, __N_X), '->', ((__T_G2_QUARTER, __N_X), (__T_G2_QUARTER, __N_X))],  # 47
        [(__N_X, __N_X), '->', ((__T_G2_EIGHT, __N_X), (__T_G2_EIGHT, __N_X))],  # 48
        [(__N_X, __N_X), '->', ((__T_A2_FULL, __N_X), (__T_A2_FULL, __N_X))],  # 49
        [(__N_X, __N_X), '->', ((__T_A2_HALF, __N_X), (__T_A2_HALF, __N_X))],  # 50
        [(__N_X, __N_X), '->', ((__T_A2_QUARTER, __N_X), (__T_A2_QUARTER, __N_X))],  # 51
        [(__N_X, __N_X), '->', ((__T_A2_EIGHT, __N_X), (__T_A2_EIGHT, __N_X))],  # 52
        [(__N_X, __N_X), '->', ((__T_H2_FULL, __N_X), (__T_H2_FULL, __N_X))],  # 53
        [(__N_X, __N_X), '->', ((__T_H2_HALF, __N_X), (__T_H2_HALF, __N_X))],  # 54
        [(__N_X, __N_X), '->', ((__T_H2_QUARTER, __N_X), (__T_H2_QUARTER, __N_X))],  # 55
        [(__N_X, __N_X), '->', ((__T_H2_EIGHT, __N_X), (__T_H2_EIGHT, __N_X))],  # 56
        [(__N_X, __N_X), '->', ((__T_C3_FULL, __N_X), (__T_C3_FULL, __N_X))],  # 57
        [(__N_X, __N_X), '->', ((__T_C3_HALF, __N_X), (__T_C3_HALF, __N_X))],  # 58
        [(__N_X, __N_X), '->', ((__T_C3_QUARTER, __N_X), (__T_C3_QUARTER, __N_X))],  # 59
        [(__N_X, __N_X), '->', ((__T_C3_EIGHT, __N_X), (__T_C3_EIGHT, __N_X))],  # 60
        [(__N_X, __N_X), '->', ((__T_C1_HALF, __N_X), (__T_C1_FULL, __N_X))],  # 61 # augmentation rule set
        [(__N_X, __N_X), '->', ((__T_C1_QUARTER, __N_X), (__T_C1_HALF, __N_X))],  # 62
        [(__N_X, __N_X), '->', ((__T_C1_EIGHT, __N_X), (__T_C1_QUARTER, __N_X))],  # 63
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_D1_FULL, __N_X))],  # 64
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_D1_HALF, __N_X))],  # 65
        [(__N_X, __N_X), '->', ((__T_D1_EIGHT, __N_X), (__T_D1_QUARTER, __N_X))],  # 66
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_E1_FULL, __N_X))],  # 67
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_E1_HALF, __N_X))],  # 68
        [(__N_X, __N_X), '->', ((__T_E1_EIGHT, __N_X), (__T_E1_QUARTER, __N_X))],  # 69
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_F1_FULL, __N_X))],  # 70
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_F1_HALF, __N_X))],  # 71
        [(__N_X, __N_X), '->', ((__T_F1_EIGHT, __N_X), (__T_F1_QUARTER, __N_X))],  # 72
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_G1_FULL, __N_X))],  # 73
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_G1_HALF, __N_X))],  # 74
        [(__N_X, __N_X), '->', ((__T_G1_EIGHT, __N_X), (__T_G1_QUARTER, __N_X))],  # 75
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_A1_FULL, __N_X))],  # 76
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_A1_HALF, __N_X))],  # 77
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_A1_QUARTER, __N_X))],  # 78
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_H1_FULL, __N_X))],  # 79
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_H1_HALF, __N_X))],  # 80
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_H1_QUARTER, __N_X))],  # 81
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_C2_FULL, __N_X))],  # 82
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_C2_HALF, __N_X))],  # 83
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_C2_QUARTER, __N_X))],  # 84
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_D2_FULL, __N_X))],  # 85
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_D2_HALF, __N_X))],  # 86
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_D2_QUARTER, __N_X))],  # 87
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_E2_FULL, __N_X))],  # 88
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_E2_HALF, __N_X))],  # 89
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_E2_QUARTER, __N_X))],  # 90
        [(__N_X, __N_X), '->', ((__T_F2_HALF, __N_X), (__T_F2_FULL, __N_X))],  # 91
        [(__N_X, __N_X), '->', ((__T_F2_QUARTER, __N_X), (__T_F2_HALF, __N_X))],  # 92
        [(__N_X, __N_X), '->', ((__T_F2_EIGHT, __N_X), (__T_F2_QUARTER, __N_X))],  # 93
        [(__N_X, __N_X), '->', ((__T_G2_HALF, __N_X), (__T_G2_FULL, __N_X))],  # 94
        [(__N_X, __N_X), '->', ((__T_G2_QUARTER, __N_X), (__T_G2_HALF, __N_X))],  # 95
        [(__N_X, __N_X), '->', ((__T_G2_EIGHT, __N_X), (__T_G2_QUARTER, __N_X))],  # 96
        [(__N_X, __N_X), '->', ((__T_A2_HALF, __N_X), (__T_A2_FULL, __N_X))],  # 97
        [(__N_X, __N_X), '->', ((__T_A2_QUARTER, __N_X), (__T_A2_HALF, __N_X))],  # 98
        [(__N_X, __N_X), '->', ((__T_A2_EIGHT, __N_X), (__T_A2_QUARTER, __N_X))],  # 99
        [(__N_X, __N_X), '->', ((__T_H2_HALF, __N_X), (__T_H2_FULL, __N_X))],  # 100
        [(__N_X, __N_X), '->', ((__T_H2_QUARTER, __N_X), (__T_H2_HALF, __N_X))],  # 101
        [(__N_X, __N_X), '->', ((__T_H2_EIGHT, __N_X), (__T_H2_QUARTER, __N_X))],  # 102
        [(__N_X, __N_X), '->', ((__T_C3_HALF, __N_X), (__T_C3_FULL, __N_X))],  # 103
        [(__N_X, __N_X), '->', ((__T_C3_QUARTER, __N_X), (__T_C3_HALF, __N_X))],  # 104
        [(__N_X, __N_X), '->', ((__T_C3_EIGHT, __N_X), (__T_C3_QUARTER, __N_X))],  # 105
        [(__N_X, __N_X), '->', ((__T_C1_FULL, __N_X), (__T_C1_HALF, __N_X))],  # 106 # diminution rule set
        [(__N_X, __N_X), '->', ((__T_C1_HALF, __N_X), (__T_C1_QUARTER, __N_X))],  # 107
        [(__N_X, __N_X), '->', ((__T_C1_QUARTER, __N_X), (__T_C1_EIGHT, __N_X))],  # 108
        [(__N_X, __N_X), '->', ((__T_D1_FULL, __N_X), (__T_D1_HALF, __N_X))],  # 109
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_D1_QUARTER, __N_X))],  # 110
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_D1_EIGHT, __N_X))],  # 111
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_E1_HALF, __N_X))],  # 112
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_E1_QUARTER, __N_X))],  # 113
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_E1_EIGHT, __N_X))],  # 114
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_F1_HALF, __N_X))],  # 115
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_F1_QUARTER, __N_X))],  # 116
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_F1_EIGHT, __N_X))],  # 117
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_G1_HALF, __N_X))],  # 118
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_G1_QUARTER, __N_X))],  # 119
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_G1_EIGHT, __N_X))],  # 120
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_A1_HALF, __N_X))],  # 121
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_A1_QUARTER, __N_X))],  # 122
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_A1_EIGHT, __N_X))],  # 123
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_H1_HALF, __N_X))],  # 124
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_H1_QUARTER, __N_X))],  # 125
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_H1_EIGHT, __N_X))],  # 126
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_C2_HALF, __N_X))],  # 127
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_C2_QUARTER, __N_X))],  # 128
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_C2_EIGHT, __N_X))],  # 129
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_D2_HALF, __N_X))],  # 130
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_D2_QUARTER, __N_X))],  # 131
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_D2_EIGHT, __N_X))],  # 132
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_E2_HALF, __N_X))],  # 133
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_E2_QUARTER, __N_X))],  # 134
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_E2_EIGHT, __N_X))],  # 135
        [(__N_X, __N_X), '->', ((__T_F2_FULL, __N_X), (__T_F2_HALF, __N_X))],  # 136
        [(__N_X, __N_X), '->', ((__T_F2_HALF, __N_X), (__T_F2_QUARTER, __N_X))],  # 137
        [(__N_X, __N_X), '->', ((__T_F2_QUARTER, __N_X), (__T_F2_EIGHT, __N_X))],  # 138
        [(__N_X, __N_X), '->', ((__T_G2_FULL, __N_X), (__T_G2_HALF, __N_X))],  # 139
        [(__N_X, __N_X), '->', ((__T_G2_HALF, __N_X), (__T_G2_QUARTER, __N_X))],  # 140
        [(__N_X, __N_X), '->', ((__T_G2_QUARTER, __N_X), (__T_G2_EIGHT, __N_X))],  # 141
        [(__N_X, __N_X), '->', ((__T_A2_FULL, __N_X), (__T_A2_HALF, __N_X))],  # 142
        [(__N_X, __N_X), '->', ((__T_A2_HALF, __N_X), (__T_A2_QUARTER, __N_X))],  # 143
        [(__N_X, __N_X), '->', ((__T_A2_QUARTER, __N_X), (__T_A2_EIGHT, __N_X))],  # 144
        [(__N_X, __N_X), '->', ((__T_H2_FULL, __N_X), (__T_H2_HALF, __N_X))],  # 145
        [(__N_X, __N_X), '->', ((__T_H2_HALF, __N_X), (__T_H2_QUARTER, __N_X))],  # 146
        [(__N_X, __N_X), '->', ((__T_H2_QUARTER, __N_X), (__T_H2_EIGHT, __N_X))],  # 147
        [(__N_X, __N_X), '->', ((__T_C3_FULL, __N_X), (__T_C3_HALF, __N_X))],  # 148
        [(__N_X, __N_X), '->', ((__T_C3_HALF, __N_X), (__T_C3_QUARTER, __N_X))],  # 149
        [(__N_X, __N_X), '->', ((__T_C3_QUARTER, __N_X), (__T_C3_EIGHT, __N_X))],  # 150
        [(__N_X, __N_X), '->', ((__T_C1_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 151 # transposition rule set
        [(__N_X, __N_X), '->', ((__T_C1_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 152
        [(__N_X, __N_X), '->', ((__T_C1_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 153
        [(__N_X, __N_X), '->', ((__T_C1_EIGHT, __N_X), (__T_C2_EIGHT, __N_X))],  # 154
        [(__N_X, __N_X), '->', ((__T_D1_FULL, __N_X), (__T_D2_FULL, __N_X))],  # 155
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_D2_HALF, __N_X))],  # 156
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_D2_QUARTER, __N_X))],  # 157
        [(__N_X, __N_X), '->', ((__T_D1_EIGHT, __N_X), (__T_D2_EIGHT, __N_X))],  # 158
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_E2_FULL, __N_X))],  # 159
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_E2_HALF, __N_X))],  # 160
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_E2_QUARTER, __N_X))],  # 161
        [(__N_X, __N_X), '->', ((__T_E1_EIGHT, __N_X), (__T_E2_EIGHT, __N_X))],  # 162
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_F2_FULL, __N_X))],  # 163
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_F2_HALF, __N_X))],  # 164
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_F2_QUARTER, __N_X))],  # 165
        [(__N_X, __N_X), '->', ((__T_F1_EIGHT, __N_X), (__T_F2_EIGHT, __N_X))],  # 166
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_G2_FULL, __N_X))],  # 167
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_G2_HALF, __N_X))],  # 168
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_G2_QUARTER, __N_X))],  # 169
        [(__N_X, __N_X), '->', ((__T_G1_EIGHT, __N_X), (__T_G2_EIGHT, __N_X))],  # 170
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_A2_FULL, __N_X))],  # 171
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_A2_HALF, __N_X))],  # 172
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_A2_QUARTER, __N_X))],  # 173
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_A2_EIGHT, __N_X))],  # 174
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_H2_FULL, __N_X))],  # 175
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_H2_HALF, __N_X))],  # 176
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_H2_QUARTER, __N_X))],  # 177
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_H2_EIGHT, __N_X))],  # 178
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_C3_FULL, __N_X))],  # 179
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_C3_HALF, __N_X))],  # 180
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_C3_QUARTER, __N_X))],  # 181
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_C3_EIGHT, __N_X))],  # 182
        [(__N_X, __N_X), '->', ((__T_C1_FULL, __N_X), (__T_D1_FULL, __N_X))],  # 183 # sequence+ rule set
        [(__N_X, __N_X), '->', ((__T_C1_HALF, __N_X), (__T_D1_HALF, __N_X))],  # 184
        [(__N_X, __N_X), '->', ((__T_C1_QUARTER, __N_X), (__T_D1_QUARTER, __N_X))],  # 185
        [(__N_X, __N_X), '->', ((__T_C1_EIGHT, __N_X), (__T_D1_EIGHT, __N_X))],  # 186
        [(__N_X, __N_X), '->', ((__T_D1_FULL, __N_X), (__T_E1_FULL, __N_X))],  # 187
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_E1_HALF, __N_X))],  # 188
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],  # 189
        [(__N_X, __N_X), '->', ((__T_D1_EIGHT, __N_X), (__T_E1_EIGHT, __N_X))],  # 190
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_F1_FULL, __N_X))],  # 191
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_F1_HALF, __N_X))],  # 192
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_F1_QUARTER, __N_X))],  # 193
        [(__N_X, __N_X), '->', ((__T_E1_EIGHT, __N_X), (__T_F1_EIGHT, __N_X))],  # 194
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_G1_FULL, __N_X))],  # 195
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_G1_HALF, __N_X))],  # 196
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],  # 197
        [(__N_X, __N_X), '->', ((__T_F1_EIGHT, __N_X), (__T_G1_EIGHT, __N_X))],  # 198
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_A1_FULL, __N_X))],  # 199
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_A1_HALF, __N_X))],  # 200
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_A1_QUARTER, __N_X))],  # 201
        [(__N_X, __N_X), '->', ((__T_G1_EIGHT, __N_X), (__T_A1_EIGHT, __N_X))],  # 202
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_H1_FULL, __N_X))],  # 203
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_H1_HALF, __N_X))],  # 204
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_H1_QUARTER, __N_X))],  # 205
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_H1_EIGHT, __N_X))],  # 206
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 207
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 208
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 209
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_C2_EIGHT, __N_X))],  # 210
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_D2_FULL, __N_X))],  # 211
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_D2_HALF, __N_X))],  # 212
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_D2_QUARTER, __N_X))],  # 213
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_D2_EIGHT, __N_X))],  # 214
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_E2_FULL, __N_X))],  # 215
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_E2_HALF, __N_X))],  # 216
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_E2_QUARTER, __N_X))],  # 217
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_E2_EIGHT, __N_X))],  # 218
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_F2_FULL, __N_X))],  # 219
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_F2_HALF, __N_X))],  # 220
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_F2_QUARTER, __N_X))],  # 221
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_F2_EIGHT, __N_X))],  # 222
        [(__N_X, __N_X), '->', ((__T_F2_FULL, __N_X), (__T_G2_FULL, __N_X))],  # 223
        [(__N_X, __N_X), '->', ((__T_F2_HALF, __N_X), (__T_G2_HALF, __N_X))],  # 224
        [(__N_X, __N_X), '->', ((__T_F2_QUARTER, __N_X), (__T_G2_QUARTER, __N_X))],  # 225
        [(__N_X, __N_X), '->', ((__T_F2_EIGHT, __N_X), (__T_G2_EIGHT, __N_X))],  # 226
        [(__N_X, __N_X), '->', ((__T_G2_FULL, __N_X), (__T_A2_FULL, __N_X))],  # 227
        [(__N_X, __N_X), '->', ((__T_G2_HALF, __N_X), (__T_A2_HALF, __N_X))],  # 228
        [(__N_X, __N_X), '->', ((__T_G2_QUARTER, __N_X), (__T_A2_QUARTER, __N_X))],  # 229
        [(__N_X, __N_X), '->', ((__T_G2_EIGHT, __N_X), (__T_A2_EIGHT, __N_X))],  # 230
        [(__N_X, __N_X), '->', ((__T_A2_FULL, __N_X), (__T_H2_FULL, __N_X))],  # 231
        [(__N_X, __N_X), '->', ((__T_A2_HALF, __N_X), (__T_H2_HALF, __N_X))],  # 232
        [(__N_X, __N_X), '->', ((__T_A2_QUARTER, __N_X), (__T_H2_QUARTER, __N_X))],  # 233
        [(__N_X, __N_X), '->', ((__T_A2_EIGHT, __N_X), (__T_H2_EIGHT, __N_X))],  # 234
        [(__N_X, __N_X), '->', ((__T_H2_FULL, __N_X), (__T_C3_FULL, __N_X))],  # 235
        [(__N_X, __N_X), '->', ((__T_H2_HALF, __N_X), (__T_C3_HALF, __N_X))],  # 236
        [(__N_X, __N_X), '->', ((__T_H2_QUARTER, __N_X), (__T_C3_QUARTER, __N_X))],  # 237
        [(__N_X, __N_X), '->', ((__T_H2_EIGHT, __N_X), (__T_C3_EIGHT, __N_X))],  # 238
        [(__N_X, __N_X), '->', ((__T_D1_FULL, __N_X), (__T_C1_FULL, __N_X))],  # 239 sequence - rule set
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_C1_HALF, __N_X))],  # 240
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_C1_QUARTER, __N_X))],  # 241
        [(__N_X, __N_X), '->', ((__T_D1_EIGHT, __N_X), (__T_C1_EIGHT, __N_X))],  # 242
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_D1_FULL, __N_X))],  # 243
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_D1_HALF, __N_X))],  # 244
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_D1_QUARTER, __N_X))],  # 245
        [(__N_X, __N_X), '->', ((__T_E1_EIGHT, __N_X), (__T_D1_EIGHT, __N_X))],  # 246
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_E1_FULL, __N_X))],  # 247
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_E1_HALF, __N_X))],  # 248
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],  # 249
        [(__N_X, __N_X), '->', ((__T_F1_EIGHT, __N_X), (__T_F1_EIGHT, __N_X))],  # 250
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_F1_FULL, __N_X))],  # 251
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_F1_HALF, __N_X))],  # 252
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_F1_QUARTER, __N_X))],  # 253
        [(__N_X, __N_X), '->', ((__T_G1_EIGHT, __N_X), (__T_F1_EIGHT, __N_X))],  # 254
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_G1_FULL, __N_X))],  # 255
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_G1_HALF, __N_X))],  # 256
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],  # 257
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_G1_EIGHT, __N_X))],  # 258
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_A1_FULL, __N_X))],  # 259
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_A1_HALF, __N_X))],  # 260
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_A1_QUARTER, __N_X))],  # 261
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_A1_EIGHT, __N_X))],  # 262
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_H1_FULL, __N_X))],  # 263
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_H1_HALF, __N_X))],  # 264
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_H2_QUARTER, __N_X))],  # 265
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_H2_EIGHT, __N_X))],  # 266
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 267
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 268
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 269
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_C2_EIGHT, __N_X))],  # 270
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_D2_FULL, __N_X))],  # 271
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_D2_HALF, __N_X))],  # 272
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_D2_QUARTER, __N_X))],  # 273
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_D2_EIGHT, __N_X))],  # 274
        [(__N_X, __N_X), '->', ((__T_F2_FULL, __N_X), (__T_E2_FULL, __N_X))],  # 275
        [(__N_X, __N_X), '->', ((__T_F2_HALF, __N_X), (__T_E2_HALF, __N_X))],  # 276
        [(__N_X, __N_X), '->', ((__T_F2_QUARTER, __N_X), (__T_E2_QUARTER, __N_X))],  # 277
        [(__N_X, __N_X), '->', ((__T_F2_EIGHT, __N_X), (__T_F2_EIGHT, __N_X))],  # 278
        [(__N_X, __N_X), '->', ((__T_G2_FULL, __N_X), (__T_F2_FULL, __N_X))],  # 279
        [(__N_X, __N_X), '->', ((__T_G2_HALF, __N_X), (__T_F2_HALF, __N_X))],  # 280
        [(__N_X, __N_X), '->', ((__T_G2_QUARTER, __N_X), (__T_F2_QUARTER, __N_X))],  # 281
        [(__N_X, __N_X), '->', ((__T_G2_EIGHT, __N_X), (__T_F2_EIGHT, __N_X))],  # 282
        [(__N_X, __N_X), '->', ((__T_A2_FULL, __N_X), (__T_G2_FULL, __N_X))],  # 283
        [(__N_X, __N_X), '->', ((__T_A2_HALF, __N_X), (__T_G2_HALF, __N_X))],  # 284
        [(__N_X, __N_X), '->', ((__T_A2_QUARTER, __N_X), (__T_G2_QUARTER, __N_X))],  # 285
        [(__N_X, __N_X), '->', ((__T_A2_EIGHT, __N_X), (__T_G2_EIGHT, __N_X))],  # 286
        [(__N_X, __N_X), '->', ((__T_H2_FULL, __N_X), (__T_A2_FULL, __N_X))],  # 287
        [(__N_X, __N_X), '->', ((__T_H2_HALF, __N_X), (__T_A2_HALF, __N_X))],  # 288
        [(__N_X, __N_X), '->', ((__T_H2_QUARTER, __N_X), (__T_A2_QUARTER, __N_X))],  # 289
        [(__N_X, __N_X), '->', ((__T_H2_EIGHT, __N_X), (__T_A2_EIGHT, __N_X))],  # 290
        [(__N_X, __N_X), '->', ((__T_C3_FULL, __N_X), (__T_H2_FULL, __N_X))],  # 291
        [(__N_X, __N_X), '->', ((__T_C3_HALF, __N_X), (__T_H2_HALF, __N_X))],  # 292
        [(__N_X, __N_X), '->', ((__T_C3_QUARTER, __N_X), (__T_H2_QUARTER, __N_X))],  # 293
        [(__N_X, __N_X), '->', ((__T_C3_EIGHT, __N_X), (__T_H2_EIGHT, __N_X))],  # 294
        [(__N_X, __N_X), '->', ((__T_D1_FULL, __N_X), (__T_E1_FULL, __N_X))],  # 295 contrary - rule set
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_E1_HALF, __N_X))],  # 296
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],  # 297
        [(__N_X, __N_X), '->', ((__T_D1_EIGHT, __N_X), (__T_E1_EIGHT, __N_X))],  # 298
        [(__N_X, __N_X), '->', ((__T_D1_FULL, __N_X), (__T_C1_FULL, __N_X))],  # 299
        [(__N_X, __N_X), '->', ((__T_D1_HALF, __N_X), (__T_C1_HALF, __N_X))],  # 300
        [(__N_X, __N_X), '->', ((__T_D1_QUARTER, __N_X), (__T_C1_QUARTER, __N_X))],  # 301
        [(__N_X, __N_X), '->', ((__T_D1_EIGHT, __N_X), (__T_C1_EIGHT, __N_X))],  # 302
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_F1_FULL, __N_X))],  # 303
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_F1_HALF, __N_X))],  # 304
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_F1_QUARTER, __N_X))],  # 305
        [(__N_X, __N_X), '->', ((__T_E1_EIGHT, __N_X), (__T_F1_EIGHT, __N_X))],  # 306
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_G1_FULL, __N_X))],  # 307
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_G1_HALF, __N_X))],  # 308
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],  # 309
        [(__N_X, __N_X), '->', ((__T_E1_EIGHT, __N_X), (__T_G1_EIGHT, __N_X))],  # 310
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_D1_FULL, __N_X))],  # 311
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_D1_HALF, __N_X))],  # 312
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_D1_QUARTER, __N_X))],  # 313
        [(__N_X, __N_X), '->', ((__T_E1_EIGHT, __N_X), (__T_D1_EIGHT, __N_X))],  # 314
        [(__N_X, __N_X), '->', ((__T_E1_FULL, __N_X), (__T_C1_FULL, __N_X))],  # 315
        [(__N_X, __N_X), '->', ((__T_E1_HALF, __N_X), (__T_C1_HALF, __N_X))],  # 316
        [(__N_X, __N_X), '->', ((__T_E1_QUARTER, __N_X), (__T_C1_QUARTER, __N_X))],  # 317
        [(__N_X, __N_X), '->', ((__T_E1_EIGHT, __N_X), (__T_C1_EIGHT, __N_X))],  # 318
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_G1_FULL, __N_X))],  # 319
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_G1_HALF, __N_X))],  # 320
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],  # 321
        [(__N_X, __N_X), '->', ((__T_F1_EIGHT, __N_X), (__T_G1_EIGHT, __N_X))],  # 322
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_A1_FULL, __N_X))],  # 323
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_A1_HALF, __N_X))],  # 324
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_A1_QUARTER, __N_X))],  # 325
        [(__N_X, __N_X), '->', ((__T_F1_EIGHT, __N_X), (__T_A1_EIGHT, __N_X))],  # 326
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_H1_FULL, __N_X))],  # 327
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_H1_HALF, __N_X))],  # 328
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_H1_QUARTER, __N_X))],  # 329
        [(__N_X, __N_X), '->', ((__T_F1_EIGHT, __N_X), (__T_H1_EIGHT, __N_X))],  # 330
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_E1_FULL, __N_X))],  # 331
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_E1_HALF, __N_X))],  # 332
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],  # 333
        [(__N_X, __N_X), '->', ((__T_F1_EIGHT, __N_X), (__T_E1_EIGHT, __N_X))],  # 334
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_D1_FULL, __N_X))],  # 335
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_D1_HALF, __N_X))],  # 336
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_D1_QUARTER, __N_X))],  # 337
        [(__N_X, __N_X), '->', ((__T_F1_EIGHT, __N_X), (__T_D1_EIGHT, __N_X))],  # 338
        [(__N_X, __N_X), '->', ((__T_F1_FULL, __N_X), (__T_C1_FULL, __N_X))],  # 339
        [(__N_X, __N_X), '->', ((__T_F1_HALF, __N_X), (__T_C1_HALF, __N_X))],  # 340
        [(__N_X, __N_X), '->', ((__T_F1_QUARTER, __N_X), (__T_C1_QUARTER, __N_X))],  # 341
        [(__N_X, __N_X), '->', ((__T_F1_EIGHT, __N_X), (__T_C1_EIGHT, __N_X))],  # 342
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_A1_FULL, __N_X))],  # 343
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_A1_HALF, __N_X))],  # 344
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_A1_QUARTER, __N_X))],  # 345
        [(__N_X, __N_X), '->', ((__T_G1_EIGHT, __N_X), (__T_A1_EIGHT, __N_X))],  # 346
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_H1_FULL, __N_X))],  # 347
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_H1_HALF, __N_X))],  # 348
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_H1_QUARTER, __N_X))],  # 349
        [(__N_X, __N_X), '->', ((__T_G1_EIGHT, __N_X), (__T_H1_EIGHT, __N_X))],  # 350
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 351
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 352
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 353
        [(__N_X, __N_X), '->', ((__T_G1_EIGHT, __N_X), (__T_C2_EIGHT, __N_X))],  # 354
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_D2_FULL, __N_X))],  # 355
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_D2_HALF, __N_X))],  # 356
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_D2_QUARTER, __N_X))],  # 357
        [(__N_X, __N_X), '->', ((__T_G1_EIGHT, __N_X), (__T_D2_EIGHT, __N_X))],  # 358
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_F1_FULL, __N_X))],  # 359
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_F1_HALF, __N_X))],  # 360
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_F1_QUARTER, __N_X))],  # 361
        [(__N_X, __N_X), '->', ((__T_G1_EIGHT, __N_X), (__T_F1_EIGHT, __N_X))],  # 362
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_E1_FULL, __N_X))],  # 363
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_E1_HALF, __N_X))],  # 364
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],  # 365
        [(__N_X, __N_X), '->', ((__T_G1_EIGHT, __N_X), (__T_E1_EIGHT, __N_X))],  # 366
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_D1_FULL, __N_X))],  # 367
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_D1_HALF, __N_X))],  # 368
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_D1_QUARTER, __N_X))],  # 369
        [(__N_X, __N_X), '->', ((__T_G1_EIGHT, __N_X), (__T_D1_EIGHT, __N_X))],  # 370
        [(__N_X, __N_X), '->', ((__T_G1_FULL, __N_X), (__T_C1_FULL, __N_X))],  # 371
        [(__N_X, __N_X), '->', ((__T_G1_HALF, __N_X), (__T_C1_HALF, __N_X))],  # 372
        [(__N_X, __N_X), '->', ((__T_G1_QUARTER, __N_X), (__T_C1_QUARTER, __N_X))],  # 373
        [(__N_X, __N_X), '->', ((__T_G1_EIGHT, __N_X), (__T_C1_EIGHT, __N_X))],  # 374
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_H1_FULL, __N_X))],  # 375
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_H1_HALF, __N_X))],  # 376
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_H1_QUARTER, __N_X))],  # 377
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_H1_EIGHT, __N_X))],  # 378
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 379
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 380
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 381
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_C2_EIGHT, __N_X))],  # 382
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_D2_FULL, __N_X))],  # 383
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_D2_HALF, __N_X))],  # 384
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_D2_QUARTER, __N_X))],  # 385
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_D2_EIGHT, __N_X))],  # 386
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_E2_FULL, __N_X))],  # 387
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_E2_HALF, __N_X))],  # 388
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_E2_QUARTER, __N_X))],  # 389
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_E2_EIGHT, __N_X))],  # 390
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_F2_FULL, __N_X))],  # 391
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_F2_HALF, __N_X))],  # 392
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_F2_QUARTER, __N_X))],  # 393
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_F2_EIGHT, __N_X))],  # 394
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_G1_FULL, __N_X))],  # 395
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_G1_HALF, __N_X))],  # 396
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],  # 397
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_G1_EIGHT, __N_X))],  # 398
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_F1_FULL, __N_X))],  # 399
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_F1_HALF, __N_X))],  # 400
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_F1_QUARTER, __N_X))],  # 401
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_F1_EIGHT, __N_X))],  # 402
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_E1_FULL, __N_X))],  # 403
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_E1_HALF, __N_X))],  # 404
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],  # 405
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_E1_EIGHT, __N_X))],  # 406
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_D1_FULL, __N_X))],  # 407
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_D1_HALF, __N_X))],  # 408
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_D1_QUARTER, __N_X))],  # 409
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_D1_EIGHT, __N_X))],  # 410
        [(__N_X, __N_X), '->', ((__T_A1_FULL, __N_X), (__T_C1_FULL, __N_X))],  # 411
        [(__N_X, __N_X), '->', ((__T_A1_HALF, __N_X), (__T_C1_HALF, __N_X))],  # 412
        [(__N_X, __N_X), '->', ((__T_A1_QUARTER, __N_X), (__T_C1_QUARTER, __N_X))],  # 413
        [(__N_X, __N_X), '->', ((__T_A1_EIGHT, __N_X), (__T_C1_EIGHT, __N_X))],  # 414
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 415
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 416
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 417
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_C2_EIGHT, __N_X))],  # 418
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_D2_FULL, __N_X))],  # 419
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_D2_HALF, __N_X))],  # 420
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_D2_QUARTER, __N_X))],  # 421
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_D2_EIGHT, __N_X))],  # 422
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_E2_FULL, __N_X))],  # 423
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_E2_HALF, __N_X))],  # 424
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_E2_QUARTER, __N_X))],  # 425
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_E2_EIGHT, __N_X))],  # 426
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_F2_FULL, __N_X))],  # 427
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_F2_HALF, __N_X))],  # 428
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_F2_QUARTER, __N_X))],  # 429
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_F2_EIGHT, __N_X))],  # 430
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_G2_FULL, __N_X))],  # 431
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_G2_HALF, __N_X))],  # 432
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_G2_QUARTER, __N_X))],  # 433
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_G2_EIGHT, __N_X))],  # 434
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_A2_FULL, __N_X))],  # 435
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_A2_HALF, __N_X))],  # 436
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_A2_QUARTER, __N_X))],  # 437
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_A2_EIGHT, __N_X))],  # 438
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_A1_FULL, __N_X))],  # 439
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_A1_HALF, __N_X))],  # 440
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_A1_QUARTER, __N_X))],  # 441
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_A1_EIGHT, __N_X))],  # 442
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_G1_FULL, __N_X))],  # 443
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_G1_HALF, __N_X))],  # 444
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],  # 445
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_G1_EIGHT, __N_X))],  # 446
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_F1_FULL, __N_X))],  # 447
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_F1_HALF, __N_X))],  # 448
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_F1_QUARTER, __N_X))],  # 449
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_F1_EIGHT, __N_X))],  # 450
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_E1_FULL, __N_X))],  # 451
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_E1_HALF, __N_X))],  # 452
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],  # 453
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_E1_EIGHT, __N_X))],  # 454
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_D1_FULL, __N_X))],  # 455
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_D1_HALF, __N_X))],  # 456
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_D1_QUARTER, __N_X))],  # 457
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_D1_EIGHT, __N_X))],  # 458
        [(__N_X, __N_X), '->', ((__T_H1_FULL, __N_X), (__T_C1_FULL, __N_X))],  # 459
        [(__N_X, __N_X), '->', ((__T_H1_HALF, __N_X), (__T_C1_HALF, __N_X))],  # 460
        [(__N_X, __N_X), '->', ((__T_H1_QUARTER, __N_X), (__T_C1_QUARTER, __N_X))],  # 461
        [(__N_X, __N_X), '->', ((__T_H1_EIGHT, __N_X), (__T_C1_EIGHT, __N_X))],  # 462
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_D2_FULL, __N_X))],  # 463
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_D2_HALF, __N_X))],  # 464
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_D2_QUARTER, __N_X))],  # 465
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_D2_EIGHT, __N_X))],  # 466
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_E2_FULL, __N_X))],  # 467
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_E2_HALF, __N_X))],  # 468
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_E2_QUARTER, __N_X))],  # 469
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_E2_EIGHT, __N_X))],  # 470
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_F2_FULL, __N_X))],  # 471
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_F2_HALF, __N_X))],  # 472
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_F2_QUARTER, __N_X))],  # 473
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_F2_EIGHT, __N_X))],  # 474
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_G2_FULL, __N_X))],  # 475
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_G2_HALF, __N_X))],  # 476
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_G2_QUARTER, __N_X))],  # 477
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_G2_EIGHT, __N_X))],  # 478
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_A2_FULL, __N_X))],  # 479
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_A2_HALF, __N_X))],  # 480
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_A2_QUARTER, __N_X))],  # 481
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_A2_EIGHT, __N_X))],  # 482
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_H2_FULL, __N_X))],  # 483
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_H2_HALF, __N_X))],  # 484
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_H2_QUARTER, __N_X))],  # 485
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_H2_EIGHT, __N_X))],  # 486
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_C3_FULL, __N_X))],  # 487
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_C3_HALF, __N_X))],  # 488
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_C3_QUARTER, __N_X))],  # 489
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_C3_EIGHT, __N_X))],  # 490
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_H1_FULL, __N_X))],  # 491
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_H1_HALF, __N_X))],  # 492
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_H1_QUARTER, __N_X))],  # 493
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_H1_EIGHT, __N_X))],  # 494
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_A1_FULL, __N_X))],  # 495
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_A1_HALF, __N_X))],  # 496
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_A1_QUARTER, __N_X))],  # 497
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_A1_EIGHT, __N_X))],  # 498
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_G1_FULL, __N_X))],  # 499
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_G1_HALF, __N_X))],  # 500
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],  # 501
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_G1_EIGHT, __N_X))],  # 502
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_F1_FULL, __N_X))],  # 503
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_F1_HALF, __N_X))],  # 504
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_F1_QUARTER, __N_X))],  # 505
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_F1_EIGHT, __N_X))],  # 506
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_E1_FULL, __N_X))],  # 507
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_E1_HALF, __N_X))],  # 508
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],  # 509
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_E1_EIGHT, __N_X))],  # 510
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_D1_FULL, __N_X))],  # 511
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_D1_HALF, __N_X))],  # 512
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_D1_QUARTER, __N_X))],  # 513
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_D1_EIGHT, __N_X))],  # 514
        [(__N_X, __N_X), '->', ((__T_C2_FULL, __N_X), (__T_C1_FULL, __N_X))],  # 515
        [(__N_X, __N_X), '->', ((__T_C2_HALF, __N_X), (__T_C1_HALF, __N_X))],  # 516
        [(__N_X, __N_X), '->', ((__T_C2_QUARTER, __N_X), (__T_C1_QUARTER, __N_X))],  # 517
        [(__N_X, __N_X), '->', ((__T_C2_EIGHT, __N_X), (__T_C1_EIGHT, __N_X))],  # 518
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 519
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 520
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 521
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_C2_EIGHT, __N_X))],  # 522
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_H1_FULL, __N_X))],  # 523
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_H1_HALF, __N_X))],  # 524
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_H1_QUARTER, __N_X))],  # 525
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_H1_EIGHT, __N_X))],  # 526
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_A1_FULL, __N_X))],  # 527
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_A1_HALF, __N_X))],  # 528
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_A1_QUARTER, __N_X))],  # 529
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_A1_EIGHT, __N_X))],  # 530
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_G1_FULL, __N_X))],  # 531
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_G1_HALF, __N_X))],  # 532
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],  # 533
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_G1_EIGHT, __N_X))],  # 534
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_F1_FULL, __N_X))],  # 535
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_F1_HALF, __N_X))],  # 536
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_F1_QUARTER, __N_X))],  # 537
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_F1_EIGHT, __N_X))],  # 538
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_E1_FULL, __N_X))],  # 539
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_E1_HALF, __N_X))],  # 540
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_E1_QUARTER, __N_X))],  # 541
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_E1_EIGHT, __N_X))],  # 542
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_E2_FULL, __N_X))],  # 543
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_E2_HALF, __N_X))],  # 544
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_E2_QUARTER, __N_X))],  # 545
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_E2_EIGHT, __N_X))],  # 546
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_F2_FULL, __N_X))],  # 547
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_F2_HALF, __N_X))],  # 548
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_F2_QUARTER, __N_X))],  # 549
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_F2_EIGHT, __N_X))],  # 550
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_G2_FULL, __N_X))],  # 551
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_G2_HALF, __N_X))],  # 552
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_G2_QUARTER, __N_X))],  # 553
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_G2_EIGHT, __N_X))],  # 554
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_A2_FULL, __N_X))],  # 555
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_A2_HALF, __N_X))],  # 556
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_A2_QUARTER, __N_X))],  # 557
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_A2_EIGHT, __N_X))],  # 558
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_H2_FULL, __N_X))],  # 559
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_H2_HALF, __N_X))],  # 560
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_H2_QUARTER, __N_X))],  # 561
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_H2_EIGHT, __N_X))],  # 562
        [(__N_X, __N_X), '->', ((__T_D2_FULL, __N_X), (__T_C3_FULL, __N_X))],  # 563
        [(__N_X, __N_X), '->', ((__T_D2_HALF, __N_X), (__T_C3_HALF, __N_X))],  # 564
        [(__N_X, __N_X), '->', ((__T_D2_QUARTER, __N_X), (__T_C3_QUARTER, __N_X))],  # 565
        [(__N_X, __N_X), '->', ((__T_D2_EIGHT, __N_X), (__T_C3_EIGHT, __N_X))],  # 566
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_D2_FULL, __N_X))],  # 567
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_D2_HALF, __N_X))],  # 568
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_D2_QUARTER, __N_X))],  # 569
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_D2_EIGHT, __N_X))],  # 570
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 571
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 572
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 573
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_C2_EIGHT, __N_X))],  # 574
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_H1_FULL, __N_X))],  # 575
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_H1_HALF, __N_X))],  # 576
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_H1_QUARTER, __N_X))],  # 577
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_H1_EIGHT, __N_X))],  # 578
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_A1_FULL, __N_X))],  # 579
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_A1_HALF, __N_X))],  # 580
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_A1_QUARTER, __N_X))],  # 581
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_A1_EIGHT, __N_X))],  # 582
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_G1_FULL, __N_X))],  # 583
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_G1_HALF, __N_X))],  # 584
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_G1_QUARTER, __N_X))],  # 585
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_G1_EIGHT, __N_X))],  # 586
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_F2_FULL, __N_X))],  # 587
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_F2_HALF, __N_X))],  # 588
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_F2_QUARTER, __N_X))],  # 589
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_F2_EIGHT, __N_X))],  # 590
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_G2_FULL, __N_X))],  # 591
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_G2_HALF, __N_X))],  # 592
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_G2_QUARTER, __N_X))],  # 593
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_G2_EIGHT, __N_X))],  # 594
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_A2_FULL, __N_X))],  # 595
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_A2_HALF, __N_X))],  # 596
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_A2_QUARTER, __N_X))],  # 597
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_A2_EIGHT, __N_X))],  # 598
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_H2_FULL, __N_X))],  # 599
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_H2_HALF, __N_X))],  # 600
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_H2_QUARTER, __N_X))],  # 601
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_H2_EIGHT, __N_X))],  # 602
        [(__N_X, __N_X), '->', ((__T_E2_FULL, __N_X), (__T_C3_FULL, __N_X))],  # 603
        [(__N_X, __N_X), '->', ((__T_E2_HALF, __N_X), (__T_C3_HALF, __N_X))],  # 604
        [(__N_X, __N_X), '->', ((__T_E2_QUARTER, __N_X), (__T_C3_QUARTER, __N_X))],  # 605
        [(__N_X, __N_X), '->', ((__T_E2_EIGHT, __N_X), (__T_C3_EIGHT, __N_X))],  # 606
        [(__N_X, __N_X), '->', ((__T_F2_FULL, __N_X), (__T_E2_FULL, __N_X))],  # 607
        [(__N_X, __N_X), '->', ((__T_F2_HALF, __N_X), (__T_E2_HALF, __N_X))],  # 608
        [(__N_X, __N_X), '->', ((__T_F2_QUARTER, __N_X), (__T_E2_QUARTER, __N_X))],  # 609
        [(__N_X, __N_X), '->', ((__T_F2_EIGHT, __N_X), (__T_E2_EIGHT, __N_X))],  # 610
        [(__N_X, __N_X), '->', ((__T_F2_FULL, __N_X), (__T_D2_FULL, __N_X))],  # 611
        [(__N_X, __N_X), '->', ((__T_F2_HALF, __N_X), (__T_D2_HALF, __N_X))],  # 612
        [(__N_X, __N_X), '->', ((__T_F2_QUARTER, __N_X), (__T_D2_QUARTER, __N_X))],  # 613
        [(__N_X, __N_X), '->', ((__T_F2_EIGHT, __N_X), (__T_D2_EIGHT, __N_X))],  # 614
        [(__N_X, __N_X), '->', ((__T_F2_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 615
        [(__N_X, __N_X), '->', ((__T_F2_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 616
        [(__N_X, __N_X), '->', ((__T_F2_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 617
        [(__N_X, __N_X), '->', ((__T_F2_EIGHT, __N_X), (__T_C2_EIGHT, __N_X))],  # 618
        [(__N_X, __N_X), '->', ((__T_F2_FULL, __N_X), (__T_H1_FULL, __N_X))],  # 619
        [(__N_X, __N_X), '->', ((__T_F2_HALF, __N_X), (__T_H1_HALF, __N_X))],  # 620
        [(__N_X, __N_X), '->', ((__T_F2_QUARTER, __N_X), (__T_H1_QUARTER, __N_X))],  # 621
        [(__N_X, __N_X), '->', ((__T_F2_EIGHT, __N_X), (__T_H1_EIGHT, __N_X))],  # 622
        [(__N_X, __N_X), '->', ((__T_F2_FULL, __N_X), (__T_G2_FULL, __N_X))],  # 623
        [(__N_X, __N_X), '->', ((__T_F2_HALF, __N_X), (__T_G2_HALF, __N_X))],  # 624
        [(__N_X, __N_X), '->', ((__T_F2_QUARTER, __N_X), (__T_G2_QUARTER, __N_X))],  # 625
        [(__N_X, __N_X), '->', ((__T_F2_EIGHT, __N_X), (__T_G2_EIGHT, __N_X))],  # 626
        [(__N_X, __N_X), '->', ((__T_F2_FULL, __N_X), (__T_A2_FULL, __N_X))],  # 627
        [(__N_X, __N_X), '->', ((__T_F2_HALF, __N_X), (__T_A2_HALF, __N_X))],  # 628
        [(__N_X, __N_X), '->', ((__T_F2_QUARTER, __N_X), (__T_A2_QUARTER, __N_X))],  # 629
        [(__N_X, __N_X), '->', ((__T_F2_EIGHT, __N_X), (__T_A2_EIGHT, __N_X))],  # 630
        [(__N_X, __N_X), '->', ((__T_F2_FULL, __N_X), (__T_H2_FULL, __N_X))],  # 631
        [(__N_X, __N_X), '->', ((__T_F2_HALF, __N_X), (__T_H2_HALF, __N_X))],  # 632
        [(__N_X, __N_X), '->', ((__T_F2_QUARTER, __N_X), (__T_H2_QUARTER, __N_X))],  # 633
        [(__N_X, __N_X), '->', ((__T_F2_EIGHT, __N_X), (__T_H2_EIGHT, __N_X))],  # 634
        [(__N_X, __N_X), '->', ((__T_F2_FULL, __N_X), (__T_C3_FULL, __N_X))],  # 635
        [(__N_X, __N_X), '->', ((__T_F2_HALF, __N_X), (__T_C3_HALF, __N_X))],  # 636
        [(__N_X, __N_X), '->', ((__T_F2_QUARTER, __N_X), (__T_C3_QUARTER, __N_X))],  # 637
        [(__N_X, __N_X), '->', ((__T_F2_EIGHT, __N_X), (__T_C3_EIGHT, __N_X))],  # 638
        [(__N_X, __N_X), '->', ((__T_G2_FULL, __N_X), (__T_F2_FULL, __N_X))],  # 639
        [(__N_X, __N_X), '->', ((__T_G2_HALF, __N_X), (__T_F2_HALF, __N_X))],  # 640
        [(__N_X, __N_X), '->', ((__T_G2_QUARTER, __N_X), (__T_F2_QUARTER, __N_X))],  # 641
        [(__N_X, __N_X), '->', ((__T_G2_EIGHT, __N_X), (__T_F2_EIGHT, __N_X))],  # 642
        [(__N_X, __N_X), '->', ((__T_G2_FULL, __N_X), (__T_E2_FULL, __N_X))],  # 643
        [(__N_X, __N_X), '->', ((__T_G2_HALF, __N_X), (__T_E2_HALF, __N_X))],  # 644
        [(__N_X, __N_X), '->', ((__T_G2_QUARTER, __N_X), (__T_E2_QUARTER, __N_X))],  # 645
        [(__N_X, __N_X), '->', ((__T_G2_EIGHT, __N_X), (__T_E2_EIGHT, __N_X))],  # 646
        [(__N_X, __N_X), '->', ((__T_G2_FULL, __N_X), (__T_D2_FULL, __N_X))],  # 647
        [(__N_X, __N_X), '->', ((__T_G2_HALF, __N_X), (__T_D2_HALF, __N_X))],  # 648
        [(__N_X, __N_X), '->', ((__T_G2_QUARTER, __N_X), (__T_D2_QUARTER, __N_X))],  # 649
        [(__N_X, __N_X), '->', ((__T_G2_EIGHT, __N_X), (__T_D2_EIGHT, __N_X))],  # 650
        [(__N_X, __N_X), '->', ((__T_G2_FULL, __N_X), (__T_A2_FULL, __N_X))],  # 651
        [(__N_X, __N_X), '->', ((__T_G2_HALF, __N_X), (__T_A2_HALF, __N_X))],  # 652
        [(__N_X, __N_X), '->', ((__T_G2_QUARTER, __N_X), (__T_A2_QUARTER, __N_X))],  # 653
        [(__N_X, __N_X), '->', ((__T_G2_EIGHT, __N_X), (__T_A2_EIGHT, __N_X))],  # 654
        [(__N_X, __N_X), '->', ((__T_G2_FULL, __N_X), (__T_H2_FULL, __N_X))],  # 655
        [(__N_X, __N_X), '->', ((__T_G2_HALF, __N_X), (__T_H2_HALF, __N_X))],  # 656
        [(__N_X, __N_X), '->', ((__T_G2_QUARTER, __N_X), (__T_H2_QUARTER, __N_X))],  # 657
        [(__N_X, __N_X), '->', ((__T_G2_EIGHT, __N_X), (__T_H2_EIGHT, __N_X))],  # 658
        [(__N_X, __N_X), '->', ((__T_G2_FULL, __N_X), (__T_C3_FULL, __N_X))],  # 659
        [(__N_X, __N_X), '->', ((__T_G2_HALF, __N_X), (__T_C3_HALF, __N_X))],  # 660
        [(__N_X, __N_X), '->', ((__T_G2_QUARTER, __N_X), (__T_C3_QUARTER, __N_X))],  # 661
        [(__N_X, __N_X), '->', ((__T_G2_EIGHT, __N_X), (__T_C3_EIGHT, __N_X))],  # 662
        [(__N_X, __N_X), '->', ((__T_A2_FULL, __N_X), (__T_G2_FULL, __N_X))],  # 663
        [(__N_X, __N_X), '->', ((__T_A2_HALF, __N_X), (__T_G2_HALF, __N_X))],  # 664
        [(__N_X, __N_X), '->', ((__T_A2_QUARTER, __N_X), (__T_G2_QUARTER, __N_X))],  # 665
        [(__N_X, __N_X), '->', ((__T_A2_EIGHT, __N_X), (__T_G2_EIGHT, __N_X))],  # 666
        [(__N_X, __N_X), '->', ((__T_A2_FULL, __N_X), (__T_F2_FULL, __N_X))],  # 667
        [(__N_X, __N_X), '->', ((__T_A2_HALF, __N_X), (__T_F2_HALF, __N_X))],  # 668
        [(__N_X, __N_X), '->', ((__T_A2_QUARTER, __N_X), (__T_F2_QUARTER, __N_X))],  # 669
        [(__N_X, __N_X), '->', ((__T_A2_EIGHT, __N_X), (__T_F2_EIGHT, __N_X))],  # 670
        [(__N_X, __N_X), '->', ((__T_A2_FULL, __N_X), (__T_H2_FULL, __N_X))],  # 671
        [(__N_X, __N_X), '->', ((__T_A2_HALF, __N_X), (__T_H2_HALF, __N_X))],  # 672
        [(__N_X, __N_X), '->', ((__T_A2_QUARTER, __N_X), (__T_H2_QUARTER, __N_X))],  # 673
        [(__N_X, __N_X), '->', ((__T_A2_EIGHT, __N_X), (__T_H2_EIGHT, __N_X))],  # 674
        [(__N_X, __N_X), '->', ((__T_A2_FULL, __N_X), (__T_C2_FULL, __N_X))],  # 675
        [(__N_X, __N_X), '->', ((__T_A2_HALF, __N_X), (__T_C2_HALF, __N_X))],  # 676
        [(__N_X, __N_X), '->', ((__T_A2_QUARTER, __N_X), (__T_C2_QUARTER, __N_X))],  # 677
        [(__N_X, __N_X), '->', ((__T_A2_EIGHT, __N_X), (__T_C2_EIGHT, __N_X))],  # 678
        [(__N_X, __N_X), '->', ((__T_H2_FULL, __N_X), (__T_A2_FULL, __N_X))],  # 679
        [(__N_X, __N_X), '->', ((__T_H2_HALF, __N_X), (__T_A2_HALF, __N_X))],  # 608
        [(__N_X, __N_X), '->', ((__T_H2_QUARTER, __N_X), (__T_A2_QUARTER, __N_X))],  # 681
        [(__N_X, __N_X), '->', ((__T_H2_EIGHT, __N_X), (__T_A2_EIGHT, __N_X))],  # 682
        [(__N_X, __N_X), '->', ((__T_H2_FULL, __N_X), (__T_C3_FULL, __N_X))],  # 683
        [(__N_X, __N_X), '->', ((__T_H2_HALF, __N_X), (__T_C3_HALF, __N_X))],  # 684
        [(__N_X, __N_X), '->', ((__T_H2_QUARTER, __N_X), (__T_C3_QUARTER, __N_X))],  # 685
        [(__N_X, __N_X), '->', ((__T_H2_EIGHT, __N_X), (__T_C3_EIGHT, __N_X))],  # 686
        [__N_S, '->', __N_R],  # 687
        [__N_R, '->', (__T_C1_FULL, __N_R, __T_C1_FULL)],  # 688
        [__N_R, '->', (__T_C1_HALF, __N_R, __T_C1_HALF)],  # 689
        [__N_R, '->', (__T_C1_QUARTER, __N_R, __T_C1_QUARTER)],  # 690
        [__N_R, '->', (__T_C1_EIGHT, __N_R, __T_C1_EIGHT)],  # 691
        [__N_R, '->', (__T_D1_FULL, __N_R, __T_D1_FULL)],  # 692
        [__N_R, '->', (__T_D1_HALF, __N_R, __T_D1_HALF)],  # 693
        [__N_R, '->', (__T_D1_QUARTER, __N_R, __T_D1_QUARTER)],  # 694
        [__N_R, '->', (__T_D1_EIGHT, __N_R, __T_D1_EIGHT)],  # 695
        [__N_R, '->', (__T_E1_FULL, __N_R, __T_E1_FULL)],  # 696
        [__N_R, '->', (__T_E1_HALF, __N_R, __T_E1_HALF)],  # 697
        [__N_R, '->', (__T_E1_QUARTER, __N_R, __T_E1_QUARTER)],  # 698
        [__N_R, '->', (__T_E1_EIGHT, __N_R, __T_E1_EIGHT)],  # 699
        [__N_R, '->', (__T_F1_FULL, __N_R, __T_F1_FULL)],  # 700
        [__N_R, '->', (__T_F1_HALF, __N_R, __T_F1_HALF)],  # 701
        [__N_R, '->', (__T_F1_QUARTER, __N_R, __T_F1_QUARTER)],  # 702
        [__N_R, '->', (__T_F1_EIGHT, __N_R, __T_F1_EIGHT)],  # 703
        [__N_R, '->', (__T_G1_FULL, __N_R, __T_G1_FULL)],  # 704
        [__N_R, '->', (__T_G1_HALF, __N_R, __T_G1_HALF)],  # 705
        [__N_R, '->', (__T_G1_QUARTER, __N_R, __T_G1_QUARTER)],  # 706
        [__N_R, '->', (__T_G1_EIGHT, __N_R, __T_G1_EIGHT)],  # 707
        [__N_R, '->', (__T_A1_FULL, __N_R, __T_A1_FULL)],  # 708
        [__N_R, '->', (__T_A1_HALF, __N_R, __T_A1_HALF)],  # 709
        [__N_R, '->', (__T_A1_QUARTER, __N_R, __T_A1_QUARTER)],  # 710
        [__N_R, '->', (__T_A1_EIGHT, __N_R, __T_A1_EIGHT)],  # 711
        [__N_R, '->', (__T_H1_FULL, __N_R, __T_H1_FULL)],  # 712
        [__N_R, '->', (__T_H1_HALF, __N_R, __T_H1_HALF)],  # 713
        [__N_R, '->', (__T_H1_QUARTER, __N_R, __T_H1_QUARTER)],  # 714
        [__N_R, '->', (__T_H1_EIGHT, __N_R, __T_H1_EIGHT)],  # 715
        [__N_R, '->', (__T_C2_FULL, __N_R, __T_C2_FULL)],  # 716
        [__N_R, '->', (__T_C2_HALF, __N_R, __T_C2_HALF)],  # 717
        [__N_R, '->', (__T_C2_QUARTER, __N_R, __T_C2_QUARTER)],  # 718
        [__N_R, '->', (__T_C2_EIGHT, __N_R, __T_C2_EIGHT)],  # 719
        [__N_R, '->', (__T_D2_FULL, __N_R, __T_D2_FULL)],  # 720
        [__N_R, '->', (__T_D2_HALF, __N_R, __T_D2_HALF)],  # 721
        [__N_R, '->', (__T_D2_QUARTER, __N_R, __T_D2_QUARTER)],  # 722
        [__N_R, '->', (__T_D2_EIGHT, __N_R, __T_D2_EIGHT)],  # 723
        [__N_R, '->', (__T_E2_FULL, __N_R, __T_E2_FULL)],  # 724
        [__N_R, '->', (__T_E2_HALF, __N_R, __T_E2_HALF)],  # 725
        [__N_R, '->', (__T_E2_QUARTER, __N_R, __T_E2_QUARTER)],  # 726
        [__N_R, '->', (__T_E2_EIGHT, __N_R, __T_E2_EIGHT)],  # 727
        [__N_R, '->', (__T_F2_FULL, __N_R, __T_F2_FULL)],  # 728
        [__N_R, '->', (__T_F2_HALF, __N_R, __T_F2_HALF)],  # 729
        [__N_R, '->', (__T_F2_QUARTER, __N_R, __T_F2_QUARTER)],  # 730
        [__N_R, '->', (__T_F2_EIGHT, __N_R, __T_F2_EIGHT)],  # 731
        [__N_R, '->', (__T_G2_FULL, __N_R, __T_G2_FULL)],  # 732
        [__N_R, '->', (__T_G2_HALF, __N_R, __T_G2_HALF)],  # 733
        [__N_R, '->', (__T_G2_QUARTER, __N_R, __T_G2_QUARTER)],  # 734
        [__N_R, '->', (__T_G2_EIGHT, __N_R, __T_G2_EIGHT)],  # 735
        [__N_R, '->', (__T_A2_FULL, __N_R, __T_A2_FULL)],  # 736
        [__N_R, '->', (__T_A2_HALF, __N_R, __T_A2_HALF)],  # 737
        [__N_R, '->', (__T_A2_QUARTER, __N_R, __T_A2_QUARTER)],  # 738
        [__N_R, '->', (__T_A2_EIGHT, __N_R, __T_A2_EIGHT)],  # 739
        [__N_R, '->', (__T_H2_FULL, __N_R, __T_H2_FULL)],  # 740
        [__N_R, '->', (__T_H2_HALF, __N_R, __T_H2_HALF)],  # 741
        [__N_R, '->', (__T_H2_QUARTER, __N_R, __T_H2_QUARTER)],  # 742
        [__N_R, '->', (__T_H2_EIGHT, __N_R, __T_H2_EIGHT)],  # 743
        [__N_R, '->', (__T_C3_FULL, __N_R, __T_C3_FULL)],  # 744
        [__N_R, '->', (__T_C3_HALF, __N_R, __T_C3_HALF)],  # 745
        [__N_R, '->', (__T_C3_QUARTER, __N_R, __T_C3_QUARTER)],  # 746
        [__N_R, '->', (__T_C3_EIGHT, __N_R, __T_C3_EIGHT)],  # 747
        [__N_R, '->', __T_END],  # 748
        [(__N_X, __N_X), '->', (__T_END, __T_END)]  # 749
    ]

    __aux_array = []  # temporary list
    __aux_position = 0  # initial temporary list position
    __position = 0  # input sequence symbol
    __var_position = 0  # variation position
    __rules_applied = []  # list of applied rules
    __last_seq_up_pos = None
    __last_seq_down_pos = None
    __res_variation = []  # list of resulting variations

    """ Class contructor with theme from input file and variation flags """

    def __init__(self, theme, variations):
        self.__theme = theme
        self.__variations = variations
        self.__dll = DLL()  # pushdown declaration as a doubly linked list

    """ Method does lexical analysis and returns list of tokens as notes. """

    def __tokenizer(self):
        tokens = []
        for note in self.__theme:
            if note.get('c1'):
                if note.get('c1') == 'full':
                    tokens.append(self.__T_C1_FULL)
                elif note.get('c1') == 'half':
                    tokens.append(self.__T_C1_HALF)
                elif note.get('c1') == 'quarter':
                    tokens.append(self.__T_C1_QUARTER)
                elif note.get('c1') == 'eight':
                    tokens.append(self.__T_C1_EIGHT)
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
                elif note.get('d1') == 'eight':
                    tokens.append(self.__T_D1_EIGHT)
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
                elif note.get('e1') == 'eight':
                    tokens.append(self.__T_E1_EIGHT)
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
                elif note.get('f1') == 'eight':
                    tokens.append(self.__T_F1_EIGHT)
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
                elif note.get('g1') == 'eight':
                    tokens.append(self.__T_G1_EIGHT)
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
                elif note.get('a1') == 'eight':
                    tokens.append(self.__T_A1_EIGHT)
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
                elif note.get('h1') == 'eight':
                    tokens.append(self.__T_H1_EIGHT)
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
                elif note.get('c2') == 'eight':
                    tokens.append(self.__T_C2_EIGHT)
                else:
                    print("C2 token error.")
                    exit(1)
            elif note.get('d2'):
                if note.get('d2') == 'full':
                    tokens.append(self.__T_D2_FULL)
                elif note.get('d2') == 'half':
                    tokens.append(self.__T_D2_HALF)
                elif note.get('d2') == 'quarter':
                    tokens.append(self.__T_D2_QUARTER)
                elif note.get('d2') == 'eight':
                    tokens.append(self.__T_D2_EIGHT)
                else:
                    print("C1 token error.")
                    exit(1)
            elif note.get('e2'):
                if note.get('e2') == 'full':
                    tokens.append(self.__T_E2_FULL)
                elif note.get('e2') == 'half':
                    tokens.append(self.__T_E2_HALF)
                elif note.get('e2') == 'quarter':
                    tokens.append(self.__T_E2_QUARTER)
                elif note.get('e2') == 'eight':
                    tokens.append(self.__T_E2_EIGHT)
                else:
                    print("D1 token error.")
                    exit(1)
            elif note.get('f2'):
                if note.get('f2') == 'full':
                    tokens.append(self.__T_F2_FULL)
                elif note.get('f2') == 'half':
                    tokens.append(self.__T_F2_HALF)
                elif note.get('f2') == 'quarter':
                    tokens.append(self.__T_F2_QUARTER)
                elif note.get('f2') == 'eight':
                    tokens.append(self.__T_F2_EIGHT)
                else:
                    print("E1 token error.")
                    exit(1)
            elif note.get('g2'):
                if note.get('g2') == 'full':
                    tokens.append(self.__T_G2_FULL)
                elif note.get('g2') == 'half':
                    tokens.append(self.__T_G2_HALF)
                elif note.get('g2') == 'quarter':
                    tokens.append(self.__T_G2_QUARTER)
                elif note.get('g2') == 'eight':
                    tokens.append(self.__T_G2_EIGHT)
                else:
                    print("F1 token error.")
                    exit(1)
            elif note.get('a2'):
                if note.get('a2') == 'full':
                    tokens.append(self.__T_A2_FULL)
                elif note.get('a2') == 'half':
                    tokens.append(self.__T_A2_HALF)
                elif note.get('a2') == 'quarter':
                    tokens.append(self.__T_A2_QUARTER)
                elif note.get('a2') == 'eight':
                    tokens.append(self.__T_A2_EIGHT)
                else:
                    print("G1 token error.")
                    exit(1)
            elif note.get('h2'):
                if note.get('h2') == 'full':
                    tokens.append(self.__T_H2_FULL)
                elif note.get('h2') == 'half':
                    tokens.append(self.__T_H2_HALF)
                elif note.get('h2') == 'quarter':
                    tokens.append(self.__T_H2_QUARTER)
                elif note.get('h2') == 'eight':
                    tokens.append(self.__T_H2_EIGHT)
                else:
                    print("A1 token error.")
                    exit(1)
            elif note.get('c3'):
                if note.get('c3') == 'full':
                    tokens.append(self.__T_C3_FULL)
                elif note.get('c3') == 'half':
                    tokens.append(self.__T_C3_HALF)
                elif note.get('c3') == 'quarter':
                    tokens.append(self.__T_C3_QUARTER)
                elif note.get('c3') == 'eight':
                    tokens.append(self.__T_C3_EIGHT)
                else:
                    print("H1 token error.")
                    exit(1)
        """ Adding bar line and end symbol. """
        tokens.append(self.__T_END)
        tokens.append(self.__THEME_END)
        return tokens

    """ Method selects rule from LL table.
        input_s is token symbol from input.
        stack_s is symbol from top of the pushdown. """

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

    """ Returns right side of a rule. """

    def __get_right_side(self, rule_number):
        return self.__rules[rule_number][2]

    """ Does reverse push to pushdown.
        items are symbols, that are being pushed
        deep is flag for deeper push into pushdown
        before nonterminal are being pushed items """

    def __reverse_push(self, items, deep, nonterminal):
        if type(items) != tuple:
            # items are not inside of a tuple
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
            # pushing reversed tuple
            """ How to reverse a tuple is from 
            https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python 
            Cited: 6 april, Author: mipadi """
            for item in items[::-1]:
                # deep push
                if not deep:
                    self.__dll.push(item)
                    # if it is nonterminal, then append it into aux array
                    if item == self.__N_X or item == self.__N_S and len(self.__aux_array) == 1:
                        self.__aux_array.append(self.__dll.head)
                    # inside of a rule is nonterminal N_R and append it into aux array
                    if item == self.__N_R:
                        self.__aux_array.append(self.__dll.head)
                else:
                    # receive inserted symbol and save it to aux array if it is nonterminal
                    result = self.__dll.insert(nonterminal, item)
                    if item == self.__N_X:
                        self.__aux_array.append(result)

    """ Get key from map, that is inside LL table"""

    def __get_key(self, dictionary, variation):
        # if variation exists in LL table, then return it, otherwise it is else
        for key in dictionary.keys():
            if variation == key:
                return key
        return 'else'

    """ Method returns number of a rule, that has to be applied. """

    def __get_rule_number(self, rule, variation, distances):
        res_rule = rule[self.__get_key(rule, variation)]
        # if inside the table is dictionary (contrary motion)
        if type(res_rule) == dict:
            try:
                con_rule = res_rule[distances[self.__position]]  # pick contrary rule from distance dictionary
            except:
                con_rule = con_rule = res_rule[0]  # if distance is out of range, then copy tone
            return con_rule
        else:
            return res_rule

    """ List through pushdown until last symbol and save resulting variation. """

    def __save_result(self):
        variation = []
        node = self.__dll.head
        while node and node.data != self.__THEME_END:
            variation.append(node.data)
            self.__dll.pop()
            node = node.next
        self.__res_variation.append(variation)
        print(self.__res_variation)

    """ Method returns resulting list of variations. """

    def get_result(self):
        return self.__res_variation

    """ Removes extra bar line, that is produced by rules. """

    def __remove_extra_bline(self, variation_count):
        if self.__var_position - 2 == 0:  # only one variation, then pop bar line
            if self.__variations[self.__var_position - 2] != 'grad':
                self.__dll.pop()
        elif 0 <= self.__var_position - 1 <= variation_count:  # if there is more variations cut extra bar line
            if self.__variations[self.__var_position - 1] != 'grad':
                self.__dll.pop()

    """ Method returns tuple number for requested token. """

    def __get_tuple_number(self, tuples, token):
        position = -1
        for token_tuple in tuples:
            position += 1
            if token in token_tuple:
                return position

    """ Gets distances between notes for contrary motion variation. 
        tokens is input list of tokens"""

    def __get_distances(self, tokens):
        last_token = -1
        result_dist = []
        tuple_list = [(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15), (16, 17, 18, 19), (20, 21, 22, 23),
                      (24, 25, 26, 27), (28, 29, 30, 31), (32, 33, 34, 35), (36, 37, 38, 39), (40, 41, 42, 43),
                      (44, 45, 46, 47), (48, 49, 50, 51), (52, 53, 54, 55), (56, 57, 58, 59)]
        for token in tokens:
            distance = 0
            if token == self.__T_END:
                break
            if last_token != -1:
                abs_token = self.__get_tuple_number(tuple_list, token)
                abs_last_token = self.__get_tuple_number(tuple_list, last_token)
                distance = (abs_last_token - abs_token) * 2
            last_token = tokens[0]
            result_dist.append(distance)
        return result_dist

    """ If there is multiple sequence variations, then there is need to pick last variation that was done. """
    def __select_tokens(self, tokens, variation_count):
        if self.__var_position > variation_count:  # last variation, then end it
            return self.__THEME_END
        if self.__variations[self.__var_position] == 'seq+' and self.__last_seq_up_pos is not None:
            tokens = self.__res_variation[self.__last_seq_up_pos]
            return tokens[self.__position]
        elif self.__variations[self.__var_position] == 'seq-' and self.__last_seq_down_pos is not None:
            tokens = self.__res_variation[self.__last_seq_down_pos]
            return tokens[self.__position]
        else:
            return tokens[self.__position]

    """ Generating music with help of syntax analysis. """

    def syntax_analysis(self):
        variation_count = len(self.__variations) - 1
        # Pushdown initialization
        self.__dll.push(self.__THEME_END)
        self.__dll.push(self.__N_S)
        # save nonterminal into aux array
        self.__aux_array.append(self.__dll.head)
        # receive tokens
        tokens = self.__tokenizer()
        distances = self.__get_distances(tokens)
        print(self.__variations)
        # while pushdown is not empty do generating
        while self.__dll.not_empty():
            cur_token = self.__select_tokens(tokens, variation_count)  # tokens[self.__position]  # get token
            if self.__dll.head.data == self.__T_END:  # on the top of the pushdown is bar line
                self.__var_position += 1  # move to next variation
                if cur_token == self.__THEME_END and self.__var_position > variation_count:
                    # end of variation save result
                    self.__remove_extra_bline(variation_count)
                    self.__save_result()
                    self.__dll.pop()
                elif cur_token == self.__T_END and self.__var_position > variation_count:
                    # variation is coming to end, move to last symbol
                    self.__position += 1
                else:
                    # save result and set pointer to next variation, refresh pushdown
                    self.__remove_extra_bline(variation_count)
                    self.__save_result()
                    if self.__variations[self.__var_position] == 'seq+':
                        self.__last_seq_up_pos = self.__var_position - 1
                    elif self.__variations[self.__var_position] == 'seq-':
                        self.__last_seq_down_pos = self.__var_position - 1
                    self.__aux_position = 0
                    self.__position = 0
                    self.__dll.push(self.__N_S)
                    self.__aux_array.append(self.__dll.head)
            elif self.__T_C1_FULL <= self.__dll.head.data <= self.__T_END:  # terminal
                # if on the top of the pushdown is terminal pop it, and move position to next input symbol
                if self.__dll.head.data == cur_token:
                    self.__dll.pop()
                    self.__position += 1
                else:
                    print("Wrong terminal on top of the pusdown.")
                    exit(1)
            elif self.__N_X <= self.__dll.head.data <= self.__N_R:  # nonterminal
                cur_varia = self.__variations[self.__var_position]  # get variation
                rule = self.__get_rule(cur_token, self.__dll.head.data)  # find rule in LL table
                # if top of the pushdown and aux array item is same and rule is dictionary from LL table
                if self.__dll.head.data == self.__N_S:
                    non_terminal = self.__aux_array[0]
                    popped = self.__dll.pop()
                    self.__aux_array.remove(popped)
                    self.__reverse_push(self.__get_right_side(self.__get_rule_number(rule, cur_varia, distances)),
                                        False, non_terminal)
                    self.__rules_applied.append(rule)
                else:
                    non_terminal = self.__aux_array[0]
                    popped = self.__dll.pop()  # get nonterminal from top of the pushdown
                    self.__aux_array.remove(popped)  # remove pointer form aux array
                    # get whole right-side of the rule
                    right_side = self.__get_right_side(self.__get_rule_number(rule, cur_varia, distances))
                    # if current variation is not retro-gration
                    if cur_varia != 'grad':
                        self.__reverse_push(right_side[0], False, non_terminal)  # push it in reverse on the top
                        deep_non_terminal = self.__aux_array[0]  # get second pointer to non-terminal
                        self.__aux_array.remove(deep_non_terminal)  # remove second pointer to non-terminal
                        self.__reverse_push(right_side[1], True, deep_non_terminal)  # deep rule push
                        self.__dll.remove(deep_non_terminal)  # remove second non-terminal from pushdown
                        self.__rules_applied.append(rule)  # save applied rule
                    else:
                        # retro-gration rule apply
                        self.__reverse_push(right_side, False, non_terminal)
            else:
                print("Wrong symbol.")
                exit(1)
