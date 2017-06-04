def decimal_to_binary(dec_num):
    number = abs(dec_num)
    binary = ''
    while number >= 1:
        binary = str(number%2)+str(binary)
        number = int(number/2)
    return binary
