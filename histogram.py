# ECOR 1042 Lab 6 - Template submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Axel Greavette"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101298645"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-045"

#==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt

# Do NOT include a main script in your submission

def histogram(data: list[dict], atr: str) -> int:
    """
    This function takes in a list of dictionaries and an attribute to create a histogram of the data.
    For numerical data, the function will create a histogram with 20 evenly spaced bins, and for categorical data it will just count it.
    
    >>> histogram(load_data("characters-test.csv", ("All", "")), "Strength")
    [Figure displayed]
    20
    >>> histogram(load_data("characters-test.csv", ("All", "")), "Luck")
    [Figure displayed]
    0.89
    >>> histogram(load_data("characters-test.csv", ("All", "")), "Occupation")
    [Figure displayed]
    -1 
    """

    data = [d[atr] for d in data]
    data.sort()

    maximum = max(data) if isinstance(data[0], (int, float)) else -1

    # i got lazy
    if isinstance(data[0], (int, float)):
        # create a list of 20 evenly spaced numbers between 0 and the maximum value
        uniques = [round(i * maximum/20, 2) for i in range(21)]
        #empty dictionaries to make sure they're defined
        distributed = {} # this will contain the values that fit into our ranges
        fill = {} # while this will be padded with zeros to ensure that all ranges are present in the final dictionary and histogram
        for key, val in {i:data.count(i) for i in data}.items():
            for iteration in uniques:
                # if we're on the final iteration, we already know the outcome so break
                if uniques.index(iteration) == len(uniques) - 1:
                    break

                # we're already iterating through and determining the string keys, so might as well
                # create a dummy dict to fill out the missing increments while we do it
                fill[f"{iteration}-{uniques[uniques.index(iteration) + 1]}"] = 0

                # check if the key is greater than the current iteration and less than the next one
                if key > iteration and key <= uniques[uniques.index(iteration) + 1]:
                    distributed[f"{iteration}-{uniques[uniques.index(iteration) + 1]}"] = val                    

        # combine the two dictionaries, with a preference for the distributed values
        count = {**fill, **distributed}
    else:
        # easy... just count the occures of each value in the array
        count = {i: data.count(i) for i in data}

    _fig = plt.figure()
    plt.title(f"{atr} Distribution Across Dataset")
    plt.xlabel(atr)
    plt.ylabel("Number of Occurences")
    plt.bar([key for key, _ in count.items()], [val for _, val in count.items()], color="blue")

    plt.show()

    return maximum