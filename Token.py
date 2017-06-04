assignment_operators = ['=', '+=', '-=', '*=', '/=', '%=']
logical_operators = ['&&', '||', '!']
relational_operators = ['==', '!=', '>', '<', '>=', '<=']
arithmetic_operators = ['+', '-', '*', '/', '++', '--']
boolean = ['true','false']

def isVariable(token):
    result = token[0].isalpha()
    for i in token[1:]:
        result = result and (i.isalpha() or i.isdigit())
    return result

def isCharacter(token):
    if len(token) == 3 and token[0] == '\'' and token[2] == '\'' and token[1].isalpha():
        return True

def token_statement_num(token):
    if token in relational_operators+logical_operators:
        return 17
    elif token in assignment_operators[1:]:
        return 0
    elif token in arithmetic_operators[:-2]:
        return 1
    elif token in arithmetic_operators[-2:]:
        return 2
    elif token == 'bool':
        return 3
    elif token == 'int':
        return 4
    elif token == 'char':
        return 5
    elif token == ';':
        return 6
    elif token == ',':
        return 7
    elif token == '=':
        return 8
    elif token == 'if':
        return 9
    elif token == 'while':
        return 10
    elif token == '(':
        return 11
    elif token == ')':
        return 12
    elif isVariable(token):
        return 13
    elif isCharacter(token):
        return 14
    else:
        try:
            int(token)
            return 15
        except:
            return 16

def token_expression_num(token):
    if token == '!':
        return 0
    elif token in logical_operators[:-1]:
        return 1
    elif token in relational_operators:
        return 2
    elif token in arithmetic_operators[:-2]:
        return 3
    elif token == '(':
        return 4
    elif token == ')':
        return 5
    elif token in boolean:
        return 6
    elif isCharacter(token):
        return 7
    elif isVariable(token):
        return 8
    else:
        try:
            int(token)
            return 9
        except:
            return 10
