from StateMachine import *
from Token import *
from Binary import *
from SayehInstruction import *
from Semantic import operation_priority

symbol_table = []
identifier_table = []
keyword_table = []
regmem_table = []
number_table = []
operator_table = []
punctuation_table = []

keywords=['true','false','int','bool','char','else','while','if']
operators=['=', '+', '-', '/', '*', '||', '&&', '++', '--', '==', '!=', '>', '<', '>=', '<=', '!', '+=', '-=', '*=', '/=', '%=']
punctuations=['(', ')', '{', '}', ',', ';']

current_wp = 0
last_available_reg = 0
last_available_mem = 1023
last_available_number = 0

operation_stack = []
operand_stack = []

Registers_situation = [0, 0, 0, 0]


def get_next_wp():
    global current_wp, Registers_situation, last_available_mem
    if current_wp == 60:
        for x in operand_stack[-4:]:
            if x[0] is not 'identifier' and x[2] in [0,1,2,3]:
                print(move_immd_low(decimal_to_binary(3, 2), decimal_to_binary(dec_num=last_available_mem, low=True)))
                print(move_immd_high(decimal_to_binary(3, 2), decimal_to_binary(dec_num=last_available_mem, high=True)))
                print(store_address(decimal_to_binary(3, 2), decimal_to_binary(x[2], 2)))
                x[1] = 'mem'
                x[2] = last_available_mem
                last_available_mem -= 1
        Registers_situation = [0, 0, 0, 0]
        print(clr_wp())
        current_wp = 0
    else:
        for x in operand_stack[-4:-1]:
            if x[0] is not 'identifier' and x[2] in [0, 1, 2, 3]:
                print(move_immd_low(decimal_to_binary(3, 2), decimal_to_binary(dec_num=last_available_mem, low=True)))
                print(move_immd_high(decimal_to_binary(3, 2), decimal_to_binary(dec_num=last_available_mem, high=True)))
                print(store_address(decimal_to_binary(3, bin_len=2), decimal_to_binary(x[2], bin_len=2)))
                x[1] = 'mem'
                x[2] = last_available_mem
                last_available_mem -= 1
        Registers_situation = Registers_situation[2:]+[0, 0]
        print(add_win_pointer(decimal_to_binary(2, 8)))
        current_wp += 2


def find_empty_register(number_of_desired_registers):
    if number_of_desired_registers == 1:
        for value in range(len(Registers_situation)):
            if Registers_situation[value] == 0:
                return [True, value]
        return [False]
    elif number_of_desired_registers == 2:
        result = []
        for value in range(len(Registers_situation)):
            if Registers_situation[value] == 0:
                result += [value]
            if len(result) == 2:
                return [True] + result
        return [False]
    return [False]


def calculate():
    first_var = operand_stack.pop()
    second_var = operand_stack.pop()
    reg_add = [0,0]
    for tmp_var in [first_var,second_var]:
        if tmp_var[0] == 'identifier':
            reg_res = find_empty_register(2)
            if not reg_res[0]:
                get_next_wp()
                reg_res = find_empty_register(2)
            print(move_immd_low(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=tmp_var[1][-1], low=True)))
            print(move_immd_high(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=tmp_var[1][-1], high=True)))
            print(load_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(reg_res[1], 2)))
            if tmp_var == first_var:
                reg_add[0] = reg_res[1]
            else:
                reg_add[1] = reg_res[1]
        else:
            if tmp_var[1] == 'reg':
                if tmp_var == first_var:
                    reg_add[0] = tmp_var[2]
                else:
                    reg_add[1] = tmp_var[2]
            elif tmp_var[1] == 'mem':
                reg_res = find_empty_register(2)
                if not reg_res[0]:
                    get_next_wp()
                    reg_res = find_empty_register(2)
                print(move_immd_low(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=tmp_var[2], low=True)))
                print(move_immd_high(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=tmp_var[2], high=True)))
                print(load_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(reg_res[1], 2)))
                if tmp_var == first_var:
                    reg_add[0] = reg_res[1]
                else:
                    reg_add[1] = reg_res[1]
            else:
                reg_res = find_empty_register(2)
                if not reg_res[0]:
                    get_next_wp()
                    reg_res = find_empty_register(2)
                print(move_immd_low(decimal_to_binary(reg_res[1], 2),  decimal_to_binary(dec_num=tmp_var[-1], low=True)))
                print(move_immd_high(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=tmp_var[-1], high=True)))
                if tmp_var == first_var:
                    reg_add[0] = reg_res[1]
                else:
                    reg_add[1] = reg_res[1]
    Registers_situation[min(reg_add)] = 1
    operation = operation_stack.pop()
    if operation == '+':
        print(add_registers(decimal_to_binary(min(reg_add[0],reg_add[1]), 2),decimal_to_binary(max(reg_add[0],reg_add[1]), 2)))
        operand_stack.append(['not_identifier', 'reg',min(reg_add[0],reg_add[1])])
    if operation == '-':
        print(subtract_registers(decimal_to_binary(min(reg_add[0], reg_add[1]), 2), decimal_to_binary(max(reg_add[0], reg_add[1]), 2)))
        operand_stack.append(['not_identifier', 'reg', min(reg_add[0], reg_add[1])])
    if operation == '*':
        print(multiply_registers(decimal_to_binary(min(reg_add[0], reg_add[1]), 2), decimal_to_binary(max(reg_add[0], reg_add[1]), 2)))
        operand_stack.append(['not_identifier', 'reg', min(reg_add[0], reg_add[1])])
    if operation == '/':
        print(division_registers(decimal_to_binary(min(reg_add[0], reg_add[1]), 2), decimal_to_binary(max(reg_add[0], reg_add[1]), 2)))
        operand_stack.append(['not_identifier', 'reg', min(reg_add[0], reg_add[1])])
    return 0


