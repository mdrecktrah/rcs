# Version 0.3

# Import modules
import random

# Create dictionaries
faction_races = {
    "Alliance":["Dwarf", "Gnome", "Human", "Night elf"],
    "Horde":["Orc", "Tauren", "Troll", "Undead"]
}

races_classes = {
    "Dwarf":["Hunter", "Paladin", "Priest", "Rogue", "Warrior"],
    "Gnome":["Mage", "Rogue", "Warlock", "Warrior"],
    "Human":["Mage", "Paladin", "Priest", "Rogue", "Warlock", "Warrior"],
    "Night elf":["Druid", "Hunter", "Priest", "Rogue", "Warrior"],
    "Orc":["Hunter", "Rogue", "Shaman", "Warlock", "Warrior"],
    "Tauren":["Druid", "Hunter", "Shaman", "Warrior"],
    "Troll":["Hunter", "Mage", "Priest", "Rogue", "Shaman", "Warrior"],
    "Undead":["Mage", "Priest", "Rogue", "Warlock", "Warrior"]
}

start_areas_races = {
    "Dun Morogh":["Dwarf", "Gnome"],
    "Elwynn":"Human",
    "Teldrassil":"Night elf",
    "Durotar":["Orc", "Troll"],
    "Mulgore":"Tauren",
    "Lordaeron":"Undead"
}

spec_types = {
    "Tank":["Warrior", "Druid", "Paladin"],
    "Healer":["Priest", "Druid", "Paladin", "Shaman"],
    "Melee":["Warrior", "Rogue", "Shaman", "Paladin", "Druid"],
    "Ranged":["Mage", "Warlock", "Hunter", "Druid", "Priest", "Shaman"]
}

# Define functions
def random_character(faction_filter=None, race_filter=None, spec_type_filter=None, class_filter=None):
    if faction_filter is None:
        faction = random.choice(list(faction_races.keys()))
    else:
        faction = faction_filter
    
    """
    Races need to depend on classes as well. Currently, there is an error if there are no filters except for a class filter which results in empty sequences,
    for example if you only choose Alliance as faction and later on Paladin as class filter.
    This might be because the selected race does not include Paladins in their classes.
    """
    possible_races = faction_races[faction]
    if race_filter:
        possible_races = [race for race in possible_races if race in race_filter]
    selected_race = random.choice(possible_races)

    if spec_type_filter:
        possible_classes = []
        for spec in spec_type_filter:
            if class_filter:
                for cls in class_filter:
                    if cls in spec_types[spec] and cls in races_classes[selected_race]:
                        possible_classes.append(cls)
            else:
                for cls in spec_types[spec] and cls in races_classes[selected_race]:
                    possible_classes.append(cls)
    else:
        possible_classes = races_classes[selected_race] 
        if class_filter:
            possible_classes = [cls for cls in possible_classes if cls in class_filter]
    possible_classes = list(set(possible_classes))
    selected_class = random.choice(possible_classes)

    possible_specs = [spec for spec, cls in spec_types.items() if selected_class in cls]
    if spec_type_filter:
        possible_specs = [spec for spec in possible_specs if spec in spec_type_filter]
    selected_spec = random.choice(possible_specs)

    start_area = None
    for area, races in start_areas_races.items():
        if selected_race in races:
            start_area = area
            break

    return {
        "Faction": faction,
        "Starting Area": start_area,
        "Race": selected_race,
        "Class": selected_class,
        "Spec Type": selected_spec
    }

def faction_selection(faction_select):
    if faction_select == "R" or faction_select == "Random":
        faction_filter = None
    elif faction_select == "A" or faction_select == "Alliance":
        faction_filter = "Alliance"
    elif faction_select == "H" or faction_select == "Horde":
        faction_filter = "Horde"
    else:
        faction_select = input("Please select a valid option: A(lliance), H(orde) or R(andom) ").capitalize()
        faction_filter = faction_selection(faction_select)
    return faction_filter

def race_selection(race_select_trigger, faction_filter):
    if race_select_trigger == "Y" or race_select_trigger == "Yes":
        print(f"Please choose one or multiple of the following races:")
        if faction_filter != None:
            for race in faction_races[faction_filter]:
                print(f"- {race}")
        else:
            for faction in faction_races.keys():
                print("-" * 10)
                print(f"{faction}:")
                for race in faction_races[faction]:
                    print(f"- {race}")
        race_filter = [race.strip().capitalize() for race in input("If you select more than one race, please separate with a ',': ").split(",")]
    elif race_select_trigger == "N" or race_select_trigger == "No":
        race_filter = None
    else:
        print("Please enter a valid option.")
        race_select_trigger = input("Do you want to select one or multiple races for the selection process? Y(es) or N(o): ").capitalize()
        race_filter = race_selection(race_select_trigger, faction_filter)
    return race_filter

