if __name__ == '__main__':
	brides = ["Maria", "Kenya", "Amee", "Angelina"]
	grooms = ["John", "Harry", "Peter", "Mark"]
	res = []

	if len(brides) != len(grooms):
		print("Number of Brides and Grooms does not match")

	for b, g in zip(brides, grooms):
		res.append((b, g))

	print(res)