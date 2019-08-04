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
	a = ["a", "b" , "c", "d", "f", "g", "h"]

	if (len(a) > 1):
		for i in range(len(a)-1):
			temp = i+i+1
			if temp%2!=0 and isPrime(temp):
				print("Found Defected Package at position", i, "and", i+1)
	else:
		print("There are less than 2 packages to test")