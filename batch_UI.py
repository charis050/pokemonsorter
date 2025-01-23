# ECOR 1042 Lab 6 - Template Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Abdullah Khan"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "1010305235"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-045"

#==========================================#
# Place your script for your batch_UI after this line
from load_data import *
from sort import *
from curve_fit import *
from histogram import *
import string

filename = input("Please enter the name of the file where your commands are stored: ")

commands = open(filename)

data = []

load_step = True

for line in commands:
    i = 0
    steps = []
    for command in line.strip().split(';'):
        steps.append(command)
        i += 1

    if load_step:
        try:
            if steps[2] == 'Luck':
                steps[3] = float(steps[3])

            if steps[2] == 'Strength':
                temp_strength = []
                for i in steps[3].strip(string.punctuation).split(','):
                    temp_strength.append(i)
                strength = (int(temp_strength[0]), int(temp_strength[1]))
        except:
            None
        load_step = False

    if steps[0] == 'l' or steps[0] == 'L':
        if steps[2] == 'Occupation' or steps[2] == 'Weapon':
            data = calculate_health(load_data(steps[1], (steps[2], steps[3])))
        else:
            data = calculate_health(load_data(steps[1], ('All', 'Nothing')))
            i = 0
            while i < len(data):
                if steps[2] == 'Luck' and data[i]['Luck'] > steps[3]:
                    data.pop(i)
                    i -= 1

                if steps[2] == 'Strength' and data[i]['Strength'] > strength[0] or data[i]['Strength'] < strength[1]:
                    data.pop(i)
                    i -= 1

                i += 1

            for char in data:
                if not(steps[2] == 'All'):
                    del char[steps[2]]

        print('Data loaded')

    if steps[0] == 's' or steps[0] == 'S':
        data = sort(data, steps[2], steps[1])
        print('Data sorted.')
        if steps[3] == 'y':
            print(data)

    if steps[0] == 'c' or steps[0] == 'C':
        print(curve_fit(data, steps[1], int(steps[2])))

    if steps[0] == 'h' or steps[0] == 'H':
        histogram(data, steps[1])



