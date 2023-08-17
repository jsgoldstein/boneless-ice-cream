import unittest

from statistics import mean as _mean_

from set_1 import (
    print_str_5_times,
    str_5_times,
    str_n_times,
    str_5_times_as_list,
    str_n_times_as_list,
    flip_str,
    add_all_nums,
    mean
)

class TestSuite1(unittest.TestCase):

    def test_print_str_5_times(self):
        self.assertIsNone(
            print_str_5_times('cat')
        )

        with self.assertRaises(Exception) as e:
            print_str_5_times(10)

    def test_str_5_times(self):
        self.assertEqual(
            str_5_times('cat'),
            'catcatcatcatcat'
        )
        self.assertEqual(
            str_5_times(''),
            ''
        )
        self.assertEqual(
            str_5_times(' '),
            '     '
        )
        with self.assertRaises(Exception) as e:
            str_5_times(10)

    def test_str_n_times(self):
        self.assertEqual(
            str_n_times('cat', 2),
            'catcat'
        )
        self.assertEqual(
            str_n_times('cat', 0),
            ''
        )
        with self.assertRaises(Exception) as e:
            str_n_times('cat', -1)

        self.assertEqual(
            str_n_times('', 5),
            ''
        )
        self.assertEqual(
            str_n_times(' ', 1),
            ' '
        )

    def test_str_5_times_as_list(self):
        self.assertEqual(
            str_5_times_as_list('cat'),
            ["cat", "cat", "cat", "cat", "cat"]
        )
        self.assertEqual(
            str_5_times_as_list(''),
            ["", "", "", "", ""]
        )

    def test_str_n_times_as_list(self):
        self.assertEqual(
            str_n_times_as_list('cat', 2),
            ['cat', 'cat']
        )
        self.assertEqual(
            str_n_times_as_list('cat', 0),
            []
        )
        with self.assertRaises(Exception) as e:
            str_n_times_as_list('cat', -1)

    def test_flip_str(self):
        self.assertEqual(
            flip_str('cat'),
            'tac'
        )
        self.assertEqual(
            flip_str(''),
            ''
        )
        self.assertEqual(
            flip_str('racecar'),
            'racecar'
        )

    def test_add_all_nums(self):
        self.assertEqual(
            add_all_nums([1, 2, 3]),
            sum([1, 2, 3])
        )
        self.assertEqual(
            add_all_nums([1, -1, 1, -1]),
            sum([1, -1, 1, -1])
        )
        self.assertEqual(
            add_all_nums([-1, -1, -1, -1]),
            sum([-1, -1, -1, -1])
        )
        self.assertEqual(
            add_all_nums([20, ]),
            sum([20, ])
        )
        self.assertEqual(
            add_all_nums(list()),
            sum(list())
        )

    def test_mean(self):
        self.assertEqual(
            mean([1, 2, 3]),
            _mean_([1, 2, 3])
        )
        self.assertEqual(
            mean([1, -1, 1, -1]),
            _mean_([1, -1, 1, -1])
        )
        self.assertEqual(
            mean([-1, -1, -1, -1]),
            _mean_([-1, -1, -1, -1])
        )
        self.assertEqual(
            mean([20, ]),
            _mean_([20, ])
        )
        with self.assertRaises(Exception) as e:
            mean(list())

if __name__ == '__main__':
    # Run with `python -m pytest`
    unittest.main()
