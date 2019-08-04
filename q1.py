import math

# Function to find the Primes number
def isPrime(num):
	if num < 2:
		return False

	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

if __name__ == '__main__':
	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	pillow = 19
	res = 0

	list2 = [i+pillow for i in list1]

	for i in list2:
		res += i if isPrime(i) else 0

	print("Prize money:", res)
