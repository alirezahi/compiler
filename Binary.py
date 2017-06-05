def decimal_to_binary(dec_num='', bin_len=16,low=False,high=False):
    number = abs(int(dec_num))
    binary = ''
    while number >= 1:
        binary = str(number % 2)+str(binary)
        number = int(number/2)
    len_digit = len(binary)
    for i in range(bin_len-len_digit):
        binary = '0'+binary
    if low:
        return binary[8:]
    if high:
        return binary[:8]
    return binary


def binary_to_decimal(bin_num):
    binary = str(bin_num)
    power = len(bin_num) - 1
    decimal = 0
    for digit in binary:
        decimal += (2**power) * int(digit)
        power -= 1
    return str(decimal)

def complement(bin_num,sec_num):
    bin_num= str(bin_num)
    bin_len = len(bin_num) - 1
    return 2**bin_len-int(binary_to_decimal(bin_num))+int(sec_num)