from EnrollMeLex import lexer

import unittest



class MyTestFunctions(unittest.TestCase):


    # Test for correct tokenization of IDs (reserved words)
    def test_valid_ID(self):

        lexer.input("enroll")
        self.assertMultiLineEqual(str(lexer.token()), "LexToken(ENROLL,'enroll',1,0)")

        lexer.input("drop")
        self.assertEqual(str(lexer.token()), "LexToken(DROP,'drop',1,0)")

        lexer.input("change")
        self.assertEqual(str(lexer.token()), "LexToken(CHANGE,'change',1,0)")

        lexer.input("available")
        self.assertEqual(str(lexer.token()), "LexToken(AVAILABLE,'available',1,0)")

        lexer.input("schedule")
        self.assertEqual(str(lexer.token()), "LexToken(SCHEDULE,'schedule',1,0)")


    def test_enroll_a_course(self):
        lexer.input("enroll ICOM4036")

        self.assertEqual(str(lexer.token()), "LexToken(ENROLL,'enroll',1,0)")
        self.assertEqual(str(lexer.token()), "LexToken(COURSE,'ICOM4036',1,7)")

    def test_drop_a_course(self):
        lexer.input("drop ICOM4036 030")

        self.assertMultiLineEqual(str(lexer.token()), "LexToken(DROP,'drop',1,0)")
        self.assertEqual(str(lexer.token()), "LexToken(COURSE,'ICOM4036',1,5)")
        self.assertEqual(str(lexer.token()), "LexToken(SECTION,'030',1,14)")

    def test_change_a_course(self):
        lexer.input("change ICOM5995")

        self.assertEqual(str(lexer.token()), "LexToken(CHANGE,'change',1,0)")
        self.assertEqual(str(lexer.token()), "LexToken(COURSE,'ICOM5995',1,7)")

    def test_schedule(self):
        lexer.input("schedule morning")

        self.assertEqual(str(lexer.token()), "LexToken(SCHEDULE,'schedule',1,0)")
        self.assertEqual(str(lexer.token()), "LexToken(TIME,'morning',1,9)")


    if __name__ == '__main__':
        unittest.main(exit=False)