import unittest


def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last

    else:
        full_name = first + ' ' + last
    return full_name.title()


class NamesTestCase(unittest.TestCase):
    """Tests for 'get_formatted_name'."""

    def test_1(self):
        """Do names like 'Antoniete Gomez' work?"""
        formatted_name = get_formatted_name('antoniete', 'gomez')
        self.assertEqual(formatted_name, 'Antoniete Gomez')

    def test_2(self):
        """Do names like 'Mario Antoniete Gomez' work? """
        formatted_name = get_formatted_name('mario', 'gomez','antoniete')
        self.assertEqual(formatted_name, 'Mario Antoniete Gomez')


unittest.main()
