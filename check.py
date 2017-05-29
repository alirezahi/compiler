def parenthes_brace_Check(file_input):
    # It checks whether the number of open and close parentheses or braces are equal or not
    line_number = 1
    comma_counter = 0
    brace_counter = 0
    tmp_token = ''
    for line in file_input:
        for token in line.replace('\t',' ').split(' '):
            if token.strip() == '(':
                comma_counter +=1
            elif token.strip() == ')':
                comma_counter -= 1
                if comma_counter<0:
                    return False,str(line_number),str(tmp_token),'parenthese'
            elif token.strip() == '{':
                brace_counter += 1
            elif token.strip() == '}':
                brace_counter -= 1
                if brace_counter <0:
                    return False,str(line_number),str(tmp_token),'brace'
            tmp_token = token
        line_number += 1
    if comma_counter > 0:
        return False,'0','1','parenthes'
    elif brace_counter > 0:
        return False,'0','1','brace'
    return True,[],[],[]