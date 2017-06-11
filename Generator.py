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

logical_priority = {'!': 2,'&&': 1,'||': 0}

current_wp = 0
last_available_reg = 0
memory_capacity = 1023
last_available_mem = memory_capacity + 0
last_available_number = 0

operation_stack = []
operand_stack = []

logical_operation_stack = []
logical_operand_stack = []

relational_operator_stack = []

Registers_situation = [0, 0, 0, 0]


def set_address_division(address_number):
    address_result = []
    while address_number >= 255:
        address_result.append(255)
        address_number -= 255
    if address_result is not 0:
        address_result.append(address_number)
    return address_result


def get_next_wp():
    next_wp_result = []
    global current_wp, Registers_situation, last_available_mem
    if current_wp == 60:
        limit_size = -4
        if len(operand_stack) < 4:
            limit_size = -1 * len(operand_stack)
        for x in operand_stack[limit_size:]:
            if x[0] is not 'identifier' and x[2] in [0,1,2,3]:
                next_wp_result.append(move_immd_low(decimal_to_binary(3, 2), decimal_to_binary(dec_num=last_available_mem, low=True)))
                next_wp_result.append(move_immd_high(decimal_to_binary(3, 2), decimal_to_binary(dec_num=last_available_mem, high=True)))
                next_wp_result.append(store_address(decimal_to_binary(3, 2), decimal_to_binary(x[2], 2)))
                x[1] = 'mem'
                x[2] = last_available_mem
                last_available_mem -= 1
        limit_size = -4
        if len(logical_operand_stack) < 4:
            limit_size = -1 * len(logical_operand_stack)
        for x in logical_operand_stack[limit_size:]:
            if x[0] is not 'identifier' and x[2] in [0, 1, 2, 3]:
                next_wp_result.append(move_immd_low(decimal_to_binary(3, 2), decimal_to_binary(dec_num=last_available_mem, low=True)))
                next_wp_result.append(move_immd_high(decimal_to_binary(3, 2), decimal_to_binary(dec_num=last_available_mem, high=True)))
                next_wp_result.append(store_address(decimal_to_binary(3, 2), decimal_to_binary(x[2], 2)))
                x[1] = 'mem'
                x[2] = last_available_mem
                last_available_mem -= 1
        Registers_situation = [0, 0, 0, 0]
        next_wp_result.append(clr_wp())
        current_wp = 0
    else:
        limit_size = -4
        if len(operand_stack)<4:
            limit_size = -1 * len(operand_stack)
        for x in operand_stack[limit_size:]:
            if x[0] is not 'identifier' and x[2] in [0, 1]:
                next_wp_result.append(move_immd_low(decimal_to_binary(3, 2), decimal_to_binary(dec_num=last_available_mem, low=True)))
                next_wp_result.append(move_immd_high(decimal_to_binary(3, 2), decimal_to_binary(dec_num=last_available_mem, high=True)))
                next_wp_result.append(store_address(decimal_to_binary(3, bin_len=2), decimal_to_binary(x[2], bin_len=2)))
                x[1] = 'mem'
                x[2] = last_available_mem
                last_available_mem -= 1
        limit_size = -4
        if len(logical_operand_stack) < 4:
            limit_size = -1 * len(logical_operand_stack)
        for x in logical_operand_stack[limit_size:]:
            if x[0] is not 'identifier' and x[2] in [0, 1]:
                next_wp_result.append(move_immd_low(decimal_to_binary(3, 2), decimal_to_binary(dec_num=last_available_mem, low=True)))
                next_wp_result.append(move_immd_high(decimal_to_binary(3, 2), decimal_to_binary(dec_num=last_available_mem, high=True)))
                next_wp_result.append(store_address(decimal_to_binary(3, bin_len=2), decimal_to_binary(x[2], bin_len=2)))
                x[1] = 'mem'
                x[2] = last_available_mem
                last_available_mem -= 1
        Registers_situation = Registers_situation[2:]+[0, 0]
        next_wp_result.append(add_win_pointer(decimal_to_binary(2, 8)))
        current_wp += 2
    return next_wp_result


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


