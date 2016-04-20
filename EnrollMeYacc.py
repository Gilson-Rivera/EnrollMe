# ------------------------------------------------------------
# EnrollMeYacc.py
# ------------------------------------------------------------
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from EnrollMeLex import tokens

# Import intermediate code module here
import EnrollMeTools

# Primary reduce statement
def p_statement(p):
    '''statement : statement_enroll
                 | statement_drop
                 | statement_change
                 | statement_available
                 | statement_schedule'''
    pass


def p_statement_enroll(p):
    'statement_enroll : ENROLL COURSE SECTION'
    p[0] = p[1] + p[2] + p[3]
    res = EnrollMeTools.enroll(p[2], p[3])
    print(res)

def p_statement_drop(p):
    'statement_drop : DROP COURSE'
    p[0] = p[1] + p[2]
    print("parsed 'statement_drop'")
    print("identifier: " + p[1])
    print("tokens: " + p[2])
    res = EnrollMeTools.drop(p[2])
    print(res)

def p_statement_change(p):
    'statement_change : CHANGE COURSE SECTION'
    p[0] = p[1] + p[2] + p[3]
    res = EnrollMeTools.change(p[2], p[3])
    print(res)

# Requisites:
#   When invoking available(), make sure to pass down arguments
#   in the correct order of course, professor, time.
def p_statement_available(p):
    '''statement_available : AVAILABLE COURSE PROFESSOR TIME
                         | AVAILABLE COURSE PROFESSOR
                         | AVAILABLE COURSE TIME
                         | AVAILABLE PROFESSOR TIME
                         | AVAILABLE COURSE
                         | AVAILABLE PROFESSOR
                         | AVAILABLE TIME
                         | AVAILABLE'''
    print("parsed 'statement_available'")
    print("identifier: " + p[1])
    print("tokens: ")
    for part in p[2:]:
        print(part)

# Requisites:
#   When invoking schedule(), table drawing of schedule
#   should be done in EnrollMeTools module.
def p_statement_schedule(p):
    'statement_schedule : SCHEDULE'
    p[0] = p[1]
    EnrollMeTools.schedule()

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
