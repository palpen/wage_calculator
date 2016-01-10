
import re
import argparse

def wage_calculator(log_txt_file, month, year, wage):

	date_pattern = "\*\*Date\*\*"  # pattern identifying the date in the file
	hours_full = []

	with log_txt_file as f:

		for line in log_txt_file:

			if re.search(r"{0}".format(date_pattern), line):  # go to the relevant line

				if re.search(month, line) and re.search(str(year), line):  # within line, go to desired month/year

					# skips two lines to the line containing the number of hours worked
					f.next()
					hours_line = f.next()

					hours_list_str = re.findall(r'[-+]?\d*\.*\d+', hours_line)  # put hours in a list
					hours_list = [float(x) for x in hours_list_str]

					hours_full += hours_list

					sum_hours_date = sum(hours_list)

					print line.rstrip()
					print "Hours logged: " + str(hours_list)
					print "Total hours for the day " + str(sum_hours_date) + "\n"

	hours_total = sum(hours_full)

	print "Total hours worked in {0} {1} is {2}".format(month, year, 														hours_total)
	print "At ${0}/hr, your total wage for {1} {2} is ${3}".format(wage, month, year, hours_total * wage)


def main():

	parser = argparse.ArgumentParser()

	parser.add_argument("file",
						help="Text file containing hours logged (e.g. ra_hours.txt)",
						type=argparse.FileType('r')
						)
	parser.add_argument("month",
						help="The month for which we want the income",
						type=str)
	parser.add_argument("year",
						help="Enter year",
						type=int)
	parser.add_argument("wage",
						help="Enter hourly wage",
						type=float)

	args = parser.parse_args()

	wage_calculator(args.file, args.month, args.year, args.wage)

if __name__ == '__main__':
	main()

