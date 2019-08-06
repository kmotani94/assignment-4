def calcSalary(salary, el, l, hours, days, start):
	week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	day = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
	n = [0, 1, 2, 3, 4, 5, 6]
	workingDays = 0
	al = el - l
	for i in range(1, days+1):
		# print(i, n[((i+day[start])%7)-1], week[((i+day[start])%7)-1])
		if (n[((i+day[start])%7)-1]<5 and n[((i+day[start])%7)-1]>=0):
			workingDays += 1

	totalHours = (workingDays-l)*hours
	totalSalary = (workingDays-l)*hours*salary
	print("Working days:", workingDays)
	print("Leaves:", l)
	print("Earned leaves:", el)
	print("Total Working days excluding leaves:", workingDays+al)
	print("Total number of hours:", totalHours)
	print("Salary per hour:", salary)
	print("Total monthly salary:", totalSalary)

if __name__ == '__main__':
	salary = 40
	el = 2
	l = 3
	hours = 8
	days = 30
	start = "Saturday"
	calcSalary(salary, el, l, hours, days, start)