def logical_calculate():
    logical_cal_res = []
    var_list = []
    first_var = logical_operand_stack.pop()
    var_list.append(first_var)
    if logical_operation_stack[-1] is not '!':
        second_var = logical_operand_stack.pop()
        var_list.append(second_var)
    reg_add = [0, 0]
    for tmp_var in var_list:
        if tmp_var[0] == 'identifier':
            reg_res = find_empty_register(2)
            if not reg_res[0]:
                get_next_wp()
                reg_res = find_empty_register(2)
            if len(var_list) == 1:
                logical_cal_res.append(move_immd_low(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=tmp_var[1][-1], low=True)))
                logical_cal_res.append(move_immd_high(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=tmp_var[1][-1], high=True)))
                logical_cal_res.append(load_address(decimal_to_binary(reg_res[2], 2), decimal_to_binary(reg_res[1], 2)))
            else:
                logical_cal_res.append(move_immd_low(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=tmp_var[1][-1], low=True)))
                logical_cal_res.append(move_immd_high(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=tmp_var[1][-1], high=True)))
                logical_cal_res.append(load_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(reg_res[2], 2)))
            if len(var_list) == 2 and tmp_var == first_var:
                reg_add[0] = reg_res[1]
            elif len(var_list) == 1:
                reg_add = reg_res[1:]
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
                if len(var_list) == 1:
                    logical_cal_res.append(move_immd_low(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=tmp_var[2], low=True)))
                    logical_cal_res.append(move_immd_high(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=tmp_var[2], high=True)))
                    logical_cal_res.append(load_address(decimal_to_binary(reg_res[2], 2), decimal_to_binary(reg_res[1], 2)))
                else:
                    logical_cal_res.append(move_immd_low(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=tmp_var[2], low=True)))
                    logical_cal_res.append(move_immd_high(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=tmp_var[2], high=True)))
                    logical_cal_res.append(load_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(reg_res[2], 2)))
                if len(var_list) == 2 and tmp_var == first_var:
                    reg_add[0] = reg_res[1]
                elif len(var_list) == 1:
                    reg_add = reg_res[1:]
                else:
                    reg_add[1] = reg_res[1]
            else:
                reg_res = find_empty_register(2)
                if not reg_res[0]:
                    get_next_wp()
                    reg_res = find_empty_register(2)
                if len(var_list) == 1:
                    logical_cal_res.append(move_immd_low(decimal_to_binary(reg_res[2], 2),decimal_to_binary(dec_num=tmp_var[-1], low=True)))
                    logical_cal_res.append(move_immd_high(decimal_to_binary(reg_res[2], 2),decimal_to_binary(dec_num=tmp_var[-1], high=True)))
                else :
                    logical_cal_res.append(move_immd_low(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=tmp_var[-1], low=True)))
                    logical_cal_res.append(move_immd_high(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=tmp_var[-1], high=True)))
                if len(var_list) == 2 and tmp_var == first_var:
                    reg_add[0] = reg_res[1]
                elif len(var_list) == 1:
                    reg_add = reg_res[1:]
                else:
                    reg_add[1] = reg_res[1]
    Registers_situation[min(reg_add)] = 1
    operation = logical_operation_stack.pop()
    if operation == '&&':
        logical_cal_res.append(and_registers(decimal_to_binary(dec_num=reg_add[0],bin_len=2),decimal_to_binary(dec_num=reg_add[1],bin_len=2)))
    if operation == '||':
        logical_cal_res.append(or_registers(decimal_to_binary(dec_num=reg_add[0], bin_len=2), decimal_to_binary(dec_num=reg_add[1], bin_len=2)))
    if operation == '!':
        logical_cal_res.append(not_register(decimal_to_binary(dec_num=reg_add[0], bin_len=2), decimal_to_binary(dec_num=reg_add[1], bin_len=2)))
    logical_operand_stack.append(['not_identifier', 'reg', min(reg_add)])
    return logical_cal_res


