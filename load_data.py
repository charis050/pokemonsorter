# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Abdullah Khan, Axel Greavette, Andrew Yan, Charis Nobossi"

# Update "" with your team (e.g. T102)
__team__ = "T045"


#==========================================#
# Place your character_occupation_list function after this line

def character_occupation_list(filename: str, occupation: str) -> list[dict]:
    """
    Returns a list of dictionaries of characters who have a certain occupation.
    
    >>>character_occupation_list('characters-mat.csv', 'AT')
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, {another element}]
    >>>character_occupation_list('characters-mat.csv', 'Occupation')
    []
    >>>character_occupation_list('characters-mat.csv', 'abc')
    []
    """
    if occupation == "Occupation":
        return []
    characters = []
    first_line = True
    for line in open(filename, "r"):
        if first_line:
            header = line.split(",")
            first_line = False
        if line.split(",")[0] == occupation:
            characters.append({header[1]: int(line.split(",")[1]), header[2]: int(line.split(",")[2]), header[3]: int(line.split(",")[3]), header[4]: int(line.split(",")[4]), header[5]: int(line.split(",")[5]), header[6]: float(line.split(",")[6]), header[7]: int(line.split(",")[7]), header[8].strip(): line.strip().split(",")[8]})
    return characters

#==========================================#
# Place your character_strength_list function after this line


def character_strength_list(file_name: str, character_strength_list: tuple[int]) -> list[dict]:
    """
   This function returns a list of characters with strenghts that are within a specific range. 
    
    Precondition:
    
    The table headers should be: 'Strenght', 'Occupation', 'Agility', 'Stamina', 'Personality', 'Intelligence', 'Luck','Armor', and 'Weapon'
    
    
    """

    in_file = open(file_name, "r")

    first_line = True

    character_list = []
    minimum = character_strength_list[0]
    maximum = character_strength_list[1]

    for line in in_file:
        line = line.strip().split(',')

        if first_line:

            first_line = False
            table_header = line

        else:

            if maximum >= int(line[1]) >= minimum:

                character = {}
                character[table_header[0]] = str(line[0])
                character[table_header[2]] = int(line[2])
                character[table_header[3]] = int(line[3])
                character[table_header[4]] = int(line[4])
                character[table_header[5]] = int(line[5])
                character[table_header[6]] = float(line[6])
                character[table_header[7]] = int(line[7])
                character[table_header[8]] = str(line[8])

                character_list.append(character)

    in_file.close()
    return character_list

#==========================================#
# Place your character_luck_list function after this line


def character_luck_list(file_name: str, luck_val: float) -> list[dict]:
    """Return a list of dictionaries of values with luck lower than the value provided. Does not return luck.
    Preconditions: 
    The file has the following columns: ['Occupation', 'Strength', 'Agility', 'Stamina', 'Personality', 'Intelligence', 'Luck', 'Armor', 'Weapon']
    >>> character_luck_list ('characters-mat.csv', 0.4)
    [{'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11, 'Armor': 8, 'Weapon': 'Staff'}, ...
    >>> character_luck_list('characters-mat.csv', 0.0)
    []
    >>> character_luck_list('characters-mat.csv', 1.82)
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Armor': 8, 'Weapon': 'Staff'}, ...
    """
    values_list = open(file_name, 'r')

    first_line = True
    val_list = []
    for line in values_list:
        line = line.strip().split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            values = {}
            values[table_header[0]] = line[0]
            for i in range(1, 6):
                values[table_header[i]] = int(line[i])
            values[table_header[7]] = int(line[7])
            values[table_header[8]] = line[8]

            if float(line[6]) < luck_val:
                val_list.append(values)
    values_list.close()
    return val_list

#==========================================#
# Place your character_weapon_list function after this line


