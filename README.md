# Wage Calculator
This is a simple system that will help you take notes on your activity and keep track of the hours you've worked. The python script will tabulate your hours by month and  calculate your income.

## How to use these files

Simple! Create a textfile much like the [sample log](https://github.com/palpen/wage_calculator/blob/master/sample_log.txt) in this repository. Each entry should have the same format as  the example below

    **Date**: 21 December 2015
    **Time**: 5pm - 7pm, 12-1am
    **Hours**: 2, 1, 

    **Notes**:
    + Debugged script written yesterday
    + Checked data 

The script that calulate the hours and wage is fairly flexible. The only requirement is that the year is four digits (to distinguish it from the day). The hours during each session may be delimited using any delimeter. There is not restriction on how the notes are entered (you can write paragraphs if you wish).

When the time comes for you to calculate your wage  for the month execute the following in the command line

    python calculate_hours.py my_log.txt MONTH YEAR HOURLY_WAGE

For the example using the sample log

    python calculate_hours.py sample_log.txt December 2015 25

The output of this entry is

IMAGE OF OUTPUT--- see screen shot