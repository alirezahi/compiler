# automata = [
#     [-1,-2,-3,-4,-24,16,10,26,0,-5,-6,1,1,2,-7,-13,-10,14,-38,-11,-8],#0
#     [-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,2,-9,-9,-9,-39,-9,-9],
#     [-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,2,-12,3,3,-40,4,-12],
#     [-13,2,6,5,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,2,0,-13,-13,-41,-13,-13],
#     [-14,-14,6,5,-14,-14,-14,-14,-14,-14,-14,-14,-14,-14,-14,-14,-14,-14,-42,-14,-14],
#     [-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,4,-43,4,-15],#5
#     [-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,-16,6,-16,7,7,-44,8,-16],
#     [-17,2,-17,9,-17,-17,-17,-17,-17,-17,-17,-17,-17,-17,-17,0,-17,-17,-45,-17,-17],
#     [-18,2,-18,9,-18,-18,-18,-18,-18,-18,-18,-18,-18,-18,-18,0,-18,-18,-46,-18,-18],
#     [-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,-19,9,-19,-19,8,-47,8,-19],
#     [-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,-20,11,-48,-20,-20],#10
#     [-21,-21,-21,-21,-21,-21,-21,-21,0,10,12,-21,-21,-21,-21,-21,-21,-21,-49,-21,-21],
#     [-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,-22,12,12,-22,-22,13,-50,13,-22],
#     [-23,-23,-23,12,-23,-23,-23,-23,0,-23,-23,-23,-23,-23,-23,13,-23,-23,-51,-23,-23],
#     [-24,-24,-24,-24,15,-24,-24,-24,-24,-24,12,-24,-24,-24,-24,-24,-24,-24,-52,-24,-24],
#     [-25,-25,-25,-25,-25,-25,-25,-25,0,-25,-25,-25,-25,-25,-25,-25,-25,-25,-53,-25,-25],#15
#     [-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,-26,17,-54,-26,-26],
#     [-27,-27,-27,-27,-27,-27,-27,-27,0,16,18,-27,-27,-27,-27,-27,-27,-27,-55,-27,-27],
#     [-28,-28,-28,-28,-28,-28,-28,-28,-28,-28,-28,-28,-28,-28,18,-28,-28,19,-56,20,-28],
#     [-29,-29,22,21,-29,-29,-29,-29,0,-29,-29,-29,-29,-29,-29,-29,-29,-29,-57,-29,-29],
#     [-30,-30,22,21,-30,-30,-30,-30,-30,-30,-30,-30,-30,-30,-30,20,-30,-30,-58,-30,-30],#20
#     [-31,-31,-31,-31,-31,-31,-31,-31,-31,-31,-31,-31,-31,-31,21,-31,-31,20,-59,20,-31],
#     [-32,-32,-32,-32,-32,-32,-32,-32,-32,-32,-32,-32,-32,-32,22,-32,-32,23,-60,24,-32],
#     [-33,18,-33,25,-33,-33,-33,-33,0,-33,-33,-33,-33,-33,-33,23,-33,-33,-61,-33,-33],
#     [-34,18,-34,25,-34,-34,-34,-34,0,-34,-34,-34,-34,-34,-34,24,-34,-34,-62,-34,-34],
#     [-67,-67,-67,-67,-67,-67,-67,-67,-67,-67,-67,-67,-67,-67,25,-67,-67,24,-67,24,-67],#25
#     [-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,-35,27,-63,-35,-35],
#     [-36,-36,-36,-36,-36,-36,-36,-36,-36,26,29,-36,-36,-36,-36,-36,-36,-36,-64,-36,-36],
#     [-37,-37,-37,-37,-37,-37,-37,-37,0,-37,-37,-37,-37,-37,-37,-37,-37,-37,-65,-37,-37],
#     [-66,-66,-66,-66,-66,-66,-66,-66,-66,-66,-66,-66,-66,-66,-66,-66,-66,-66,28,-66,-66]
#     # [p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p],
# ]

from StateMachine import *
from Token import token_expression_num , token_statement_num

tokens_lines = []


def get_line(token_lines,token_number):
    for index,line_num in enumerate(token_lines):
        if line_num > token_number:
            final_result = index+1
            break
    return final_result


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
        current_state = expression_automata[current_state][token_expression_num(tokens[token_enum].strip())]
        if current_state >= 0 :
            token_enum += 1
    if current_state < 0 :
        return [current_state,False,token_enum]
    return [current_state,True,token_enum]


def check_statement(tokens,start=0,end=0):
    current_state = 0
    token_enum = start
    token_end = end
    while token_enum < token_end and current_state >= 0:
        tmp_token = tokens[token_enum].strip()
        tmp_state = current_state
        current_state = statement_automata[current_state][token_statement_num(tmp_token)]
        if current_state == 14 and tmp_state == 12:
            start_tmp = token_enum+1
        if current_state == 7:
            if tmp_state == 15:
                exp_end = find_end(tokens,start_tmp,';')
                if exp_end == -1:
                    return [-1000, False, start_tmp+1]
                result = check_expression(tokens,start=start_tmp,end=exp_end-1)
                if not result[1]:
                    return result
                current_state = 0
                token_enum = exp_end-1
            else:
                exp_end = find_end(tokens, token_enum+1, ';')
                if exp_end == -1:
                    return [-1000, False, token_enum + 1]
                result = check_expression(tokens, start=token_enum+1, end=exp_end-1)
                if not result[1]:
                    return result
                current_state = 0
                token_enum = exp_end-1
        if current_state == 0 and tmp_token == 'if':
            result = check_if(tokens,start=token_enum+1)
            if result[1]:
                token_enum = result[0] + 1
            else:
                return [result[0], False , result[2]]
        elif current_state == 0 and tmp_token == 'while':
            result = check_while(tokens,start=token_enum+1)
            if result[1]:
                token_enum = result[0] + 1
            else:
                return result
        elif current_state >= 0:
            token_enum += 1
    if current_state != 0:
        return [current_state,False , token_enum]
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
                if end_statement == -1 :
                    return [-1000, False , start_statement+1]
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
                    if end_statement_tmp == -1:
                        return [start_statement + 1, False, -1000]
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
                    return [result[0],False , result[2]]
            else:
                end_statement = find_end(tokens, start_statement + 1, char=';')
                if end_statement == -1:
                    return [-1000, False, start+1]
                result = check_statement(tokens=tokens, start=start_statement + 1, end=end_statement)
                if not result[1]:
                    return [result[0], False , result[2]]
            return [end_statement , True]
    return [-1001, False, start]