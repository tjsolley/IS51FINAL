"""
This program will be able to calculate the length, average, and percent
above average for a list o grades.
We will first define a main function
open and read the text file
outut the list of grade
output the sum
calculate average
create a counter for each grade above average
calculate percentage
output results to user
"""

"""
define main fuction
open and read Final.txt
identify lenght and sum of grades
divide sum by length
print outputs to user
create counter for each item in list above average
calculate percentage by counter / lenght
print ouput to user
"""

def main():
    grades = {78, 67, 56, 99, 80, 83, 82, 91, 94, 95, 77, 88, 85, 92, 91, 79, 88, 82, 81, 86, 94, 93, 92, 45}
    calculate_percentage_above_average(grades)

def calculate_percentage_above_average(grades):
    length = len(grades)
    sum1 = sum(grades)
    avg = sum1 / length
    print("Number of Grades:", length)
    print("Average Grade:", avg)
    counter = 0
    for item in grades:
        is item > avg:
        counter += 1
    PercentHigher = counter / length
    print("Percent of grades above average:", end = " ")
    print("{0:.2}".format(PercentHigher))

main()


