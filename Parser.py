# coding=utf-8
"""
    Proyecto Final
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Abril 15 2023
    Compilador para lenguaje al estilo R.
"""

# Gramática LittleDuck
"""
def p_program(p):
    '''program : PROGRAM ID SEMICOLON program_vars block'''
    p[0] = "COMPILED"


def p_program_vars(p):
    '''program_vars : vars
               | empty'''


def p_vars(p):
    '''vars : VAR ID var_id COLON type SEMICOLON vars_block'''


def p_var_id(p):
    '''var_id : COMMA ID var_id
                | empty'''


def p_vars_block(p):
    '''vars_block : ID var_id COLON type SEMICOLON vars_block
                  | empty'''


def p_type(p):
    '''type : INT
            | FLOAT'''


def p_block(p):
    '''block : LEFTBRACKET statement_block RIGHTBRACKET'''


def p_statement_block(p):
    '''statement_block : statement statement_block
                       | empty'''


def p_statement(p):
    '''statement : assignment
                 | condition
                 | writing'''


def p_assignment(p):
    '''assignment : ID EQUALS expression SEMICOLON'''


def p_condition(p):
    '''condition : IF LEFTPAREN expression RIGHTPAREN block else_condition SEMICOLON'''


def p_else_condition(p):
    '''else_condition : ELSE block
                      | empty'''


def p_writing(p):
    '''writing : PRINT LEFTPAREN print_val RIGHTPAREN SEMICOLON'''


def p_print_val(p):
    '''print_val : expression print_exp
                 | CTESTRING print_exp'''


def p_print_exp(p):
    '''print_exp : COMMA  print_val
                 | empty'''


def p_expression(p):
    '''expression : exp comparation'''


def p_exp(p):
    '''exp : term operator'''


def p_comparation(p):
    '''comparation : GREATER exp
                      | LESS exp
                      | NOTEQUAL exp
                      | empty'''


def p_term(p):
    '''term : factor term_operator'''


def p_operator(p):
    '''operator : PLUS term operator
                | MINUS term operator
                | empty'''


def p_term_operator(p):
    '''term_operator : TIMES factor term_operator
                     | DIVIDE factor term_operator
                     | empty'''


def p_factor(p):
    '''factor : LEFTPAREN expression RIGHTPAREN
              | sign var_cte'''


def p_sign(p):
    '''sign : PLUS
            | MINUS
            | empty'''


def p_var_cte(p):
    '''var_cte : ID
               | CTEI
               | CTEF'''



# Reglas de Errores

def p_error(p):
    # raise Exception("Syntax error in input! - {} ".format(p))
    print("Syntax error in input! - {} ".format(p))


def p_empty(p):
    '''empty :'''
    pass

"""


import sys
import ply.yacc as yacc

from Lexer import tokens

yacc.yacc()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        file = sys.argv[1]
        try:
            f = open(file, 'r')
            data = f.read()
            f.close()
            if yacc.parse(data) == "COMPILED":
                print("Input válido")
        except EOFError:
            print(EOFError)
    else:
        print("Sin encontrar archivo para probar")