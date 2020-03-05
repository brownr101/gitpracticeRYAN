
# Partner 1: Ryan Dumb Brown
# Partner 2: Alden Cheeseball McVay
############################################# 
def getNRandom(n):
	'''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
	from random import randint
	randlist = []
	for i in range (n):
		x = randint(1,10)
		randlist.append(x)
	print(randlist)
getNRandom(15)
		

def multiplyRandom(numbers):
	'''takes in a list of n numbers and returns the product of the numbers'''
    pass

def main():
	print(multiplyRandom(getNRandom(10))

if __name__ == "__main__":
	main()
