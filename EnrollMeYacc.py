# ------------------------------------------------------------
# EnrollMeYacc.py
# ------------------------------------------------------------
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from EnrollMeLex import tokens

# Import intermediate code module here


# Primary reduce statement
def p_statement(p):
    '''statement : statement_enroll
                 | statement_drop
                 | statement_change
                 | statement_available
                 | statement_schedule'''
    print("parsed 'statement'")
    pass


def p_statement_enroll(p):
    'statement_enroll : ENROLL COURSE SECTION'
    p[0] = p[1] + p[2] + p[3]
    # Substitute for real implementation, which should call
    # methods defined in imported module.
    print("parsed 'statement_enroll'")
    print("identifier: " + p[1])
    print("tokens: " + p[2] + " " + p[3])

def p_statement_drop(p):
    'statement_drop : DROP COURSE'
    p[0] = p[1] + p[2]
    # Same
    print("parsed 'statement_drop'")
    print("identifier: " + p[1])
    print("tokens: " + p[2])

def p_statement_change(p):
    'statement_change : CHANGE COURSE SECTION'
    p[0] = p[1] + p[2] + p[3]
    # Same
    print("parsed 'statement_change'")
    print("identifier: " + p[1])
    print("tokens: " + p[2] + " " + p[3])

def p_statement_available(p):
    '''statement_available : AVAILABLE COURSE PROFESSOR TIME
                         | AVAILABLE COURSE PROFESSOR
                         | AVAILABLE COURSE TIME
                         | AVAILABLE PROFESSOR TIME
                         | AVAILABLE COURSE
                         | AVAILABLE PROFESSOR
                         | AVAILABLE TIME
                         | AVAILABLE'''
    # Same
    print("parsed 'statement_available'")
    print("identifier: " + p[1])
    print("tokens: ")
    for part in p[2:]:
        print(part)

def p_statement_schedule(p):
    'statement_schedule : SCHEDULE'
    p[0] = p[1]
    # Same

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = raw_input('EnrollMe > ')
    except EOFError:
        break
    if s == 'quit': break
    if not s: continue
    result = parser.parse(s)
