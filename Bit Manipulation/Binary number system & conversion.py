from unicodedata import decimal


def int2BinaryConversion(num):
    res = ''
    while num>0:
        if num%2==0:
             res+='0'
        else:
            res+='1'
        num = num//2
    res = res[::-1]
    return res

    # return bin(num)[2:]

def binary2Decimal(binary):
    res = 0
    n = len(binary)
    for b in binary:
        res += (int(b)*2**(n-1))
        n -= 1
    return res
    # return int(binary)

print(int2BinaryConversion(12))
print(binary2Decimal("1100"))

