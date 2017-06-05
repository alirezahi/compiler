def decimal_to_binary(dec_num):
    number = abs(dec_num)
    binary = ''
    while number >= 1:
        binary = str(number%2)+str(binary)
        number = int(number/2)
    return binary


def binary_to_decimal(bin_num):
    binary = str(bin_num)
    power = len(bin_num) - 1
    decimal = 0
    for digit in binary:
        decimal += (2**power) * int(digit)
        power -= 1
    return str(decimal)