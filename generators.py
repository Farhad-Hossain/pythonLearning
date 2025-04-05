import sys
def my_generators():
    for i in range(0, 100, 2):
        yield i

g = my_generators()
# print(next(g))
# print(next(g))
# print(next(g))


# print( sum(g) )
# print( sorted(g) )



# def countdown(num):
#     print("Starting")
#     while num > 0:
#         yield num
#         num -= 1

# cd = countdown(5)
# print(next(cd))
# print(next(cd))




def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1

    # print(nums)
    return nums

print( sum(firstn(10)) )




def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print( sum(firstn_generator(10)) )



print( sys.getsizeof(firstn(1000)) )
print( sys.getsizeof(firstn_generator(1000)) )




def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
    
print( list(fibonacci(100)) )



g = (i for i in range(100) if i % 2 == 0)
for i in g:
    print(i)