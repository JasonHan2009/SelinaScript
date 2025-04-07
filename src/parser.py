import ply.yacc as yacc
from lexical import lexer
from tokens import token_list

tokens = token_list

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('nonassoc', 'UMINUS'),
)
def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_binop(p):
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

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_string(p):
    '''
    string : STR
    '''
    p[0] = p[1]

def p_string_expr(p):
    '''
    expression : string
    '''
    p[0] = p[1][1:-1]

def p_char(p):
    '''
    char : CHAR
    '''
    p[0] = p[1][1:-1][0]

def p_char_expr(p):
    '''
    expression : char
    '''
    p[0] = p[1]

def p_int(p):
    '''
    int : INT
    '''
    p[0] = p[1]

def p_float(p):
    '''
    float : FLOAT
    '''
    p[0] = p[1]

def p__(p):
    '''
    empty : _
    '''
    p[0] = p[1]


def p_int_expr(p):
    '''
    expression : INT expression
    '''
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
   
    if '"' in p[2]:
        p[0] = 0  # Initialize sum
        for j in p[2][1:-1]:  # Remove quotes and iterate
            p[0] += int(ord(j))  # Accumulate ord values
    if "'" in p[2]:
        p[0] = 0  # Initialize sum
        for j in p[2][1:-1][0]:  # Remove quotes and iterate
            p[0] += int(ord(j))  # Accumulate ord values
    if is_number(p[2].replace('"', '')):
        p[0] = p[2].replace('"', '')

def p_float_expr(p):
    '''
    expression : FLOAT expression
    '''
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    if '"' in p[2]:
        p[0] = 0  # Initialize sum
        for j in p[2][1:-1]:  # Remove quotes and iterate
            p[0] += float(ord(j))  # Accumulate ord values
    if "'" in p[2]:
        p[0] = 0  # Initialize sum
        for j in p[2][1:-1][0]:  # Remove quotes and iterate
            p[0] += float(ord(j))  # Accumulate ord values
    if is_number(p[2].replace('"', '')):
        p[0] = float(p[2].replace('"', ''))

def p_printstmt(p):
    '''
    expression : PRINT expression
    '''
    if isinstance(p[2], str):
        # Handle all string types
        print(p[2])
        p[0] = p[2]
    else:
        print(p[2])
        p[0] = p[2]
# 解析字符串级运算(INT)
def p_string_calculate(p):
    '''
    expression : INT string PLUS string
               | INT string MINUS string
               | INT string TIMES string
               | INT string DIVIDE string
    '''
    # Convert both strings to their ordinal sums first
    left_sum = sum(ord(c) for c in p[2][1:-1])
    right_sum = sum(ord(c) for c in p[4][1:-1])

    # Then perform numeric operation
    if p[3] == '+':
        p[0] = left_sum + right_sum
    elif p[3] == '-':
        p[0] = left_sum - right_sum
    elif p[3] == '*':
        p[0] = left_sum * right_sum
    elif p[3] == '/':
        p[0] = left_sum / right_sum if right_sum != 0 else 0

# 解析字符串级运算(FLOAT)
def p_string_float_calculate(p):
    '''
    expression : float string PLUS string
               | float string MINUS string
               | float string TIMES string
               | float string DIVIDE string
               
    '''
    # Convert both strings to their ordinal sums first
    left_sum = sum(ord(c) for c in p[2][1:-1])
    right_sum = sum(ord(c) for c in p[4][1:-1])

    # Then perform numeric operation
    if p[3] == '+':
        p[0] = float(left_sum + right_sum)
    elif p[3] == '-':
        p[0] = float(left_sum - right_sum)
    elif p[3] == '*':
        p[0] = float(left_sum * right_sum)
    elif p[3] == '/':
        p[0] = float(left_sum / right_sum) if right_sum != 0.0 else 0.0

# 解析字符级运算
def p_char_calculate(p):
    '''
    expression : float char PLUS char
               | float char MINUS char
               | float char TIMES char
               | float char DIVIDE char
               
    '''
    # Convert both strings to their ordinal sums first
    left_sum = sum(ord(c) for c in p[2])
    right_sum = sum(ord(c) for c in p[4])

    # Then perform numeric operation
    if p[3] == '+':
        p[0] = float(left_sum + right_sum)
    elif p[3] == '-':
        p[0] = float(left_sum - right_sum)
    elif p[3] == '*':
        p[0] = float(left_sum * right_sum)
    elif p[3] == '/':
        p[0] = float(left_sum / right_sum) if right_sum != 0.0 else 0.0

# 解析字符级运算
def p_char_integer_calculate(p):
    '''
    expression : int char PLUS char
               | int char MINUS char
               | int char TIMES char
               | int char DIVIDE char
               
    '''
    left_sum = sum(ord(c) for c in p[2])
    right_sum = sum(ord(c) for c in p[4])

    # Then perform numeric operation
    if p[3] == '+':
        p[0] = int(left_sum + right_sum)
    elif p[3] == '-':
        p[0] = int(left_sum - right_sum)
    elif p[3] == '*':
        p[0] = int(left_sum * right_sum)
    elif p[3] == '/':
        p[0] = int(left_sum / right_sum) if right_sum != 0 else 0


# 解析字符串包裹的数字还有字符包裹的数字的相加（withtype）
def p_with_type_str_or_char_calc(p):
    '''
    expression : INT STR PLUS STR
               | INT STR MINUS STR
               | INT STR TIMES STR
               | INT STR DIVIDE STR

               | INT CHAR PLUS CHAR
               | INT CHAR MINUS CHAR
               | INT CHAR TIMES CHAR
               | INT CHAR DIVIDE CHAR

               | FLOAT STR PLUS STR
               | FLOAT STR MINUS STR
               | FLOAT STR TIMES STR
               | FLOAT STR DIVIDE STR

               | FLOAT CHAR PLUS CHAR
               | FLOAT CHAR MINUS CHAR
               | FLOAT CHAR TIMES CHAR
               | FLOAT CHAR DIVIDE CHAR

    '''
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    op1 = None 
    op2 = None
    left = p[1]
    if '"' in p[2] and '"' in p[4]:
        op1 = p[2][1:-1]
        op2 = p[4][1:-1]
    elif "'" in p[2] and "'" in p[4]:
        op1 = p[2][1:-1][0]
        op2 = p[4][1:-1][0]

    mid = p[3]
    if is_number(op1) and is_number(op2): 
        if mid == '+' and left == 'Int':
            p[0] = int(op1) + int(op2)
        elif mid == '-' and left == 'Int':
            p[0] = int(op1) - int(op2)
        elif mid == '*' and left == 'Int':
            p[0] = int(op1) * int(op2)
        elif mid == '/' and left == 'Int':
            p[0] = int(op1) / int(op2) if int(op2) != 0 else 0
        
        elif mid == '+' and left == 'Float':
            p[0] = float(op1) + float(op2)
        elif mid == '-' and left == 'Float':
            p[0] = float(op1) - float(op2)
        elif mid == '*' and left == 'Float':
            p[0] = float(op1) * float(op2)
        elif mid == '/' and left == 'Float':
            p[0] = float(op1) / float(op2) if float(op2) != 0.0 else 0.0
        
            

def p_empty(p):
    '''
    expression : empty expression
    '''
    p[0] = '_'

def p_error(p):
    print("语法错误!")
# === 初始化 ===
parser = yacc.yacc()

# === 测试用例 ===
if __name__ == "__main__":
    while (True):
        expr = input("CLI ")
        result = parser.parse(expr)
        