def registers_handle():
    var = operand_stack[-2:]
    needed = 0
    for variable in var:
        if variable[0][0] == 'identifier' or (variable[0][1] is not 'reg'):
            needed += 1
    if needed == 0:
        return
    elif needed == 1:
        if find_empty_register(1)[0]:
            return
        return
    elif needed == 2:
        if find_empty_register(2)[0]:
            return
        return


def register_file_memory():
    return 0


def find_var(searching_identifier):
    for variable in identifier_table:
        if variable[0] == searching_identifier:
            return variable


def set_to_symbol_table(token):
    if token in keywords:
        x = -1
        for z in range(len(keyword_table)):
            if token == keyword_table[z]:
                x = z
                symbol_table.append(['keyword', z])
        if x == -1:
            keyword_table.append(token)
            symbol_table.append(['keyword', len(keyword_table)-1])
    elif token in operators:
        x = -1
        for z in range(len(operator_table)):
            if token == operator_table[z]:
                x = z
                symbol_table.append(['operator', z])
        if x == -1:
            operator_table.append(token)
            symbol_table.append(['operator', len(operator_table) - 1])
    elif token in punctuations:
        x = -1
        for z in range(len(punctuation_table)):
            if token == punctuation_table[z]:
                x = z
                symbol_table.append(['punctutation', z])
        if x == -1:
            punctuation_table.append(token)
            symbol_table.append(['punctutation', len(punctuation_table) - 1])
    else:
        try:
            int(token)
            number_table.append(['s'+str(len(number_table)),token,None,None])
            symbol_table.append(['number',len(number_table) -1])
        except:
            x = -1
            for z in range(len(identifier_table)):
                if token == identifier_table[z][0]:
                    x = z
                    symbol_table.append(['identifier', z])
            if x == -1:
                identifier_table.append([token,None,None])
                symbol_table.append(['identifier', len(identifier_table) - 1])


def find_end(tokens, start_token, char):
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
        elif char == ';':
            finded = False
            while not finded and token_enum<len(tokens):
                if tokens[token_enum] == ';':
                    return token_enum + 1
                token_enum += 1


def store_variable(variable):
    cal_result = operand_stack.pop()
    if cal_result[0] == 'identifier':
        reg_res = find_empty_register(2)
        if not reg_res[0]:
            get_next_wp()
            reg_res = find_empty_register(2)
        print(move_immd_low(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=cal_result[1][-1], low=True)))
        print(move_immd_high(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=cal_result[1][-1], high=True)))
        print(load_address(decimal_to_binary(reg_res[2], 2), decimal_to_binary(reg_res[1], 2)))
        print(move_immd_low(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=find_var(variable)[-1], low=True)))
        print(move_immd_high(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=find_var(variable)[-1], high=True)))
        print(store_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(reg_res[2], 2)))
    else:
        if cal_result[1] == 'reg':
            reg_res = find_empty_register(2)
            if not reg_res[0]:
                get_next_wp()
                reg_res = find_empty_register(2)
            print(move_immd_low(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=find_var(variable)[-1], low=True)))
            print(move_immd_high(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=find_var(variable)[-1], high=True)))
            print(store_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(cal_result[2], 2)))
        elif cal_result[1] == 'None':
            reg_res = find_empty_register(2)
            if not reg_res[0]:
                get_next_wp()
                reg_res = find_empty_register(2)
            print(move_immd_low(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=find_var(variable)[-1], low=True)))
            print(move_immd_high(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=find_var(variable)[-1], high=True)))
            print(move_immd_low(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=cal_result[-1], low=True)))
            print(move_immd_high(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=cal_result[-1], high=True)))
            print(store_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(reg_res[2], 2)))
    return


