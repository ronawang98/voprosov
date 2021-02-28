import unittest
from abbreviation import abbreviation

class AbbreviationTest(unittest.TestCase):
    def test_valid_cases(self):
        self.assertTrue(abbreviation("AbcDE", "ABDE"))
        self.assertTrue(abbreviation("daBcd", "ABC"))
        self.assertTrue(abbreviation("zzzzzzzzzzz", "ZZZ"))
        self.assertTrue(abbreviation("zef", "ZF"))
        self.assertTrue(abbreviation("RonarOlL", "ROLL"))

    def test_invalid_cases(self):
        self.assertFalse(abbreviation("AbcDE", "AFDE"))
        self.assertFalse(abbreviation("fAFf", "FFFF"))
        self.assertFalse(abbreviation("zzzzzzzzzzzzzzzzzz", "ZZZZZZZZYZZZZZZZ"))
        self.assertFalse(abbreviation("zEf", "ZF"))
        self.assertFalse(abbreviation("string", "STRINGG"))


    def test_special_cases(self):
        self.assertTrue(abbreviation("fF", "F"))
        self.assertTrue(abbreviation("ABccCccb", "ABCB"))
        self.assertTrue(abbreviation("fffffffFFFFfffff", "FFFFFFFFF"))
        self.assertTrue(abbreviation("eEeEEeE", "EEEEE"))

    def test_empty_case(self):
        self.assertTrue(abbreviation("", ""))
