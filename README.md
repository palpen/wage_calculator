# Wage Calculator
This is a simple system for research assistants for taking notes on your activity and keeping track of the hours you've worked. The python script will tabulate your hours by month and calculate your income.

### How to use these files

Simple! Create a textfile much like the [sample log](https://github.com/palpen/wage_calculator/blob/master/sample_log.txt) in this repository. Each entry should be formatted like the sample below

    **Date**: 21 December 2015
    **Time**: 5pm - 7pm, 12-1am
    **Hours**: 2, 1

    **Notes**:
    + Debugged script written yesterday
    + Checked data 

The script depends on \*\*Date\*\* and \*\*Hours\*\* and their exact ordering to work. Other than that, it is fairly flexible. The only other requirement is that the year is four digits (to distinguish it from the day). The hours during each session may be delimited using any common delimiter (comma, space, semi-colon). There are no restrictions on how log entries under \*\*Notes\*\* are entered (you can write paragraphs if you wish).

### Calculating hours and total wages for a month

When the time comes for you to calculate your total hours and wages for the month, make sure that the python script is in the same directory as your log, then execute the following in the command line

    python calculate_hours.py MY_LOG.txt MONTH YEAR HOURLY_WAGE

For example, to calculate total hours and wages for December 2015 using the sample_log.txt, we execute

    python calculate_hours.py sample_log.txt December 2015 25

The output for which is

![Alt text][id]

### To Do:
- Get hours worked from \*\*Time\*\*
- Allow calculation of hours and wages for multiple months



TEST
[id]: img/output_term.png
