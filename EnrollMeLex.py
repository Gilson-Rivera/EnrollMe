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
    'SECTION'
]

# Regular expression rules for simple tokens
t_COURSE = r'[a-zA-z]{4}[0-9]{4}'
t_SECTION = r'[0-9]{3}'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test
s = "enroll icom4036 030"
print('lexer:'+ str(lexer))
print('input: ' + s)
print('tokens: ')
lexer.input(s)
for tok in lexer:
    print(tok)

if __name__ == "__main__":
    import sys
