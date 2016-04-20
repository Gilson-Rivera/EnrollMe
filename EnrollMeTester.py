from EnrollMeLex import lexer

import unittest



class MyTestFunctions(unittest.TestCase):


    # Test for correct tokenization of IDs (reserved words)
    def test_valid_ID(self):

        lexer.input("enroll")
        self.assertMultiLineEqual("LexToken(ENROLL,'enroll',1,0)", str(lexer.token()))

        lexer.input("drop")
        self.assertEqual("LexToken(DROP,'drop',1,0)", str(lexer.token()))

        lexer.input("change")
        self.assertEqual("LexToken(CHANGE,'change',1,0)", str(lexer.token()))

        lexer.input("available")
        self.assertEqual("LexToken(AVAILABLE,'available',1,0)", str(lexer.token()))

        lexer.input("schedule")
        self.assertEqual("LexToken(SCHEDULE,'schedule',1,0)", str(lexer.token()))


    def test_enroll_a_course(self):
        lexer.input("enroll ICOM4036")

        self.assertEqual("LexToken(ENROLL,'enroll',1,0)", str(lexer.token()))
        self.assertEqual("LexToken(COURSE,'ICOM4036',1,7)", str(lexer.token()))

    def test_drop_a_course(self):
        lexer.input("drop ICOM4036 030")

        self.assertMultiLineEqual("LexToken(DROP,'drop',1,0)", str(lexer.token()))
        self.assertEqual("LexToken(COURSE,'ICOM4036',1,5)", str(lexer.token()))
        self.assertEqual("LexToken(SECTION,'030',1,14)", str(lexer.token()))

    def test_change_a_course(self):
        lexer.input("change ICOM5995")

        self.assertEqual("LexToken(CHANGE,'change',1,0)", str(lexer.token()))
        self.assertEqual("LexToken(COURSE,'ICOM5995',1,7)", str(lexer.token()))

    def test_schedule(self):
        lexer.input("schedule morning")

        self.assertEqual("LexToken(SCHEDULE,'schedule',1,0)", str(lexer.token()))
        self.assertEqual("LexToken(TIME,'morning',1,9)", str(lexer.token()))


    if __name__ == '__main__':
        unittest.main(exit=False)