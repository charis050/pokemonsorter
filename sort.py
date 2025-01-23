# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Abdullah Khan, Axel Greavette, Andrew Yan, Charis Nobossi"

# Update "" with your team (e.g. T102)
__team__ = "T045"

#==========================================#
# Place your sort_characters_agility_bubble function after this line


def sort_characters_agility_bubble(characters_list: list[dict], sort_choice: str) -> list[dict]:
    """ This function sorts characters in a list by their agility, in either an asending or descending order. 
    
    Examples: 
    >>> sort_characters_agility_bubble([{'Occupation':'AT', 'Agility':8}, {'Occupation':'EB', 'Agility':13}, {'Occupation':'DB', 'Agility':9}, {'Occupation':'AT', 'Agility':12}], 'A')
    
    [{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'AT', 'Agility': 12}, {'Occupation': 'DB', 'Agility': 9}, {'Occupation': 'AT', 'Agility': 8}]
    
    >>> sort_characters_agility_bubble([{'Occupation':'DB', 'Agility':7}, {'Occupation':'EB', 'Agility':10}, {'Occupation':'DB', 'Agility':4}, {'Occupation':'AT', 'Agility':12}], 'A')
     
    [{'Occupation': 'EB', 'Agility': 4}, {'Occupation': 'DB', 'Agility': 7}, {'Occupation': 'DB', 'Agility': 10}, {'Occupation': 'AT', 'Agility': 12)]
    
    >>> sort_characters_agility_bubble([{'Occupation':'EB', 'Agility':12}, {'Occupation':'EB', 'Agility':13}, {'Occupation':'DB', 'Agility':22}, {'Occupation':'AT', 'Agility':15 'A')

    [{'Occupation': 'EB', 'Agility': 12}, {'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'AT', 'Agility': 15}, {'Occupation': 'DB', 'Agility': 22)]

      
    """

    swap = True
    while swap:
        swap = False
        for i in range(len(characters_list) - 1):
            character1 = characters_list[i]
            character2 = characters_list[i + 1]

            if "Agility" in character1 and "Agility" in character2:

                if sort_choice == "A":

                    if character1["Agility"] > character2["Agility"]:
                        aux = characters_list[i]
                        characters_list[i] = characters_list[i + 1]
                        characters_list[i + 1] = aux
                        swap = True

                elif sort_choice == "D":

                    if character2["Agility"] > character1["Agility"]:
                        aux = characters_list[i]
                        characters_list[i] = characters_list[i + 1]
                        characters_list[i + 1] = aux
                        swap = True

            else:
                print("Agility Key is not in the dictionary")

                return characters_list

    return characters_list

#==========================================#
# Place your sort_characters_intelligence_selection function after this line


def sort_characters_intelligence_selection(characters: list[dict], order: str) -> list[dict]:
    """
    Takes a list of dictionaries and reordies them in either ascending and descending order based on the value associated with the "Intelligence" key in the dictionaries.
    Preconditions: Every Dictionary must have the same keys.
    >>>sort_characters_intelligence_selection([{"Occupation": "EB", "Intelligence": 9}, {"Occupation": "M", "Intelligence": 12}], "D")
    [{'Occupation': 'M', 'Intelligence': 12}, {'Occupation': 'EB', 'Intelligence': 9}]
    >>>sort_characters_intelligence_selection([{"Occupation": "EB"}, {"Occupation": "M"}], "D")
    "Intelligence" key is not present
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]
    >>>sort_characters_intelligence_selection([{"Occupation": "EB", "Intelligence": 4}, {"Occupation": "M", "Intelligence": 2}, {"Occupation": "M", "Intelligence": 5}, {"Occupation": "M", "Intelligence": 76}, {"Occupation": "M", "Intelligence": 243542}, {"Occupation": "M", "Intelligence": 23}, {"Occupation": "M", "Intelligence": 222}, {"Occupation": "M", "Intelligence": 67}, {"Occupation": "M", "Intelligence": 2}, {"Occupation": "M", "Intelligence": 9}], "D")
    [{'Occupation': 'M', 'Intelligence': 243542}, {'Occupation': 'M', 'Intelligence': 222}, {'Occupation': 'M', 'Intelligence': 76}, {'Occupation': 'M', 'Intelligence': 67}, {'Occupation': 'M', 'Intelligence': 23}, {'Occupation': 'M', 'Intelligence': 9}, {'Occupation': 'M', 'Intelligence': 5}, {'Occupation': 'EB', 'Intelligence': 4}, {'Occupation': 'M', 'Intelligence': 2}, {'Occupation': 'M', 'Intelligence': 2}]
    """
    if len(characters) == 0 or characters[0].get("Intelligence") == None:
        print('''"Intelligence" key is not present''')

    else:
        for i in range(len(characters)):
            nextcha = i

            for j in range(i + 1, len(characters)):
                if (order == "A" and characters[nextcha].get("Intelligence") > characters[j].get("Intelligence")) or (order == "D" and characters[nextcha].get("Intelligence") < characters[j].get("Intelligence")):
                    nextcha = j

            characters[i], characters[nextcha] = characters[nextcha], characters[i]

    return characters

#==========================================#
# Place your sort_characters_health_insertion function after this line


