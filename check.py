def commaCheck(file_input):
    # It checks whether the number of open and close parentheses are equal or not
    line_number = 1
    comma_counter = 0
    tmp_token = ''
    for line in file_input:
        for token in line.replace('\t',' ').split(' '):
            if token.strip() == '(':
                comma_counter +=1
            elif token.strip() == ')':
                comma_counter -= 1
                if comma_counter<0:
                    return False,str(line_number),str(tmp_token)
            else:
                tmp_token = token
        line_number += 1
    if comma_counter>0:
        return False,'0','1'
    return True,[],[]
