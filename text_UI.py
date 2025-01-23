# ECOR 1042 Lab 6 - Template text UI
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Andrew Yan"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101295798"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-045"

#==========================================#
# Place your script for your text_UI after this line
from load_data import *
from sort import *
from curve_fit import *
from histogram import *
while True:
    ui_main = input("The available commands are:\n\tL)oad data\n\tS)ort data\n\tC)urve fit\n\tH)istogram\n\tE)xit\n\nPlease type your command: ").upper()
    if ui_main == "L":
        file_name = input("Please enter the name of the file: ")
        try:
            open(file_name)
        except:
            print("No such file.")
            pass
        else:
            user_att = input("Please enter the attribute to use as a filter: ")
            if user_att not in ("Occupation", "Strength", "Luck", "Weapon", "All"):
                print("Invalid command.")
                pass
            elif user_att == "All":
                data = calculate_health(load_data(file_name, ("All", "ignored")))
                print("Data loaded.")
            elif user_att in ("Occupation", "Weapon"):
                user_att_val = input("Please enter the value of the attribute: ")
                data = calculate_health(load_data(file_name, (user_att, user_att_val)))
                print("Data loaded.")
            elif user_att in ("Luck"):
                try:
                    user_att_val = float(input("Please enter the value of the attribute: "))
                except:
                    print("Invalid command.")
                    pass
                else:
                    data = calculate_health(load_data(file_name, ("All", "ignored")))
                    i = 0
                    while i < len(data):
                        if data[i]['Luck'] > user_att_val:
                            data.pop(i)
                            i -= 1
                        i += 1
                    for char in data:
                        del char['Luck']
                    print("Data loaded.")
            else:
                try:
                    user_strength_min = int(input("Please enter the lower value of the attribute: "))
                    user_strength_max = int(input("Please enter the upper value of the attribute: "))
                except:
                    print("Invalid command")
                    pass
                else:
                    data = calculate_health(load_data(file_name, ("All", "ignored")))
                    i = 0
                    while i < len(data):
                        if data[i]['Strength'] < user_strength_min or data[i]['Strength'] > user_strength_max:
                            data.pop(i)
                            i -= 1
                        i += 1
                    for char in data:
                        del char['Strength']
                    print("Data loaded.")

    elif ui_main == "S":
        try:
            data == ""
        except:
            print("File not loaded. Please, load a file first.")
            pass
        else:
            user_sort_att = input("Please enter the attribute you want to use for sorting:\n'Agility', 'Armor', 'Intelligence', 'Health': ")
            if user_sort_att not in ("Agility", "Armor", "Intelligence", "Health"):
                print("Invalid command.")
                pass
            else:
                user_sort_ord = input("Ascending (A) or Descending (D) order: ").upper()
                if user_sort_ord not in ("A", "D"):
                    print("Invalid command.")
                    pass
                else:
                    data_sorted = sort(data, user_sort_ord, user_sort_att)
                    user_sort_disp = input("Data sorted. Do you want to display the data?: ").lower()
                    if user_sort_disp not in ("y", "n"):
                        print("Invalid command.")
                        pass
                    elif user_sort_disp in "y":
                        print(data_sorted)
                    else:
                        pass

    elif ui_main == "C":
        try:
            data == ""
        except:
            print("File not loaded. Please, load a file first.")
            pass
        else:
            user_curve_att = input("Please enter the attribute you want to use to find the best fit for Health: ")
            try:
                user_curve_poly = int(input("Please enter the order of the polynomial to be fitted: "))
            except:
                ("Invalid command")
                pass
            else:
                print(curve_fit(data, user_curve_att, user_curve_poly))

    elif ui_main == "H":
        try:
            data == ""
        except:
            print("File not loaded. Please, load a file first.")
            pass
        else:
            user_hist_att = input("Please enter the attribute you want to use for plotting: ")
            histogram(data, user_hist_att)

    elif ui_main == "E":
        break

    else:
        print("No such command")