def calculate(relational_operation=False):
    calculate_res = []
    first_var = operand_stack.pop()
    second_var = operand_stack.pop()
    reg_add = [0, 0]
    for tmp_var in [first_var, second_var]:
        if tmp_var[0] == 'identifier':
            reg_res = find_empty_register(2)
            if not reg_res[0]:
                get_next_wp()
                reg_res = find_empty_register(2)
            calculate_res.append(move_immd_low(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=tmp_var[1][-1], low=True)))
            calculate_res.append(move_immd_high(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=tmp_var[1][-1], high=True)))
            calculate_res.append(load_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(reg_res[1], 2)))
            if tmp_var == first_var:
                reg_add[0] = reg_res[1]
            else:
                reg_add[1] = reg_res[1]
            Registers_situation[reg_res[1]] = 1
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
                calculate_res.append(move_immd_low(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=tmp_var[2], low=True)))
                calculate_res.append(move_immd_high(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=tmp_var[2], high=True)))
                calculate_res.append(load_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(reg_res[1], 2)))
                if tmp_var == first_var:
                    reg_add[0] = reg_res[1]
                else:
                    reg_add[1] = reg_res[1]
                Registers_situation[reg_res[1]] = 1
            else:
                reg_res = find_empty_register(2)
                if not reg_res[0]:
                    get_next_wp()
                    reg_res = find_empty_register(2)
                calculate_res.append(move_immd_low(decimal_to_binary(reg_res[1], 2),  decimal_to_binary(dec_num=tmp_var[-1], low=True)))
                calculate_res.append(move_immd_high(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=tmp_var[-1], high=True)))
                if tmp_var == first_var:
                    reg_add[0] = reg_res[1]
                else:
                    reg_add[1] = reg_res[1]
                Registers_situation[reg_res[1]] = 1
    Registers_situation[min(reg_add)] = 1
    if relational_operation:
        operation = relational_operator_stack.pop()
        calculate_res.append(clr_c())
        calculate_res.append(clr_z())
        if operation == '>':
            calculate_res.append(compare_registers(decimal_to_binary(reg_add[1], 2), decimal_to_binary(reg_add[0], 2)))
            calculate_res.append(branch_if_c(decimal_to_binary(dec_num=4,bin_len=8)))
            calculate_res.append(move_immd_low(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=0, low=True)))
            calculate_res.append(move_immd_high(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=0, high=True)))
            calculate_res.append(jump_relative(decimal_to_binary(dec_num=3,bin_len=8)))
            calculate_res.append(move_immd_low(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=1, low=True)))
            calculate_res.append(move_immd_high(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=1, high=True)))
        if operation == '>=':
            calculate_res.append(compare_registers(decimal_to_binary(reg_add[0], 2), decimal_to_binary(reg_add[1], 2)))
            calculate_res.append(branch_if_c(decimal_to_binary(dec_num=4, bin_len=8)))
            calculate_res.append(move_immd_low(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=1, low=True)))
            calculate_res.append(move_immd_high(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=1, high=True)))
            calculate_res.append(jump_relative(decimal_to_binary(dec_num=3, bin_len=8)))
            calculate_res.append(move_immd_low(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=0, low=True)))
            calculate_res.append(move_immd_high(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=0, high=True)))
        if operation == '<':
            calculate_res.append(compare_registers(decimal_to_binary(reg_add[0], 2), decimal_to_binary(reg_add[1], 2)))
            calculate_res.append(branch_if_c(decimal_to_binary(dec_num=4, bin_len=8)))
            calculate_res.append(move_immd_low(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=0, low=True)))
            calculate_res.append(move_immd_high(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=0, high=True)))
            calculate_res.append(jump_relative(decimal_to_binary(dec_num=3, bin_len=8)))
            calculate_res.append(move_immd_low(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=1, low=True)))
            calculate_res.append(move_immd_high(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=1, high=True)))
        if operation == '<=':
            calculate_res.append(compare_registers(decimal_to_binary(reg_add[1], 2), decimal_to_binary(reg_add[0], 2)))
            calculate_res.append(branch_if_c(decimal_to_binary(dec_num=4, bin_len=8)))
            calculate_res.append(move_immd_low(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=1, low=True)))
            calculate_res.append(move_immd_high(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=1, high=True)))
            calculate_res.append(jump_relative(decimal_to_binary(dec_num=3, bin_len=8)))
            calculate_res.append(move_immd_low(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=0, low=True)))
            calculate_res.append(move_immd_high(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=0, high=True)))
        if operation == '==':
            calculate_res.append(compare_registers(decimal_to_binary(reg_add[0], 2), decimal_to_binary(reg_add[1], 2)))
            calculate_res.append(branch_if_z(decimal_to_binary(dec_num=3, bin_len=8)))
            calculate_res.append(move_immd_low(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=0, low=True)))
            calculate_res.append(move_immd_high(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=0, high=True)))
            calculate_res.append(jump_relative(decimal_to_binary(dec_num=3, bin_len=8)))
            calculate_res.append(move_immd_low(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=1, low=True)))
            calculate_res.append(move_immd_high(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=1, high=True)))
        if operation == '!=':
            calculate_res.append(compare_registers(decimal_to_binary(reg_add[0], 2), decimal_to_binary(reg_add[1], 2)))
            calculate_res.append(branch_if_z(decimal_to_binary(dec_num=3, bin_len=8)))
            calculate_res.append(move_immd_low(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=1, low=True)))
            calculate_res.append(move_immd_high(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=1, high=True)))
            calculate_res.append(jump_relative(decimal_to_binary(dec_num=3, bin_len=8)))
            calculate_res.append(move_immd_low(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=0, low=True)))
            calculate_res.append(move_immd_high(decimal_to_binary(min(reg_add), 2), decimal_to_binary(dec_num=0, high=True)))
        logical_operand_stack.append(['not_identifier', 'reg', min(reg_add)])
    else:
        operation = operation_stack.pop()
        if operation in ['+','+=']:
            calculate_res.append(add_registers(decimal_to_binary(min(reg_add[0],reg_add[1]), 2),decimal_to_binary(max(reg_add[0],reg_add[1]), 2)))
        if operation in ['-','-=']:
            calculate_res.append(subtract_registers(decimal_to_binary(min(reg_add[0], reg_add[1]), 2), decimal_to_binary(max(reg_add[0], reg_add[1]), 2)))
        if operation in ['*','*=']:
            calculate_res.append(multiply_registers(decimal_to_binary(min(reg_add[0], reg_add[1]), 2), decimal_to_binary(max(reg_add[0], reg_add[1]), 2)))
        if operation in ['/','/=']:
            calculate_res.append(division_registers(decimal_to_binary(min(reg_add[0], reg_add[1]), 2), decimal_to_binary(max(reg_add[0], reg_add[1]), 2)))
        operand_stack.append(['not_identifier', 'reg', min(reg_add[0], reg_add[1])])
    return calculate_res


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