def check_expression(tokens,start=0,end=0):
    current_state = 0
    token_enum = start + 0
    while token_enum < end:
        current_state = expression_automata[current_state][token_expression_num(tokens[token_enum].strip())]
        token_enum += 1
    return [current_state,True,token_enum]


def check_statement(tokens,start=0,end=0):
    global last_available_mem , last_available_number
    current_state = 0
    token_enum = start
    token_end = end
    while token_enum < token_end:
        tmp_token = tokens[token_enum].strip()
        tmp_state = current_state
        current_state = statement_automata[current_state][token_statement_num(tmp_token)]
        if current_state in [2, 6, 9, 12]:
            last_var = tmp_token
            variable = find_var(tmp_token)
            variable[2] = last_available_mem
            last_available_mem -= 1
        if current_state == 14 and tmp_state == 12:
            start_tmp = token_enum+1

#       handling bool defined scope
        if current_state == 7:
            if tmp_state == 15:
                exp_end = find_end(tokens,start_tmp,';')
                check_expression(tokens,start=start_tmp,end=exp_end-1)
                current_state = 0
                token_enum = exp_end-1
            else:
                exp_end = find_end(tokens, token_enum+1, ';')
                check_expression(tokens, start=token_enum+1, end=exp_end-1)
                current_state = 0
                token_enum = exp_end-1

#       handling_if_scope
        if current_state == 0 and tmp_token == 'if':
            result = check_if(tokens,start=token_enum+1)
            token_enum = result[0] + 1

#       handling_while_scope
        elif current_state == 0 and tmp_token == 'while':
            result = check_while(tokens, start=token_enum+1)
            token_enum = result[0] + 1

#       operation computing
        if current_state == 10 and tmp_token is not '=':
            if tmp_token is not '(':
                while len(operation_stack) > 0 and operation_priority[tmp_token] <= operation_priority[operation_stack[-1]]:
                    calculate()
            operation_stack.append(tmp_token)
        if current_state == 11:
            if tmp_token == ')':
                while operation_stack[-1] is not '(':
                    calculate()
                operation_stack.pop()
            else:
                if isVariable(tmp_token):
                    operand_stack.append(['identifier',find_var(tmp_token)])
                else:
                    operand_stack.append(['not_identifier', 'None', '', tmp_token])
                    last_available_number += 1
        if current_state == 0 and tmp_state == 11:
            while len(operation_stack) > 0:
                calculate()
            store_variable(last_var)
        token_enum += 1


def check_if(tokens,start):
    token_enum = start + 0
    start_statement = find_end(tokens, token_enum, char=')')
    check_expression(tokens, start=token_enum + 1, end=start_statement)
    if tokens[start_statement + 1] == '{':
        end_statement = find_end(tokens, start_statement + 1, char='}')
        check_statement(tokens=tokens, start=start_statement + 2, end=end_statement)
    else:
        end_statement = find_end(tokens, start_statement + 1, char=';')
        check_statement(tokens=tokens, start=start_statement + 1, end=end_statement)
    if len(tokens) > end_statement+1 and tokens[end_statement+1] == 'else':
        if tokens[end_statement + 2] == '{':
            end_statement_tmp = find_end(tokens, end_statement + 2, char='}')
            check_statement(tokens=tokens, start=end_statement + 3, end=end_statement_tmp)
        else:
            end_statement_tmp = find_end(tokens, end_statement + 2, char=';')
            check_statement(tokens=tokens, start=end_statement + 2, end=end_statement_tmp)
        return [end_statement_tmp , True]
    else:
        return [end_statement , True]


def check_while(tokens,start):
    token_enum = start + 0
    start_statement = find_end(tokens, token_enum, char=')')
    check_expression(tokens, start=token_enum + 1, end=start_statement)
    if tokens[start_statement+1] == '{':
        end_statement = find_end(tokens, start_statement + 1, char='}')
        check_statement(tokens=tokens, start=start_statement + 2, end=end_statement)
    else:
        end_statement = find_end(tokens, start_statement + 1, char=';')
        check_statement(tokens=tokens, start=start_statement + 1, end=end_statement)
    return [end_statement , True]

def generate_binary_code(tokens):
    for token in tokens:
        set_to_symbol_table(token)
    check_statement(tokens,end=len(tokens))