def spec_selection(spec_type_select_trigger):
    if spec_type_select_trigger == "Y" or spec_type_select_trigger == "Yes":
        print("Please choose one or multiple of the following specs:")
        for spec in spec_types.keys():
            print(f"- {spec}")
        spec_type_filter = [spec.strip().capitalize() for spec in input("If you select more than one spec, please separate with a ',': ").split(",")]
    elif spec_type_select_trigger == "N" or spec_type_select_trigger == "No":
        spec_type_filter = None
    else:
        print("Please enter a valid option.")
        spec_type_select_trigger = input("Do you want to select one or multiple specs for the selection process? Y(es) or N(o): ").capitalize()
        spec_type_filter = spec_selection(spec_type_select_trigger)
    return spec_type_filter

def class_selection(class_select_trigger, race_filter, faction_filter, spec_type_filter):
    if class_select_trigger == "Y" or class_select_trigger == "Yes":
        class_list = []
        if race_filter != None:
            for race in race_filter:
                for cls in races_classes[race]:
                    if spec_type_filter != None:
                        for spec in spec_type_filter:
                            if cls in spec_types[spec]:
                                class_list.append(cls)
                    else:
                        class_list.append(cls)
        elif race_filter == None and faction_filter != None:
            for race in faction_races[faction_filter]:
                for cls in races_classes[race]:
                    if spec_type_filter != None:
                        for spec in spec_type_filter:
                            if cls in spec_types[spec]:
                                class_list.append(cls)
                    else:
                        class_list.append(cls)
        else:
            for race in races_classes.keys():
                for cls in races_classes[race]:
                    if spec_type_filter != None:
                        for spec in spec_type_filter:
                            if cls in spec_types[spec]:
                                class_list.append(cls)
                    else:
                        class_list.append(cls)
        class_list = list(set(class_list))
        class_list.sort()
        print(f"Please choose one or multiple of the following classes:")
        for cls in class_list:
            print(f"- {cls}")
        class_filter = [cls.strip().capitalize() for cls in input("If you select more than one class, please separate with a ',': ").split(",")]
    elif class_select_trigger == "N" or class_select_trigger == "No":
        class_filter = None
    else:
        print("Please enter a valid option.")
        class_select_trigger = input("Do you want to select one or multiple classes for the selection process? Y(es) or N(o): ").capitalize()
        class_filter = class_selection(class_select_trigger, race_filter, faction_filter, spec_type_filter)
    return class_filter

def number_of_chars():
    while True:
        try:
            no_of_chars = int(input("How many randomly selected characters do you want to create? "))
            return no_of_chars
        except ValueError:
            print("Please only enter a full number.")    
    
def main():
    no_of_chars = number_of_chars()

    faction_select = input("Which faction do you play in? Please choose A(lliance), H(orde) or R(andom): ").capitalize()
    faction_filter = faction_selection(faction_select)

    race_select_trigger = input("Do you want to select one or multiple races for the selection process? Y(es) or N(o): ").capitalize()
    race_filter = race_selection(race_select_trigger, faction_filter)
    # race_filter = [race.strip() for race in input("Please select one or multiple races you'd like me to choose from, separated by ',' (e.g. Orc, Tauren, Troll): ").split(",")] if race_select_trigger == "Y" or race_select_trigger == "Yes" else None

    spec_type_select_trigger = input("Do you want to select one or multiple spec types for the selection process? Y(es) or N(o): ").capitalize()
    spec_type_filter = spec_selection(spec_type_select_trigger)
    # spec_type_filter = [spec.strip() for spec in input("Please select one or multiple spec types you'd like me to choose from, separated by ',' (e.g. Tank, Melee): ").split(",")] if spec_type_select_trigger == "Y" or spec_type_select_trigger == "Yes" else None

    class_select_trigger = input("Do you want to select one or multiple classes for the selection process? Y(es) or N(o): ").capitalize()
    class_filter = class_selection(class_select_trigger, race_filter, faction_filter, spec_type_filter)
    # class_filter = [cls.strip() for cls in input("Please select one or multiple classes you'd like me to choose from, separated by ',' (e.g. Warrior, Priest, Warlock): ").split(",")] if class_select_trigger == "Y" or class_select_trigger == "Yes" else None

    print("=" * 20)
    for idx in range(no_of_chars):
        character = random_character(faction_filter, race_filter, spec_type_filter, class_filter)
        print(f"Character {idx+1} Info:")
        print(f"Faction: {character['Faction']}")
        print(f"Starting Area: {character['Starting Area']}")
        print(f"Race: {character['Race']}")
        print(f"Class: {character['Class']}")
        print(f"Spec Type: {character['Spec Type']}")
        print("=" * 20)

# RCS
if __name__ == "__main__":
    print("Welcome to RCS - the Random Character Selector for World of Warcraft Classic!\n")
    # Maybe add some more text here
    
    main()

    # Maybe add some more text here