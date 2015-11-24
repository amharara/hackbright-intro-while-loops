# #i=0
# #while (i<=20):
# 	print i,
# 	i=i+1

# i=0
# while (i<=20):
# 	if (i == 13):
# 		print "hello"
# 		i=i+1
# 	elif (i !=13):
# 		print i,
# 		i=i+1


# i=0
# while (i<=10):
# 	print i*10,
# 	i=i+1	

# i=0
# while (i<=10):
# 	if (i%2 != 0):
# 		print i,
# 	i= i + 1

# i=10
# while (i<=10):
# 	if i<0:
# 		break
# 	print i,
# 	i= i - 1

# i=10
# while (i<=10):
# 	if i==0:
# 		print "Blastoff"
# 	elif i<0:
# 		break
# 	elif i!=0:
# 		print i,
# 	i= i - 1

# fruits = ["apples", "oranges", "bananas"]
# index = 0
# while (index <len(fruits)):
# 	print fruits[index], 
# 	index = index + 1
# def sum_nums(num):
# 	i=0
# 	x=0
# 	while(i<num):
# 		x= x + i
# 		i=i+1
# 	print x,


# sum_nums(5)

# def sum_nums(num):
# 	i=0
# 	x=0
# 	while(i<=num):
# 		x= x + i
# 		i=i+1
# 	print x,


# sum_nums(3)

# def sum_nums2(num):
# 	i=0
# 	x=0
# 	if num>0:
# 		while(i<=num):
# 			x= x + i
# 			i=i+1
# 		print x,
# 	elif num<0:
# 		while(i>=num):
# 			x= x + i
# 			i=i-1
# 		print x,


# # sum_nums2(-3)

#def fizz_buzz(i):
i=1
while (i <=100):
	if (i%3==0 and i%5 ==0):
		print "fizzbuzz"
	elif (i%3==0):
		print "fizz",
	elif (i%5 == 0):
		print "buzz",
	else:
		print i, 
	i = i + 1 
#fizz_buzz()