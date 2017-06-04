from Token import *

from Syntax import statement_automata, expression_automata

operation_priority = {'(': 1, '+': 2, '+=': 2, '-': 2, '-=': 2, '*': 3, '*=': 3, '/': 3, '/=': 3}

operation_stack = []
variable_stack = []

defined_var = dict()


def get_value(var):
    try:
        res = int(var)
        return [[],res,False]
    except:
        return defined_var[var]+[True]


def is_var(var):
    try:
        res = int(var)
        return False
    except:
        return True

def calculate():
    tmp_operation = operation_stack.pop()
    if tmp_operation in ['-', '-=']:
        first_num = get_value(variable_stack.pop())
        second_num = get_value(variable_stack.pop())
        if first_num is None or second_num is None :
            return ['Variable is Undefined',False]
        if first_num[2] == True :
            if first_num[0] == 'int':
                if second_num[2] == True :
                    if second_num[0] == 'int':
                        return [second_num[1] - first_num[1], True]
                    return [second_num[:-1], False]
                return [second_num[1] - first_num[1], True]
            return [first_num[:-1],False]
        if second_num[2] == True:
            if second_num[0] == 'int':
                return [second_num[1] - first_num[1], True]
            return [second_num[:-1], False]
        return [second_num[1] - first_num[1], True]
    if tmp_operation in ['+', '+=']:
        first_num = get_value(variable_stack.pop())
        second_num = get_value(variable_stack.pop())
        if first_num is None or second_num is None :
            return ['Variable is Undefined',False]
        if first_num[2] == True:
            if first_num[0] == 'int':
                if second_num[2] == True:
                    if second_num[0] == 'int':
                        return [second_num[1] + first_num[1], True]
                    return [second_num[:-1], False]
                return [second_num[1] + first_num[1], True]
            return [first_num[:-1], False]
        if second_num[2] == True:
            if second_num[0] == 'int':
                return [second_num[1] + first_num[1], True]
            return [second_num[:-1], False]
        return [second_num[1] + first_num[1], True]
    if tmp_operation in ['*', '*=']:
        first_num = get_value(variable_stack.pop())
        second_num = get_value(variable_stack.pop())
        if first_num is None or second_num is None :
            return ['Variable is Undefined',False]
        if first_num[2] == True:
            if first_num[0] == 'int':
                if second_num[2] == True:
                    if second_num[0] == 'int':
                        return [second_num[1] * first_num[1], True]
                    return [second_num[:-1], False]
                return [second_num[1] * first_num[1], True]
            return [first_num[:-1], False]
        if second_num[2] == True:
            if second_num[0] == 'int':
                return [second_num[1] * first_num[1], True]
            return [second_num[:-1], False]
        return [second_num[1] * first_num[1], True]
    if tmp_operation in ['/', '/=']:
        first_num = get_value(variable_stack.pop())
        second_num = get_value(variable_stack.pop())
        if first_num is None or second_num is None :
            return ['Variable is Undefined',False]
        if first_num[2] == True:
            if first_num[0] == 'int':
                if second_num[2] == True:
                    if second_num[0] == 'int':
                        if first_num[1] == 0:
                            return ['Division by Zero', False]
                        return [second_num[1] / first_num[1], True]
                    return [second_num[:-1], False]
                if first_num[1] == 0:
                    return ['Division by Zero', False]
                return [second_num[1] / first_num[1], True]
            return [first_num[:-1], False]
        if second_num[2] == True:
            if second_num[0] == 'int':
                if first_num[1] == 0:
                    return ['Division by Zero', False]
                return [second_num[1] / first_num[1], True]
            return [second_num[:-1], False]
        if first_num[1] == 0:
            return ['Division by Zero', False]
        return [second_num[1] / first_num[1], True]


def find_end(tokens,start_token,char):
    token_enum = start_token + 0
    if char == ')':
        parentheses_count = 0
        finded = False
        while not finded:
            if tokens[token_enum] == '(':
                parentheses_count += 1
            elif tokens[token_enum] == ')':
                parentheses_count -= 1
            if parentheses_count == 0:
                return token_enum
            token_enum += 1
        return -1
    else:
        if char == '}':
            brace_count = 0
            finded = False
            while not finded:
                if tokens[token_enum] == '{':
                    brace_count += 1
                elif tokens[token_enum] == '}':
                    brace_count -= 1
                if brace_count == 0:
                    return token_enum
                token_enum += 1
            return -1
        elif char == ';':
            finded = False
            while not finded and token_enum<len(tokens):
                if tokens[token_enum] == ';':
                    return token_enum + 1
                token_enum += 1
            return -1


