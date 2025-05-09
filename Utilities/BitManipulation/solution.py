def print_bin(binary):
    print("{:08b}".format(binary))
    
def xor_bin(one, two):
    return one ^ two
    
def or_bin(one, two):
    return one | two
    
def and_bin(one, two):
    return one & two
    
one = 0b00001111
two = 0b11110000

print_bin(~one)

ans = or_bin(one, two)
print_bin(ans)