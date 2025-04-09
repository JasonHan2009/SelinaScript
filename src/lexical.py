from tokens import token_list
import ply.lex as lex

# === 词法分析器 ===
tokens = token_list

# 运算符定义
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUAL = r'='

# 数字处理
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# 空格处理
t_ignore = ' \t'


def t_PRINT(t):
    r'>>'
    return t  # Must return token explicitly
# 换行处理
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_INT(t):
    r'Int'
    return t

def t_FLOAT(t):
    r'Float'
    return t

def t__(t):
    r'_'
    return t

def t_LIST(t):
    r'List'
    return t

def t_STR(t):
    # 匹配双引号包裹
    r'\"([^\\\"]|\\.)*\"'
    return t

def t_CHAR(t):
    # 匹配单引号包裹（支持转义单引号）
    r"\'([^\\\']|\\.)*\'"
    return t

# 错误处理
def t_error(t):
    print(f"Illeagal Char: '{t.value[0]}'")
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.lineno = t.lexer.lineno  # This line already exists in your code
    return t


lexer = lex.lex()