def check_expression(tokens,start=0,end=0):
    current_state = 0
    token_enum = start + 0
    while token_enum < end and current_state >= 0:
        tmp_token = tokens[token_enum].strip()
        tmp_state = current_state + 0
        current_state = expression_automata[current_state][token_expression_num(tokens[token_enum].strip())]
        if current_state == 3:
            if tmp_token in defined_var:
                variable_stack.append(tmp_token)
            else:
                return ['Variable is not Defined',False,token_enum]
        if current_state == 4 or current_state == 9:
            if len(operation_stack) > 0 and operation_priority[operation_stack[-1]] > operation_priority[tmp_token] and tmp_token is not '(':
                while len(operation_stack) > 0 and operation_priority[operation_stack[-1]] > operation_priority[tmp_token] and tmp_token is not '(':
                    cal_res = calculate()
                    if cal_res[1]:
                        variable_stack.append(cal_res[0])
                    else:
                        return cal_res+[token_enum]
            elif len(operation_stack) > 0 and tmp_token != '(' and operation_stack[-1] != '(' and operation_priority[
                operation_stack[-1]] == operation_priority[tmp_token]:
                cal_res = calculate()
                if cal_res[1]:
                    variable_stack.append(cal_res[0])
                else:
                    return cal_res+[token_enum]
            operation_stack.append(tmp_token)
        if current_state == 2 or current_state == 6:
            if tmp_token == ')':
                while operation_stack[-1] is not '(':
                    cal_res = calculate()
                    if cal_res[1]:
                        variable_stack.append(cal_res[0])
                    else:
                        return cal_res+[token_enum]
                operation_stack.pop()
            else:
                variable_stack.append(tmp_token)
        if (tmp_state == 2 and current_state == 5) or (tmp_state == 6 and current_state == 0) or token_enum == end-1:
            while len(operation_stack) > 0:
                cal_res = calculate()
                if cal_res[1]:
                    variable_stack.append(cal_res[0])
                else:
                    return cal_res+[token_enum]
        token_enum += 1
    return [current_state,True,token_enum]


def sem_check(tokens,start=0,end=0):
    return check_statement(tokens=tokens,start=start,end=end)