def store_variable(variable, store_boolean=False):
    storing_result = []
    if store_boolean:
        cal_result = logical_operand_stack.pop()
    else:
        cal_result = operand_stack.pop()
    if cal_result[0] == 'identifier':
        reg_res = find_empty_register(2)
        if not reg_res[0]:
            get_next_wp()
            reg_res = find_empty_register(2)
        storing_result.append(move_immd_low(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=cal_result[1][-1], low=True)))
        storing_result.append(move_immd_high(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=cal_result[1][-1], high=True)))
        storing_result.append(load_address(decimal_to_binary(reg_res[2], 2), decimal_to_binary(reg_res[1], 2)))
        storing_result.append(move_immd_low(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=find_var(variable)[-1], low=True)))
        storing_result.append(move_immd_high(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=find_var(variable)[-1], high=True)))
        storing_result.append(store_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(reg_res[2], 2)))
    else:
        if cal_result[1] == 'reg':
            reg_res = find_empty_register(2)
            if not reg_res[0]:
                get_next_wp()
                reg_res = find_empty_register(2)
            storing_result.append(move_immd_low(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=find_var(variable)[-1], low=True)))
            storing_result.append(move_immd_high(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=find_var(variable)[-1], high=True)))
            storing_result.append(store_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(cal_result[2], 2)))
        elif cal_result[1] == 'None':
            reg_res = find_empty_register(2)
            if not reg_res[0]:
                get_next_wp()
                reg_res = find_empty_register(2)
            storing_result.append(move_immd_low(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=find_var(variable)[-1], low=True)))
            storing_result.append(move_immd_high(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=find_var(variable)[-1], high=True)))
            storing_result.append(move_immd_low(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=cal_result[-1], low=True)))
            storing_result.append(move_immd_high(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=cal_result[-1], high=True)))
            storing_result.append(store_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(reg_res[2], 2)))
    return storing_result


