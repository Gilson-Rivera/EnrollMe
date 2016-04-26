# ------------------------------------------------------------
# EnrollMeLex.py
# ------------------------------------------------------------
import ply.lex as lex

# Reserved words
reserved = {
   'enroll' : 'ENROLL',
   'drop' : 'DROP',
   'change' : 'CHANGE',
   'available' : 'AVAILABLE',
   'schedule' : 'SCHEDULE'
}

# List of token names. This is always required
tokens = [
    'COURSE',
    'SECTION',
    'PROFESSOR',
    'TIME',
    'ID'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_COURSE = r'[a-zA-Z]{4}[0-9]{4}'
t_SECTION = r'[0-9]{3}'
t_PROFESSOR = r'\b[a-zA-Z]+[+]?[a-zA-Z]+\b'

# Define a rule for time because of overlap with ID rule
def t_TIME(t):
    r'\bAM\b|\bPM\b|\bam\b|\bpm\b'
    return t

# Define a rule for reserved words
def t_ID(t):
    r'\b[a-z]+\b'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