def check_statement(tokens,start=0,end=0):
    current_state = 0
    token_enum = start
    token_end = end
    while token_enum < token_end:
        tmp_token = tokens[token_enum].strip()
        tmp_state = current_state + 0
        current_state = statement_automata[current_state][token_statement_num(tmp_token)]
        if current_state == 13:
            if defined_var[last_variable][0] != 'int':
                return ['Variable Type is not Int',False,token_enum]
            if tmp_token=='++':
                defined_var[last_variable][1] += 1
            else:
                defined_var[last_variable][1] -= 1
        if current_state == 12:
            if tmp_token in defined_var:
                last_variable = tmp_token
            else:
                return ['Variable is not Defined',False,token_enum]
        if current_state == 9:
            if tmp_token not in defined_var:
                defined_var[tmp_token] = ['int',None]
                last_variable = tmp_token
            else:
                return ['Variable is Defined Before',False,token_enum]
        elif current_state == 2 :
            if tmp_token not in defined_var:
                defined_var[tmp_token] = ['char', None]
                last_variable = tmp_token
            else:
                return ['Variable is Defined Before',False, token_enum]
        elif current_state == 6:
            if tmp_token not in defined_var:
                defined_var[tmp_token] = ['bool', None]
                last_variable = tmp_token
            else:
                return ['Variable is Defined Before',False, token_enum]
        if current_state == 10 and tmp_token is not '=':
            if tmp_token in ['+=', '-=', '*=', '/=']:
                variable_stack.append(last_variable)
            if len(operation_stack) > 0 and operation_priority[operation_stack[-1]] > operation_priority[tmp_token] and tmp_token is not '(':
                while len(operation_stack) > 0 and operation_priority[operation_stack[-1]] > operation_priority[tmp_token] and tmp_token is not '(':
                    cal_res = calculate()
                    if cal_res[1]:
                        variable_stack.append(cal_res[0])
                    else:
                        return cal_res + [token_enum]
            elif len(operation_stack)>0 and tmp_token!='(' and operation_stack[-1]!='(' and operation_priority[operation_stack[-1]] == operation_priority[tmp_token]:
                cal_res = calculate()
                if cal_res[1]:
                    variable_stack.append(cal_res[0])
                else:
                    return cal_res + [token_enum]
            operation_stack.append(tmp_token)
        if current_state == 11:
            if tmp_token == ')':
                while operation_stack[-1] is not '(':
                    cal_res = calculate()
                    if cal_res[1]:
                        variable_stack.append(cal_res[0])
                    else:
                        return cal_res + [token_enum]
                operation_stack.pop()
            else:
                variable_stack.append(tmp_token)
        if tmp_state == 11 and current_state == 0:
            while len(operation_stack)> 0:
                cal_res = calculate()
                if cal_res[1]:
                    variable_stack.append(cal_res[0])
                else:
                    return cal_res + [token_enum]
            defined_var[last_variable][1] = int(variable_stack.pop())
            print(defined_var[last_variable])
        if current_state == 0 and tmp_token == 'if':
            result = check_if(tokens,start=token_enum+1)
            if result[1]:
                token_enum = result[0] + 1
            else:
                return result
        elif current_state == 0 and tmp_token == 'while':
            result = check_while(tokens,start=token_enum+1)
            if result[1]:
                token_enum = result[0] + 1
            else:
                return result
        token_enum += 1
    return [current_state , True , token_enum]


def check_if(tokens,start):
    token_enum = start + 0
    if tokens[token_enum] == '(':
        start_statement = find_end(tokens, token_enum, char=')')
        result = check_expression(tokens, start=token_enum + 1, end=start_statement)
        if not result[1]:
            return result
        else:
            if tokens[start_statement + 1] == '{':
                end_statement = find_end(tokens, start_statement + 1, char='}')
                statement_bool = check_statement(tokens=tokens, start=start_statement + 2, end=end_statement)
                if not statement_bool[1]:
                    return [statement_bool[0] , False , statement_bool[2]]
            else:
                end_statement = find_end(tokens, start_statement + 1, char=';')
                statement_bool = check_statement(tokens=tokens, start=start_statement + 1, end=end_statement)
                if not statement_bool[1]:
                    return [statement_bool[0] , False , statement_bool[2]]
            if len(tokens) > end_statement+1 and tokens[end_statement+1] == 'else':
                if tokens[end_statement + 2] == '{':
                    end_statement_tmp = find_end(tokens, end_statement + 2, char='}')
                    statement_bool = check_statement(tokens=tokens, start=end_statement + 3, end=end_statement_tmp)
                    if not statement_bool[1]:
                        return [statement_bool[0] , False , statement_bool[2]]
                else:
                    end_statement_tmp = find_end(tokens, end_statement + 2, char=';')
                    statement_bool = check_statement(tokens=tokens, start=end_statement + 2, end=end_statement_tmp)
                    if not statement_bool[1]:
                        return [statement_bool[0] , False , statement_bool[2]]
                return [end_statement_tmp , True]
            else:
                return [end_statement , True]
    return -1


def check_while(tokens,start):
    token_enum = start + 0
    if tokens[token_enum] == '(':
        start_statement = find_end(tokens, token_enum, char=')')
        result = check_expression(tokens, start=token_enum + 1, end=start_statement)
        if not result[1]:
            return result
        else:
            if tokens[start_statement+1] == '{':
                end_statement = find_end(tokens, start_statement + 1, char='}')
                result = check_statement(tokens=tokens, start=start_statement + 2, end=end_statement)
                if not result[1]:
                    return result
            else:
                end_statement = find_end(tokens, start_statement + 1, char=';')
                result = check_statement(tokens=tokens, start=start_statement + 1, end=end_statement)
                if not result[1]:
                    return result
            return [end_statement , True]
    return -1