def check_expression(tokens,start=0,end=0):
    expression_res = []
    global last_available_mem
    current_state = 0
    token_enum = start + 0
    while token_enum < end:
        tmp_token = tokens[token_enum].strip()
        tmp_state = current_state
        current_state = expression_automata[current_state][token_expression_num(tokens[token_enum].strip())]
        #computing section
        if current_state in [4, 7]:
            if tmp_token is not '(':
                while len(operation_stack) > 0 and operation_priority[tmp_token] <= operation_priority[operation_stack[-1]]:
                    expression_res += calculate()
            operation_stack.append(tmp_token)
        if current_state in [2, 6]:
            if tmp_token == ')':
                while operation_stack[-1] is not '(':
                    expression_res += calculate()
                operation_stack.pop()
            else:
                if isVariable(tmp_token):
                    operand_stack.append(['identifier', find_var(tmp_token)])
                else:
                    operand_stack.append(['not_identifier', 'None', '', tmp_token])
        if current_state == 5:
            relational_operator_stack.append(tmp_token)
            while len(operation_stack) > 0:
                expression_res += calculate()
            #felan bahman
        if current_state == 0 and tmp_state == 0 and tmp_token == '!':
            logical_operation_stack.append(tmp_token)
        if (current_state == 6 and token_enum == end-1) or (current_state == 0 and tmp_state == 6):
            while len(operation_stack) > 0:
                expression_res += calculate()
            expression_res += calculate(relational_operation=True)
            #felan bahman and then compare
        if current_state == 6 and token_enum == end-1:
            while len(logical_operation_stack) > 0:
                expression_res += logical_calculate()
        if current_state == 0 and tmp_state == 6:
            if len(logical_operation_stack) > 0 and logical_priority[tmp_token] < logical_priority[logical_operation_stack[-1]]:
                while logical_priority[tmp_token] < logical_priority[logical_operation_stack[-1]]:
                    expression_res += logical_calculate()
            logical_operation_stack.append(tmp_token)
        token_enum += 1
    return expression_res


def check_statement(tokens,start=0,end=0):
    statement_res = []
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
                statement_res += check_expression(tokens,start=start_tmp,end=exp_end-1)
                current_state = 0
                token_enum = exp_end-1
            else:
                exp_end = find_end(tokens, token_enum+1, ';')
                statement_res += check_expression(tokens, start=token_enum+1, end=exp_end-1)
                current_state = 0
                token_enum = exp_end-1
            statement_res += store_variable(last_var, store_boolean=True)

#       handling_if_scope
        if current_state == 0 and tmp_token == 'if':
            result, ass_res = check_if(tokens,start=token_enum+1)
            token_enum = result[0] + 1
            statement_res += ass_res

#       handling_while_scope
        elif current_state == 0 and tmp_token == 'while':
            result, ass_res = check_while(tokens, start=token_enum+1)
            token_enum = result[0] + 1
            statement_res += ass_res

#       operation computing
        if current_state == 10 and tmp_token is not '=':
            if tmp_token is not '(':
                while len(operation_stack) > 0 and operation_priority[tmp_token] <= operation_priority[operation_stack[-1]]:
                    statement_res += calculate()
            operation_stack.append(tmp_token)
        if current_state == 11:
            if tmp_token == ')':
                while operation_stack[-1] is not '(':
                    statement_res += calculate()
                operation_stack.pop()
            else:
                if isVariable(tmp_token):
                    operand_stack.append(['identifier',find_var(tmp_token)])
                else:
                    operand_stack.append(['not_identifier', 'None', '', tmp_token])
        if current_state == 0 and tmp_state == 11:
            while len(operation_stack) > 0:
                statement_res += calculate()
            statement_res += store_variable(last_var)
        token_enum += 1
    return statement_res


def check_if(tokens, start):
    if_res = []
    token_enum = start + 0
    start_statement = find_end(tokens, token_enum, char=')')
    if_res += check_expression(tokens, start=token_enum + 1, end=start_statement)
    reg_res = find_empty_register(2)
    if not reg_res[0]:
        get_next_wp()
        reg_res = find_empty_register(2)
    if tokens[start_statement + 1] == '{':
        end_statement = find_end(tokens, start_statement + 1, char='}')
        if_res_tmp = check_statement(tokens=tokens, start=start_statement + 2, end=end_statement)
    else:
        end_statement = find_end(tokens, start_statement + 1, char=';')
        if_res_tmp = check_statement(tokens=tokens, start=start_statement + 1, end=end_statement)
        end_statement -= 1
    len_statements_if = len(if_res_tmp)
    if_res.append(move_immd_low(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=memory_capacity, low=True)))
    if_res.append(move_immd_high(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=memory_capacity, high=True)))
    if_res.append(load_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(reg_res[2], 2)))
    if_res.append(compare_registers(decimal_to_binary(reg_res[1] - 1, 2), decimal_to_binary(reg_res[1], 2)))
    if_res.append(branch_if_c(decimal_to_binary(dec_num=2, bin_len=8)))
    if_res.append(jump_relative(decimal_to_binary(dec_num=len_statements_if+1,bin_len=8)))
    if_res += if_res_tmp
    if len(tokens) > end_statement+1 and tokens[end_statement+1] == 'else':
        if tokens[end_statement + 2] == '{':
            end_statement_tmp = find_end(tokens, end_statement + 2, char='}')
            if_res += check_statement(tokens=tokens, start=end_statement + 3, end=end_statement_tmp)
        else:
            end_statement_tmp = find_end(tokens, end_statement + 2, char=';')
            if_res += check_statement(tokens=tokens, start=end_statement + 2, end=end_statement_tmp)
        return [end_statement_tmp, True], if_res
    else:
        return [end_statement, True], if_res


