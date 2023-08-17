import unittest

from set_2 import (
    is_num_in_list,
    count_times_in_list,
    reverse_list,
    remove_str_from_list,
    remove_duplicates_from_list,
    get_largest_num_from_list,
    get_size_of_longest_string_from_list,
    get_index_of_largest_string_from_list
)

class TestSuite2(unittest.TestCase):

    def test_is_num_in_list(self):
        self.assertTrue(
            type(is_num_in_list([], 1) == bool)
        )
        self.assertTrue(
            type(is_num_in_list([1, 2, 3], 1) == bool)
        )

        self.assertTrue(
            is_num_in_list([1, 2, 3], 1)
        )
        self.assertFalse(
            is_num_in_list([1, 2, 3], 10)
        )

        with self.assertRaises(Exception) as e:
            is_num_in_list([1, 2, 3], 'cat')

    def test_count_times_in_list(self):
        self.assertTrue(
            type(count_times_in_list([], 1) == int)
        )

        self.assertEqual(
            count_times_in_list([1, 2, 3], 1),
            1
        )
        self.assertEqual(
            count_times_in_list([1, 1, 1], 1),
            3
        )

        self.assertEqual(
            count_times_in_list([1, 2, 3], 10),
            0
        )

        with self.assertRaises(Exception) as e:
            count_times_in_list([1, 2, 3], 'cat')

    def test_reverse_list(self):
        self.assertEqual(
            reverse_list(['jake', 'was', 'here']),
            ['here', 'was', 'jake']
        )
        self.assertEqual(
            reverse(['jake']),
            ['jake']
        )

    def test_remove_str_from_list(self):
        words = ['i', 'do', 'not', 'like', 'green', 'eggs', 'and', 'ham', 'i', 'do', 'not', 'like', 'them', 'sam', 'i', 'am']
        no_i = ['do', 'not', 'like', 'green', 'eggs', 'and', 'ham', 'do', 'not', 'like', 'them', 'sam', 'am']

        self.assertEqual(
            remove_str_from_list(sorted(words), 'i'),
            sorted(no_i)
        )
        self.assertEqual(
            remove_str_from_list(sorted(words), 'jake'),
            sorted(words)
        )

        self.assertEqual(
            remove_str_from_list(sorted(['cat', 'cat', 'cat', 'cat']), 'cat'),
            ['cat']
        )


    def test_remove_duplicates_from_list(self):
        words = ['i', 'do', 'not', 'like', 'green', 'eggs', 'and', 'ham', 'i', 'do', 'not', 'like', 'them', 'sam', 'i', 'am']
        no_dupes = ['i', 'do', 'not', 'like', 'green', 'eggs', 'and', 'ham', 'them', 'sam', 'am']

        self.assertEqual(
            remove_duplicates_from_list(sorted(words)),
            sorted(no_dupes)
        )
        self.assertEqual(
            remove_duplicates_from_list([]),
            []
        )
        self.assertEqual(
            remove_duplicates_from_list(sorted(['cat', 'cat', 'cat', 'cat']), 'cat'),
            ['cat']
        )

    def test_get_largest_num_from_list(self):
        self.assertEqual(
            get_largest_num_from_list([100, 10, 1, 1000, 5000]),
            5000
        )
        self.assertEqual(
            get_largest_num_from_list([-100, -10, -1, -1000, -5000]),
            -1
        )
        self.assertEqual(
            get_largest_num_from_list([1, -1, -1, -1, 1]),
            1
        )
        with self.assertRaises(Exception) as e:
            get_largest_num_from_list([])

    def test_get_size_of_longest_string_from_list(self):
        words = ['i', 'do', 'not', 'like', 'green', 'eggs', 'and', 'ham', 'i', 'do', 'not', 'like', 'them', 'sam', 'i', 'am']

        self.assertEqual(
            get_size_of_longest_string_from_list(words),
            5
        )
        self.assertEqual(
            get_size_of_longest_string_from_list([]),
            0
        )
        with self.assertRaises(Exception) as e:
            get_size_of_longest_string_from_list([1, 2, 3])
        

    def test_get_index_of_largest_string_from_list(self):
        words = ['i', 'do', 'not', 'like', 'green', 'eggs', 'and', 'ham', 'i', 'do', 'not', 'like', 'them', 'sam', 'i', 'am']

        self.assertEqual(
            get_index_of_largest_string_from_list(words),
            4
        )


if __name__ == '__main__':
    # Run with `python -m pytest`
    unittest.main()
