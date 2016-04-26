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
    p[0] = p[1]
    pass


def p_statement_enroll(p):
    'statement_enroll : ENROLL COURSE SECTION'
    p[0] = p[1] + p[2] + p[3]
    res = EnrollMeTools.enroll(p[2], p[3])
    print(res)

def p_statement_drop(p):
    'statement_drop : DROP COURSE'
    p[0] = p[1] + p[2]
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
    '''statement_available : statement_available_cpt
                           | statement_available_cp
                           | statement_available_ct
                           | statement_available_pt
                           | statement_available_c
                           | statement_available_p
                           | statement_available_t
                           | AVAILABLE'''
    p[0] = p[1]
    if(p[1] == 'available'):
        res = EnrollMeTools.available(None, None, None)
        print(res)
    pass

def p_statement_available_cpt(p):
    'statement_available_cpt : AVAILABLE COURSE PROFESSOR TIME'
    p[0] = p[1] + p[2] + p[3] + p[4]
    res = EnrollMeTools.available(p[2], p[3], p[4])
    print(res)

def p_statement_available_cp(p):
    'statement_available_cp : AVAILABLE COURSE PROFESSOR'
    p[0] = p[1] + p[2] + p[3]
    res = EnrollMeTools.available(p[2], p[3], None)
    print(res)

def p_statement_available_ct(p):
    'statement_available_ct : AVAILABLE COURSE TIME'
    p[0] = p[1] + p[2] + p[3]
    res = EnrollMeTools.available(p[2], None, p[3])
    print(res)

def p_statement_available_pt(p):
    'statement_available_pt : AVAILABLE PROFESSOR TIME'
    p[0] = p[1] + p[2] + p[3]
    res = EnrollMeTools.available(None, p[2], p[3])
    print(res)

def p_statement_available_c(p):
    'statement_available_c : AVAILABLE COURSE'
    p[0] = p[1] + p[2]
    res = EnrollMeTools.available(p[2], None, None)
    print(res)

def p_statement_available_p(p):
    'statement_available_p : AVAILABLE PROFESSOR'
    p[0] = p[1] + p[2]
    res = EnrollMeTools.available(None, p[2], None)
    print(res)

def p_statement_available_t(p):
    'statement_available_t : AVAILABLE TIME'
    p[0] = p[1] + p[2]
    res = EnrollMeTools.available(None, None, p[2])
    print(res)

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
