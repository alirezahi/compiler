def no_operation():
    return '0000000000000000'


def halt():
    return '0000000100000000'


def set_z():
    return '0000001000000000'


def clr_z():
    return '0000001100000000' + 'clrz'


def set_c():
    return '0000010000000000'


def clr_c():
    return '0000010100000000' + 'clrc'


def clr_wp():
    return '0000011000000000'


def move_register(Rd, Rs):
    return '0001'+str(Rd)+str(Rs)+'00000000'


def load_address(Rd, Rs):
    return '0010'+str(Rd)+str(Rs)+'00000000' + 'load address'


def store_address(Rd, Rs):
    return '0011'+str(Rd)+str(Rs)+'00000000' + 'store address'


def and_registers(Rd, Rs):
    return '0110'+str(Rd)+str(Rs)+'00000000' + 'and'


def or_registers(Rd, Rs):
    return '0111'+str(Rd)+str(Rs)+'00000000' + 'or'


def not_register(Rd, Rs):
    return '1000'+str(Rd)+str(Rs)+'00000000' + 'not'


def shift_left(Rd, Rs):
    return '1001'+str(Rd)+str(Rs)+'00000000'


def shift_right(Rd, Rs):
    return '1010'+str(Rd)+str(Rs)+'00000000'


def add_registers(Rd, Rs):
    return '1011'+str(Rd)+str(Rs)+'00000000' + 'add'


def subtract_registers(Rd, Rs):
    return '1100'+str(Rd)+str(Rs)+'00000000' + 'sub'


def multiply_registers(Rd, Rs):
    return '1101'+str(Rd)+str(Rs)+'00000000' + 'multiply'


def division_registers(Rd, Rs):
    #It is not complete
    return '1101' + str(Rd) + str(Rs) + '00000000'


def compare_registers(Rd, Rs):
    return '1110'+str(Rd)+str(Rs)+'00000000' + 'compare'


def move_immd_low(Rd, I):
    return '1111'+str(Rd)+'00'+str(I) + 'mil'


def move_immd_high(Rd, I):
    return '1111'+str(Rd)+'01'+str(I) + 'mih'


def save_pc(Rd, I):
    return '1111'+str(Rd)+'10'+str(I)


def jump_address(Rd, I):
    return '1111'+str(Rd)+'11'+str(I) + 'jpa'


def jump_relative(I):
    return '00000111'+str(I) + 'jra'


def branch_if_z(I):
    return '00001000'+str(I) + 'biz'


def branch_if_c(I):
    return '00001001'+str(I) + 'bic'


def add_win_pointer(I):
    return '00001010'+str(I) + 'add_win'