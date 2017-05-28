from check import *

from Syntax import *

with open('test.txt','r') as file:
    parenthes_brace_bool, parenthes_brace_Res, parenthes_brace_Token, problem_type = parenthes_brace_Check(file)
if parenthes_brace_bool:
    with open('test.txt','r') as tmp_file:
        check_statement(tmp_file)
else:
    if parenthes_brace_Res == '0':
        if problem_type == 'parenthes':
            print('Error : Parenthes hasn\'t been closed somewhere')
        else:
            print('Error : Brace hasn\'t been closed somewhere')
    else:
        if problem_type == 'parenthes':
            print('Error : Parenthese Not Expected ' + parenthes_brace_Res + ' after \"' + parenthes_brace_Token +'\" - line ' + parenthes_brace_Res)
        else:
            print('Error : Brace Not Expected ' + parenthes_brace_Res + ' after \"' + parenthes_brace_Token +'\" - line ' + parenthes_brace_Res)