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
expression_automata = [
    [0,-1,-1,-1,0,-1,1,10,3,2,-1],
    [-2,0,-2,-2,-2,1,-2,-2,-2,-2,-2],
    [-3,-3,5,4,-3,2,-3,-3,-3,-3,-3],
    [-4,0,5,4,-4,3,-4,-4,-4,-4,-4],
    [-5,-5,-5,-5,4,-5,-5,-5,2,2,-5],
    [5,-6,-6,-6,5,-6,8,-6,7,6,-1],
    [-7,0,-7,9,-7,6,-7,-7,-7,-7,-7],
    [-8,0,-8,9,-4,7,-8,-8,-8,-8,-8],
    [-9,0,-9,-9,-9,8,-9,-9,-9,-9,-9],
    [-10,-10,-10,-10,9,-10,-10,-10,6,6,-10],
    [-12,-12,11,-12,-12,10,-12,-12,-12,-12,-12],
    [-13,-13,-13,-13,-13,-13,-13,12,12,-13,-13],
    [-14,0,-14,-14,-14,12,-14,-14,-14,-14,-14]
]

statement_automata = [
    [-1,-1,-1,5,8,1,-1,-1,-1,0,0,-1,-1,12,-1,-1,-1],#0
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,2,-1,-1,-1],
    [-2,-2,-2,-2,-2,-2,0,1,3,-2,-2,-2,-2,-2,-2,-2,-2],
    [-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,3,-3,4,4,-3,-3],
    [-4,-4,-4,-4,-4,-4,0,-4,-4,-4,-4,-4,4,6,-4,-4,-4],
    [-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,-5,6,-5,-5,-5],#5
    [-6,-6,-6,-6,-6,-6,-6,5,7,-6,-6,-6,-6,-6,-6,-6,-6],
    [-7,-7,-7,-7,-7,-7,0,-7,-7,-7,-7,-7,-7,-7,-7,-7,-7],
    [-8,-8,-8,-8,-8,-8,-8,-8,-8,-8,-8,-8,-8,9,-8,-8,-8],
    [-9,-9,-9,-9,-9,-9,0,8,10,-9,-9,-9,-9,-9,-9,-9,-9],
    [-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,-10,10,-10,11,-10,11,-10],#10
    [-11,10,-11,-11,-11,-11,0,-11,-11,-11,-11,-11,11,-11,-11,-11,-11],
    [10,-12,13,-12,-12,-12,-12,-12,10,-12,-12,-12,-12,-12,-12,-12,-12],
    [-13,-13,-13,-13,-13,-13,0,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13]
]

tokens_lines = []

from Token import token_expression_num , token_statement_num

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
        if char == ';':
            finded = False
            while not finded:
                if tokens[token_enum] == ';':
                    return token_enum + 1
                token_enum += 1
            return -1

def check_expression(tokens,start=0,end=0):
    current_state = 0
    token_enum = start + 0
    while token_enum < end and current_state >= 0:
        current_state = expression_automata[current_state][token_expression_num(tokens[token_enum].strip())]
        print(current_state)
        if current_state >= 0 :
            token_enum += 1
    if current_state < 0 :
        return [current_state,False,token_enum]
    return [current_state,True,token_enum]

def check_statement(input_tokens,initiate=False,start=0,end=0):
    current_state = 0
    if initiate:
        tokens = []
        line_num = 0
        for line in input_tokens:
            for token in line.replace('\t', ' ').replace('\n', '').split(' '):
                if token.strip() != '':
                    tokens.append(token.strip())
                    line_num += 1
            tokens_lines.append(line_num)
        tokens_number = len(tokens)
        token_enum = start
        token_end = tokens_number + 0
    else:
        tokens = input_tokens
        token_enum = start
        token_end = end
    while token_enum < token_end and current_state >= 0:
        tmp_token = tokens[token_enum].strip()
        current_state = statement_automata[current_state][token_statement_num(tmp_token)]
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
                return [result[0],False , result[2]]
        elif current_state >= 0:
            token_enum += 1
    if current_state < 0:
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
                statement_bool = check_statement(input_tokens=tokens, start=start_statement + 2, end=end_statement)
                if statement_bool[0] < 0:
                    return [statement_bool[0] , False , statement_bool[2]]
            else:
                end_statement = find_end(tokens, start_statement + 1, char=';')
                statement_bool = check_statement(input_tokens=tokens, start=start_statement + 1, end=end_statement)
                if statement_bool[0] < 0:
                    return [statement_bool[0] , False , statement_bool[2]]
            if len(tokens) > end_statement+1 and tokens[end_statement+1] == 'else':
                if tokens[end_statement + 2] == '{':
                    end_statement_tmp = find_end(tokens, end_statement + 2, char='}')
                    statement_bool = check_statement(input_tokens=tokens, start=end_statement + 3, end=end_statement_tmp)
                    if statement_bool[0] < 0:
                        return [statement_bool[0] , False , statement_bool[2]]
                else:
                    end_statement_tmp = find_end(tokens, end_statement + 2, char=';')
                    statement_bool = check_statement(input_tokens=tokens, start=end_statement + 2, end=end_statement_tmp)
                    if statement_bool[0] < 0:
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
                result = check_statement(input_tokens=tokens, start=start_statement + 2, end=end_statement)
                if not result[1]:
                    return [result[0],False , result[2]]
            else:
                end_statement = find_end(tokens, start_statement + 1, char=';')
                result = check_statement(input_tokens=tokens, start=start_statement + 1, end=end_statement)
                if not result[1]:
                    return [result[0], False , result[2]]
            return [end_statement , True]
    return -1