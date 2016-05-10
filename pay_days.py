from datetime import time, date, timedelta

# returns a list of pay days starting from next ending before end_date. 
# freq is the number of weeks between pay days
def payperiods(next, end_date, freq = 2):
	pay_days = []
	while (next < end_date):
		pay_days.append(next)
		next = next + timedelta(weeks = freq)
	return pay_days

# prints a list of dates formatted in a nice way
def print_dates(dates):
	for date in pay:
		print("{:>10}".format(date.strftime("%B")) + 
			" {:>2},".format(date.day) +
			" {}".format(date.strftime("%Y")))


pay = payperiods(date(2016, 5, 13), date(2017, 1, 1), 2)
print("There are {} pay periods left this year".format(len(pay)))
print_dates(pay)