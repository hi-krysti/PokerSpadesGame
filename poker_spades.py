cards = {
    'S2': 2,
    'S3': 3,
    'S4': 4,
    'S5': 5,
    'S6': 6,
    'S7': 7,
    'S8': 8,
    'S9': 9,
    'S10': 10,
    'SJ': 11,
    'SQ': 12,
    'SK': 13,
    'SA': 14
}


def check_straight(card1, card2, card3):
    hand = [cards[card1], cards[card2], cards[card3]]
    hand.sort()
    if hand[0] + 1 == hand[1] and hand[1] + 1 == hand[2]:
        return hand[2]
    else:
        return 0


def check_3ofa_kind(card1, card2, card3):
    hand = [cards[card1], cards[card2], cards[card3]]
    if hand[0] == hand[1] == hand[2]:
        return hand[2]
    else:
        return 0


def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0


def play_cards(left1, left2, left3, right1, right2, right3):
    left_rf = check_royal_flush(left1, left2, left3)
    right_rf = check_royal_flush(right1, right2, right3)
    left_str = check_straight(left1, left2, left3)
    right_str = check_straight(right1, right2, right3)
    left_3ofakind = check_3ofa_kind(left1, left2, left3)
    right_3ofakind = check_3ofa_kind(right1, right2, right3)
    while True:
        if left_rf > right_rf:
            return -1
        elif right_rf > left_rf:
            return 1
        elif left_rf == right_rf == 14:
            return 0
        elif left_str > right_str:
            return -1
        elif right_str > left_str:
            return 1
        elif left_str == right_str != 0:
            return 0
        elif left_3ofakind > right_3ofakind:
            return -1
        elif right_3ofakind > left_3ofakind:
            return 1
        elif left_3ofakind == right_3ofakind != 0:
            return 0
        else:
            return 0