def check_while(tokens, start):
    while_res = []
    token_enum = start + 0
    start_statement = find_end(tokens, token_enum, char=')')
    while_res_tmp_exp = check_expression(tokens, start=token_enum + 1, end=start_statement)
    while_res += while_res_tmp_exp
    reg_res = find_empty_register(2)
    if not reg_res[0]:
        get_next_wp()
        reg_res = find_empty_register(2)
    if tokens[start_statement+1] == '{':
        end_statement = find_end(tokens, start_statement + 1, char='}')
        while_res_tmp = check_statement(tokens=tokens, start=start_statement + 2, end=end_statement)
    else:
        end_statement = find_end(tokens, start_statement + 1, char=';')
        while_res_tmp = check_statement(tokens=tokens, start=start_statement + 1, end=end_statement)
    len_statements_while = len(while_res_tmp)
    while_res.append(move_immd_low(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=memory_capacity, low=True)))
    while_res.append(move_immd_high(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=memory_capacity, high=True)))
    while_res.append(load_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(reg_res[2], 2)))
    while_res.append(compare_registers(decimal_to_binary(reg_res[1] - 1, 2), decimal_to_binary(reg_res[1], 2)))
    while_res.append(branch_if_c(decimal_to_binary(dec_num=2, bin_len=8)))
    while_res.append(jump_relative(decimal_to_binary(dec_num=len_statements_while + 1, bin_len=8)))
    while_res += while_res_tmp
    reg_res = find_empty_register(2)
    if not reg_res[0]:
        get_next_wp()
        reg_res = find_empty_register(2)
    address_moving = set_address_division(int((memory_capacity-len(while_res_tmp_exp)-len(while_res_tmp))))
    while_res.append(save_pc(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=address_moving[0], bin_len=8)))
    for i in address_moving[1:-1]:
        while_res.append(move_immd_low(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=i, low=True)))
        while_res.append(move_immd_high(decimal_to_binary(reg_res[2], 2), decimal_to_binary(dec_num=i, high=True)))
        while_res.append(add_registers(decimal_to_binary(dec_num=reg_res[1],bin_len=2),decimal_to_binary(dec_num=reg_res[2],bin_len=2)))
    while_res.append(jump_address(decimal_to_binary(reg_res[1], 2), decimal_to_binary(dec_num=address_moving[-1],bin_len=8)))
    return [end_statement, True], while_res


def generate_binary_code(tokens):
    resulted_assembly_code = []
    global last_available_mem
    resulted_assembly_code.append(move_immd_low(decimal_to_binary(0, 2), decimal_to_binary(dec_num=1, low=True)))
    resulted_assembly_code.append(move_immd_high(decimal_to_binary(0, 2), decimal_to_binary(dec_num=1, high=True)))
    resulted_assembly_code.append(move_immd_low(decimal_to_binary(1, 2), decimal_to_binary(dec_num=last_available_mem, low=True)))
    resulted_assembly_code.append(move_immd_high(decimal_to_binary(1, 2), decimal_to_binary(dec_num=last_available_mem, high=True)))
    resulted_assembly_code.append(store_address(decimal_to_binary(dec_num=0, bin_len=2), decimal_to_binary(dec_num=1, bin_len=2)))
    last_available_mem -= 1
    for token in tokens:
        set_to_symbol_table(token)
    resulted_assembly_code += check_statement(tokens, end=len(tokens))
    z = 0
    for i in resulted_assembly_code:
        print(z,end=' ')
        z += 1
        print(i)