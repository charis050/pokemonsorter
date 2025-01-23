# ECOR 1042 Lab 6 - Template for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Charis Nobossi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101297742"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "045"

#==========================================#
# Place your curve_fit function after this line
import numpy as np

import matplotlib.pyplot as plt

def curve_fit(characters_list: list[dict], attribute: str, order: int) -> str:
    """ This function will return the equation of a curve that best fits when given a specific data set with health values and another attribute.
        
    Parameters:
        - character_list: A list of dictionaries representing a set of data points.
        
        Return Value:
        - str: A string representing the equation of the polynomial curve given.
               The equation is in the form 'y = ax^n + bx^(n-1) + ... + cx + d'.
               
        Examples:
        >>>curve_fit([{"Health": 2, "Strength": 4}, {"Health": 3, "Strength": 6}, {"Health": 6, "Strength": 2}, {"Health": 3, "Strength": 1}], "Strength", 2)
        ' y = -0.03140703517587802x^2 + -0.08417085427136639x + 4.221105527638202'

        >>>curve_fit([{"Health": 0, "Strength": 0}, {"Health": 4, "Strength": 2}, {"Health": 9, "Strength": 3}, {"Health": 16, "Strength": 4}], "Strength", 2)
        ' y = 1.0000000000000007x^2 + -3.0601770173539476e-15x + 4.55631731326442e-15'
        
        >>>curve_fit([{"Health": 1, "Strength": 0}, {"Health": 2, "Strength": 2}, {"Health": 3, "Strength": 9}, {"Health": 4, "Strength": 0}], "Strength", 2)
        ' y = 0.04365079365079369x^2 + -0.3373015873015879x + 2.500000000000001'
        """    
    levels = {}
    for character in characters_list:
        level = character[attribute]
        health = character['Health']
        if level not in levels:
            levels[level] = [health]
        else: 
            levels[level].append(health)
    attribute_levels = list(levels.keys())
    health_list = []
    for key in attribute_levels:
        health_list.append(np.mean(levels[key]))
        
        
                
    
    if len(attribute_levels) < 5 and order > len(attribute_levels) - 1:
        order = len(attribute_levels) - 1
       
        coeff_list = np.polyfit(attribute_levels, health_list, order)
        
        if order == 1:
            return f" y =  {coeff_list[0]}x + {coeff_list[1]}" 
        
        elif order == 2:
            return f" y = {coeff_list[0]}x^2 + {coeff_list[1]}x + {coeff_list[2]}"
        

        elif order == 3:
            return f" y = {coeff_list[0]}x^3 + {coeff_list[1]}x^2 + {coeff_list[2]}x + {coeff_list[3]}"
        
        elif order == 4:
            return f" y = {coeff_list[0]}x^4 + {coeff_list[1]}x^3 + {coeff_list[2]}x^2 + {coeff_list[3]}x + {coeff_list[4]}"
        
        elif order == 5:
            return f" y = {coeff_list[0]}x^5 + {coeff_list[1]}x^4 + {coeff_list[2]}x^3 + {coeff_list[3]}x^2 + {coeff_list[4]}x + {coeff_list[5]}"        

    else:
        coeff_list = np.polyfit(attribute_levels, health_list, order)
        
        if order == 1:
            return f" y =  {coeff_list[0]}x + {coeff_list[1]}" 
        
        elif order == 2:
            return f" y = {coeff_list[0]}x^2 + {coeff_list[1]}x + {coeff_list[2]}"
        

        elif order == 3:
            return f" y = {coeff_list[0]}x^3 + {coeff_list[1]}x^2 + {coeff_list[2]}x + {coeff_list[3]}"
        
        elif order == 4:
            return f" y = {coeff_list[0]}x^4 + {coeff_list[1]}x^3 + {coeff_list[2]}x^2 + {coeff_list[3]}x + {coeff_list[4]}"
        
        elif order == 5:
            return f" y = {coeff_list[0]}x^5 + {coeff_list[1]}x^4 + {coeff_list[2]}x^3 + {coeff_list[3]}x^2 + {coeff_list[4]}x + {coeff_list[5]}"         
            
            
        

# Do NOT include a main script in your submission