def character_weapon_list(character_file: str, weapon: str) -> list[dict]:
    """Read the given character list CSV file and return the characters that use the given weapon.
    
    >>> character_weapon_list("characters-mat.csv", "Short sword")
    [{'Occupation': 'HG', 'Strength': '19', 'Agility': '3', 'Stamina': '8', 'Personality': '9', 'Intelligence': '4', 'Luck': '0.67', 'Armor': '8'}, ...]
    >>> character_weapon_list("characters-mat.csv", "Spear")
    [{'Occupation': 'VF', 'Strength': '12', 'Agility': '12', 'Stamina': '10', 'Personality': '12', 'Intelligence': '8', 'Luck': '0.78', 'Armor': '11'}, ...]
    >>> character_weapon_list("characters-mat.csv", "Boulder")
    []
    """

    GENERAL_LIST = open(character_file, "r")
    character_matches = []

    i_hate_io_streams = []

    for line in GENERAL_LIST:
        i_hate_io_streams.append(line.strip().split(","))

    GENERAL_LIST.close()
    headers = i_hate_io_streams[0]
    del i_hate_io_streams[0]

    for character in i_hate_io_streams:
        dict_template = {}
        if character[-1] != weapon:
            continue
        else:
            for attr in headers:
                if headers.index(attr) == len(headers) - 1:
                    continue
                else:
                    dict_template[attr] = float(character[headers.index(attr)]) if attr == headers[-3] else int(character[headers.index(attr)]) if attr != headers[0] else character[headers.index(attr)]

        character_matches.append(dict_template)

    return character_matches

#==========================================#
# Place your load_data function after this line


def load_data(filename: str, attribute: tuple) -> list[dict]:
    """
    Load data from CSV and filter based on attribute. Precondition: attribute is tuple containing filter (one of "Occupation", "Strength", "Luck", "Weapon" or "All") and value (ignored if filter is "All"). 
    
    >>> load_data("characters-mat.csv", ("Occupation", "AT"))
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, ...]
    >>> load_data("characters-mat.csv", ("All", "ignored")
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, ...]
    >>> load_data("characters-mat.csv", ("Weapon","Short sword"))
    [{'Occupation': 'HG', 'Strength': 19, 'Agility': 3, 'Stamina': 8, 'Personality': 9, 'Intelligence': 4, 'Luck': 0.67, 'Armor': 8}, ...]
    """
    if attribute[0] == "Occupation":
        return character_occupation_list(filename, attribute[1])

    elif attribute[0] == "Strength":
        return character_strength_list(filename, attribute[1])

    elif attribute[0] == "Luck":
        return character_luck_list(filename, attribute[1])

    elif attribute[0] == "Weapon":
        return character_weapon_list(filename, attribute[1])

    elif attribute[0] == "All":
        characters = []
        first_line = True
        for line in open(filename, "r"):
            if first_line:
                header = line.split(",")
                first_line = False
            else:
                characters.append({header[0]: line.split(",")[0], header[1]: int(line.split(",")[1]), header[2]: int(line.split(",")[2]), header[3]: int(line.split(",")[3]), header[4]: int(line.split(",")[4]), header[5]: int(line.split(",")[5]), header[6]: float(line.split(",")[6]), header[7]: int(line.split(",")[7]), header[8].strip(): line.strip().split(",")[8]})
        return characters

    else:
        print("Invalid Value")
        return []

#==========================================#
# Place your calculate_health function after this line


def calculate_health(character_list: list[dict]) -> list[dict]:
    """Calculate health of each character in supplied dictionary list and returns a list of modified dictionaries containing health.
    
    >>> calculate_health(load_data("characters-mat.csv", ("Weapon","Short sword")))
    [{'Occupation': 'HG', 'Strength': 19, 'Agility': 3, 'Stamina': 8, 'Personality': 9, 'Intelligence': 4, 'Luck': 0.67, 'Armor': 8, 'Health': 85.88}, ...]
    >>> calculate_health([{'Occupation': 'HG', 'Strength': 18, 'Agility': 13, 'Stamina': 8, 'Personality': 13, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 11}, {'Occupation': 'HG', 'Strength': 15, 'Agility': 13, 'Stamina': 9, 'Personality': 9, 'Intelligence': 11, 'Luck': 0.39, 'Armor': 11}])
    [{'Occupation': 'HG', 'Strength': 18, 'Agility': 13, 'Stamina': 8, 'Personality': 13, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 11, 'Health': 127.5}, {'Occupation': 'HG', 'Strength': 15, 'Agility': 13, 'Stamina': 9, 'Personality': 9, 'Intelligence': 11, 'Luck': 0.39, 'Armor': 11, 'Health': 104.19}]
    >>> 
    """
    for character in character_list:
        health = (character["Strength"] + character["Agility"] + character["Stamina"] + character["Personality"] + character["Intelligence"]) + ((character["Armor"]**2) * character["Luck"])
        character["Health"] = round(health, 2)
    return character_list

# Do NOT include a main script in your submission
