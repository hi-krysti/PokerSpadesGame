import unittest
import poker_spades


class MyTestCase(unittest.TestCase):
    def test_check_straight_zero(self):
        self.assertEqual(poker_spades.check_straight('S4', 'S6', 'S7'), 0)

    def test_check_straight_max(self):
        self.assertEqual(poker_spades.check_straight('S4', 'S6', 'S5'), 6)

    def test_check_straight_max_order(self):
        self.assertEqual(poker_spades.check_straight('S4', 'S5', 'S6'), 6)

    def test_check_straight_max_face(self):
        self.assertEqual(poker_spades.check_straight('SQ', 'SK', 'SA'), 14)

    def test_check_3ofa_kind_max_face(self):
        self.assertEqual(poker_spades.check_3ofa_kind('SQ', 'SQ', 'SQ'), 12)

    def test_check_3ofa_kind_zero_face(self):
        self.assertEqual(poker_spades.check_3ofa_kind('SQ', 'SQ', 'SK'), 0)

    def test_check_3ofa_kind_max(self):
        self.assertEqual(poker_spades.check_3ofa_kind('S3', 'S3', 'S3'), 3)

    def test_check_3ofa_kind_zero(self):
        self.assertEqual(poker_spades.check_3ofa_kind('S8', 'S3', 'S3'), 0)

    def test_check_royal_flush_max(self):
        self.assertEqual(poker_spades.check_royal_flush('SQ', 'SK', 'SA'), 14)

    def test_check_royal_flush_max_order(self):
        self.assertEqual(poker_spades.check_royal_flush('SA', 'SK', 'SQ'), 14)

    def test_check_royal_flush_zero(self):
        self.assertEqual(poker_spades.check_royal_flush('SJ', 'SK', 'SQ'), 0)

    def test_check_play_cards_left_rf(self):
        self.assertEqual(poker_spades.play_cards('SA', 'SK', 'SQ', 'SJ', 'SK', 'SQ'), -1)

    def test_check_play_cards_right_rf(self):
        self.assertEqual(poker_spades.play_cards('SJ', 'SK', 'SQ', 'SA', 'SK', 'SQ'), 1)

    def test_check_play_cards_rf_draw(self):
        self.assertEqual(poker_spades.play_cards('SA', 'SK', 'SQ', 'SQ', 'SK', 'SA'), 0)

    def test_check_play_cards_rf_wins(self):
        self.assertEqual(poker_spades.play_cards('SA', 'SA', 'SA', 'SQ', 'SK', 'SA'), 1)

    def test_check_play_cards_right_str(self):
        self.assertEqual(poker_spades.play_cards('S10', 'S9', 'SJ', 'S10', 'SQ', 'SJ'), 1)

    def test_check_play_cards_left_str(self):
        self.assertEqual(poker_spades.play_cards('S10', 'SQ', 'SJ', 'S10', 'S9', 'S8'), -1)

    def test_check_play_cards_str_draw(self):
        self.assertEqual(poker_spades.play_cards('S10', 'SQ', 'SJ', 'S10', 'SJ', 'SQ'), 0)

    def test_check_play_cards_str_wins(self):
        self.assertEqual(poker_spades.play_cards('S2', 'S3', 'S4', 'SA', 'SA', 'SA'), -1)

    def test_check_play_cards_3ofa_kind_draw(self):
        self.assertEqual(poker_spades.play_cards('SA', 'SA', 'SA', 'SA', 'SA', 'SA'), 0)

    def test_check_play_cards_left_3ofa_kind(self):
        self.assertEqual(poker_spades.play_cards('SA', 'SA', 'SA', 'S2', 'S2', 'S2'), -1)

    def test_check_play_cards_right_3ofa_kind(self):
        self.assertEqual(poker_spades.play_cards('S2', 'S2', 'S2', 'S7', 'S7', 'S7'), 1)

    def test_check_play_cards_dbl_losers(self):
        self.assertEqual(poker_spades.play_cards('SA', 'S3', 'S3', 'S7', 'SK', 'S10'), 0)


if __name__ == '__main__':
    unittest.main()


