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