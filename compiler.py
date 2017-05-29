from check import *

from Syntax import *

with open('test.txt','r') as file:
    parenthes_brace_bool, parenthes_brace_Res, parenthes_brace_Token, problem_type = parenthes_brace_Check(file)
if parenthes_brace_bool:
    with open('test.txt','r') as tmp_file:
        result = check_statement(tmp_file,initiate=True,end=10)
        if result[1]:
            print('Successful')
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