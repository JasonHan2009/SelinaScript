import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'NUMBER',
    'PLUS', 'MINUS',
    'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'PRINT', 'STR', 'CHAR'
)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_PRINT = r'>>'
t_ignore  = ' \t'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def t_STR(t):
    r'\"[^"]*\"'
    return t

def t_CHAR(t):
    r"\'[^']*\'"
    return t


# Parser
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

def p_expression(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression

    '''
    if p[2] == '+': 
        p[0] = p[1] + p[3]
    elif p[2] == '-': 
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/': 
        p[0] = p[1] / p[3]

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_str(p):
    'expression : STR'
    p[0] = p[1]

def p_expression_char(p):
    'expression : CHAR'
    p[0] = p[1]

def p_datatype(p):
    '''
    datatype : DATATYPE expression
    '''
    p[0] = p[1]

def p_error(p):
    print("Syntax error!")

def p_print(p):
    '''expression : PRINT STR
                  | PRINT CHAR
                  | PRINT NUMBER
                  | PRINT expression
    '''
    if p.slice[2].type == 'STR':  # Check token type instead of content
        print(p[2][1:-1])
    elif p.slice[2].type == 'CHAR':
        print(p[2][1])
    elif p.slice[2].type == 'NUMBER':
        print(p[2])
    elif p.slice[2].type == 'expression':
        print(p[2])
    

lexer = lex.lex()
parser = yacc.yacc()

# Test function
def calculate(expression):
    return parser.parse(expression)

if __name__ == '__main__':
    test_cases = [
        ">> '1' + 3"
    ]
    
    for expr in test_cases:
        result = calculate(expr)

