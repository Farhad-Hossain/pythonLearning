# x = int(input("Please enter an integer : "))
# if x < 0:
# 	x = 0
# 	print("Negative changed to 0")
# elif x == 0:
# 	print("X is zero")
# elif x == 1:
# 	print("Single")
# else:
# 	print("More")




# for loop
fruits = ["Mango", 'Jackfruite', 'PinaApple']
for fruit in fruits:
	print(fruit, '-', len(fruit))


for i in range(100):
	print(i)

list = list(range(0, 30, 3))
for l in list :
	print(l)

a = ['mary', 'had', 'a', 'little', 'lamp']
for i in range(len(a)): 
	print(i, a[i])


print(sum(range(100)))