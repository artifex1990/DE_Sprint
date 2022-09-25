def bin_mul(bin1, bin2):
    base_type = 2
    
    return bin(int(bin1, base_type) * int(bin2, base_type)).replace("0b", "")

print(bin_mul("111", "101"))