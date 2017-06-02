from check import *

from Syntax import *

from Semantic import sem_check

tokens_lines = []

with open('test.txt','r') as file:
    parenthes_brace_bool, parenthes_brace_Res, parenthes_brace_Token, problem_type = parenthes_brace_Check(file)
if parenthes_brace_bool:
    with open('test.txt','r') as tmp_file:
        tokens = []
        line_num = 0
        for line in tmp_file:
            for token in line.replace('\t', ' ').replace('\n', '').split(' '):
                if token.strip() != '':
                    tokens.append(token.strip())
                    line_num += 1
            tokens_lines.append(line_num)
        tokens_number = len(tokens)
        result = check_statement(tokens,end=tokens_number)
        if result[1]:
            print('Successful')
            print(sem_check(tokens,start=0,end=tokens_number))
        else:
            print('Line '+ str(get_line(tokens_lines,result[2])) +' : Error ')
else:
    if parenthes_brace_Res == '0':
        if problem_type == 'parenthes':
            print('Error : Parentheses hasn\'t been closed somewhere')
        else:
            print('Error : Brace hasn\'t been closed somewhere')
    else:
        if problem_type == 'parenthes':
            print('Line '+parenthes_brace_Res+' - Error : Parentheses Not Expected ' + parenthes_brace_Res + ' after \"' + parenthes_brace_Token +'\"')
        else:
            print('Line '+parenthes_brace_Res+' - Error : Brace Not Expected ' + parenthes_brace_Res + ' after \"' + parenthes_brace_Token +'\"')