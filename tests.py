# coding=utf-8
import unittest

from test_task.string_parser import parser


class FuncTest(unittest.TestCase):
    def test_basic_example(self):
        """
        Test verifies if function returns a correct value on simple example.
        Input: s=”ccccdaababbbbccccdd”, k=3
        Explanation: 
            • The frequencies of the characters in the string are the following: a:3, b:5, c:8, d:3. 
            • If we sort the characters by frequency and alphabetical order, the result will be: c, b, a, d. 
            • First 3 characters of this list, joined into string will look like: ”cba”
        """
        args = ('ccccdaababbbbccccdd', 3)
        self.assertEqual(
            parser.func(*args),
            'cba'
        )

    def test_non_alpha_handling(self):
        """
        Test verifies if function returns a correct value if not only characters were provided.
        Input: s=”\nccc!cda? \n aba           b#@)bbb'c              c&(ccdd”, k=3 \t", k=3
        Explanation: 
            • The frequencies of the characters in the string are the following: a:3, b:5, c:8, d:3. 
            • If we sort the characters by frequency and alphabetical order, the result will be: c, b, a, d. 
            • First 3 characters of this list, joined into string will look like: ”cba”
        """
        args = ("\ncc123c!cda123? \n aba8907           b#@)478639491b,b.b\b'c              c&(ccdd”, k=3 \t", 3)
        self.assertEqual(
            parser.func(*args),
            "cba"
        )

    def test_freq_filter(self):
        """
        Test verifies if function returns a correct value on example of string with unique frequency characters.
        Input: s=”azzzzzbbxxxcccc”, k=2
        Explanation: 
            • The frequencies of the characters in the string are the following: a:1, b:2, c:4, x:3, z: 5. 
            • If we sort the characters by frequency and alphabetical order, the result will be: z, c, x, b, a. 
            • First 2 characters of this list, joined into string will look like: ”zc”
        """
        args = ('azzzzzbbxxxcccc', 2)
        self.assertEqual(
            parser.func(*args),
            'zc'
        )

    def test_alphabet_filter(self):
        """
        Test verifies if function returns a correct value on example of string with equally frequent characters.
        Input: s=”aaazzzbbbyyycccxxx”, k=4
        Explanation: 
            • The frequencies of the characters in the string are the following: a,b,c,x,y,z: 3. 
            • If we sort the characters by frequency and alphabetical order, the result will be: a, b, c, x, y, z. 
            • First 4 characters of this list, joined into string will look like: ”abcx”
        """
        args = ('aaazzzbbbyyycccxxx', 4)
        self.assertEqual(
            parser.func(*args),
            'abcx'
        )

    def test_s_type_error(self):
        """
        Test verifies if function can handle incorrect s parameter type
        """
        args = (int(), 1)
        self.assertEqual(
            parser.func(*args),
            '')

    def test_k_type_error(self):
        """
        Test verifies if function can handle incorrect k parameter type
        """
        args = (1, str())
        self.assertEqual(
            parser.func(*args),
            '')

    def test_s_is_empty_string(self):
        """
         Test verifies if function can handle case when the string is empty
         """
        args = ('', 1)
        self.assertEqual(parser.func(*args), '')

    def test_k_less_then_one(self):
        """
         Test verifies if function can handle case when k has a value > 1
        """
        args = ('a', 0)
        self.assertEqual(parser.func(*args), '')

    def test_s_handle_iterable(self):
        """
         Test verifies if function can handle case when an iterable(not string) was provided to s
        """
        args = ((['a', 'b', 'c', 'd']), 1)
        self.assertEqual(parser.func(*args), '')


if __name__ == '__main__':
    unittest.main()