def sort_characters_health_insertion(arr: list[dict], ord: str) -> list[dict]:
    """
    This function sorts a list of dictionaries by the value of the "Health" key in each dictionary using an insertion sort algorithm.
    Precondition: `ord` must be one of "A" or "D" to specify the order of the sort.

    >>> sort_characters_health_insertion(calculate_health([{'Occupation': 'HG', 'Strength': 18, 'Agility': 13, 'Stamina': 8, 'Personality': 13, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 11}, {'Occupation': 'HG', 'Strength': 15, 'Agility': 13, 'Stamina': 9, 'Personality': 9, 'Intelligence': 11, 'Luck': 0.39, 'Armor': 11}]), "A")
    [{'Occupation': 'HG', 'Strength': 15, 'Agility': 13, 'Stamina': 9, 'Personality': 9, 'Intelligence': 11, 'Luck': 0.39, 'Armor': 11, 'Health': 104.19}, {'Occupation': 'HG', 'Strength': 18, 'Agility': 13, 'Stamina': 8, 'Personality': 13, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 11, 'Health': 127.5}]
    >>> sort_characters_health_insertion(calculate_health(load_data("characters-mat.csv", ("Weapon","Short sword"))), "D")
    [{'Occupation': 'HG', 'Strength': 11, 'Agility': 11, 'Stamina': 7, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.83, 'Armor': 11, 'Health': 150.43}, ...]
    """
    dp = arr
    v = False
    for i in range(1, len(arr)):
        if "Health" not in arr[i]:
            print("Health key not found in all dictionaries.")
            v = True
            break
        k = arr[i]
        j = i - 1
        while j >= 0 and k["Health"] < arr[j]["Health"]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k

    return dp if v else arr if ord == "A" else arr[::-1]

#==========================================#
# Place your sort_characters_armor_bubble function after this line


def sort_characters_armor_bubble(characters: list[dict], order: str) -> list:
    """ The function takes a list of dictionaries and string; sorts the list based on armor attribute in ascending or descending order based on user input. Returns a list.
    
    >>> sort_characters_armor_bubble([{'Occupation': 'EB','Armor': 10}, {'Occupation': 'H', 'Armor': 11}], "D")
    [{'Occupation': 'H', 'Armor': 11}, {'Occupation': 'EB', 'Armor': 10}]
    >>> sort_characters_armor_bubble([{'Occupation': 'EB','Armor': 10}, {'Occupation': 'H', 'Armor': 11}, {'Occupation': 'G', 'Armor': 8}], "A")
    [{'Occupation': 'G', 'Armor': 8}, {'Occupation': 'EB', 'Armor': 10}, {'Occupation': 'H', 'Armor': 11}]
    >>> sort_characters_armor_bubble([{'Occupation': 'EB',}, {'Occupation': 'H'}], "D")
    "Armor" key is not present.
    [{'Occupation': 'EB'}, {'Occupation': 'H'}]
    """
    armor = False
    for character in characters:
        if 'Armor' in character:
            armor = True
            break
    if armor:
        swap = True
        n = len(characters)

        if order == 'A':
            while swap:
                swap = False
                for i in range(n - 1):
                    armor_curr = characters[i].get('Armor', int)
                    armor_next = characters[i + 1].get('Armor', int)
                    if armor_curr > armor_next:
                        place = characters[i]
                        characters[i] = characters[i + 1]
                        characters[i + 1] = place
                        swap = True

        elif order == 'D':
            while swap:
                swap = False
                for i in range(n - 1):
                    armor_curr = characters[i].get('Armor', int)
                    armor_next = characters[i + 1].get('Armor', int)
                    if armor_curr < armor_next:
                        place = characters[i]
                        characters[i] = characters[i + 1]
                        characters[i + 1] = place
                        swap = True

    else:
        print("\"Armor\" key is not present.")

    return characters

#==========================================#
# Place your sort function after this line


def sort(given: list[dict], order: str, attribute: str) -> list[dict]:
    """
    Helper method collecting all other sort functions. Supply a list of dictionaries, the order to sort them in, and the attribute to sort by (one of "Agility", "Intelligence", "Health", or "Armor").

    >>> sort([{'Occupation': 'EB','Armor': 10}, {'Occupation': 'H', 'Armor': 11}], "A", "Armor")
    [{'Occupation': 'EB', 'Armor': 10}, {'Occupation': 'H', 'Armor': 11}]
    >>> sort([{'Occupation': 'HG', 'Strength': 15, 'Agility': 13, 'Stamina': 9, 'Personality': 9, 'Intelligence': 11, 'Luck': 0.39, 'Armor': 11, 'Health': 104.19}, {'Occupation': 'HG', 'Strength': 18, 'Agility': 13, 'Stamina': 8, 'Personality': 13, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 11, 'Health': 127.5}], "D", "Agility")
    [{'Occupation': 'HG', 'Strength': 15, 'Agility': 9, 'Stamina': 9, 'Personality': 9, 'Intelligence': 11, 'Luck': 0.39, 'Armor': 11, 'Health': 104.19}, {'Occupation': 'HG', 'Strength': 18, 'Agility': 17, 'Stamina': 8, 'Personality': 13, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 11, 'Health': 127.5}]
    >>> sort([{"Occupation": "EB", "Intelligence": 9}, {"Occupation": "M", "Intelligence": 12}], "A", "Swag")
    Cannot be sorted by "Swag"
    [{"Occupation": "EB", "Intelligence": 9}, {"Occupation": "M", "Intelligence": 12}]
    """
    match attribute:
        case "Agility":
            return sort_characters_agility_bubble(given, order)
        case "Intelligence":
            return sort_characters_intelligence_selection(given, order)
        case "Health":
            return sort_characters_health_insertion(given, order)
        case "Armor":
            return sort_characters_armor_bubble(given, order)
        case _:
            print(f'Cannot be sorted by "{attribute}"')
            return given

# Do NOT include a main script in your submission


