# map
def return_square(x):
    return x * x
my_list = list(map(return_square, (1,2,3)))
print(my_list)

# filter
def even_or_not(x):
    return x % 2 == 0
all_evens = list(filter(even_or_not, (1,2,3,4,5,6,7,8,9)))

print(all_evens)
print('----')
# bool
print(bool(1))
print(bool(0))
print(bool(False))
print(bool("False"))
print(bool([]))
print('-----')

# int
print(int(0o10))
print(int('0101', 2))
print(int('0101', 8))
print(int('0101', 16))
print(int(101.909))
print(int(3.14))
print(int(-3.14))

print(int('-100'))
print(int('+100'))
print(int('100'))

# float
print(float(1))
print(float(1.34))
print(float('1.24'))
print(float(-2))
print(float('+nan'))
print(float('-inf'))
print('- - - - ')

# complex
print(complex())
print(complex(1))
print(complex(1, 2))
print(complex(2.34, 7.5))
print(complex('1+5j'))
print('----')

# bin
print(bin(23))
print(bin(1024))
print('---')

# oct
print(oct(23))
print(oct(256))
print('---')

# hex
print(hex(23))
print(hex(-30))
print('---')

# abs
print(abs(-1))
print(abs(1))
print(abs(0))
print(abs(3.14))
print(abs(3+2j))
print('-----')

# pow
print(pow(2,3))
print(pow(2, -2))
print(pow(10,2,9))
print('----')

# round
print(round(2.333, 1))
print(round(2.675, 2))
print('---')

# divmod
print(divmod(10,3)[0])
print('---')

# chr
print(chr(65))
print(chr(97))
print(''.join([chr(c) for c in range(65, 91)]))
print('---')

# ord
print(ord('a'))
print(ord('A'))
print(ord(u'a'))

# format
print(format(3.14, '0>5'))
print(format(12873682173, ','))