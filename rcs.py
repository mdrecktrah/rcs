# Version 0.1

# Import modules
import random

# Create dictionaries
faction_races = {
    "Alliance":["Dwarf", "Gnome", "Human", "Night Elf"],
    "Horde":["Orc", "Tauren", "Troll", "Undead"]
}

races_classes = {
    "Dwarf":["Hunter", "Paladin", "Priest", "Rogue", "Warrior"],
    "Gnome":["Mage", "Rogue", "Warlock", "Warrior"],
    "Human":["Mage", "Paladin", "Priest", "Rogue", "Warlock", "Warrior"],
    "Night Elf":["Druid", "Hunter", "Priest", "Rogue", "Warrior"],
    "Orc":["Hunter", "Rogue", "Shaman", "Warlock", "Warrior"],
    "Tauren":["Druid", "Hunter", "Shaman", "Warrior"],
    "Troll":["Hunter", "Mage", "Priest", "Rogue", "Shaman", "Warrior"],
    "Undead":["Mage", "Priest", "Rogue", "Warlock", "Warrior"]
}

start_areas_races = {
    "Dun Morogh":["Dwarf", "Gnome"],
    "Elwynn":"Human",
    "Teldrassil":"Night Elf",
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

    possible_races = faction_races[faction]
    if race_filter:
        possible_races = [race for race in possible_races if race in race_filter]
    selected_race = random.choice(possible_races)

    possible_classes = races_classes[selected_race]
    if class_filter:
        possible_classes = [cls for cls in possible_classes if cls in class_filter]
    selected_class = random.choice(possible_classes)

    start_area = None
    for area, races in start_areas_races.items():
        if selected_race in races:
            start_area = area
            break
    
    spec_type = None
    for spec, classes in spec_types.items():
        if selected_class in classes:
            spec_type = spec
            break

    return {
        "Faction": faction,
        "Race": selected_race,
        "Class": selected_class,
        "Starting Area": start_area,
        "Spec Type": spec_type
    }

def faction_selection(faction_select):
    if faction_select == "R" or faction_select == "Random":
        faction_filter = None
    elif faction_select == "A" or faction_select == "Alliance":
        faction_filter = "Alliance"
    elif faction_select == "H" or faction_select == "Horde":
        faction_filter = "Horde"
    else:
        print("Please select a valid option.")
        faction_selection(faction_select)
    return faction_filter
    
def main():
    no_of_chars = int(input("How many randomly selected characters do you want to create? "))

    faction_select = input("Which faction do you play in? Please choose A(lliance), H(orde) or R(andom): ").capitalize()
    faction_filter = faction_selection(faction_select)

    race_select_trigger = input("Do you want to select one or multiple races for the selection process? Y(es) or N(o): ").capitalize()
    race_filter = [race.strip() for race in input("Please select one or multiple races you'd like me to choose from, separated by ',' (e.g. Orc, Tauren, Troll): ").split(",")] if race_select_trigger == "Y" or race_select_trigger == "Yes" else None

    spec_type_select_trigger = input("Do you want to select one or multiple spec types for the selection process? Y(es) or N(o): ").capitalize()
    spec_type_filter = [spec.strip() for spec in input("Please select one or multiple spec types you'd like me to choose from, separated by ',' (e.g. Tank, Melee): ").split(",")] if spec_type_select_trigger == "Y" or spec_type_select_trigger == "Yes" else None

    class_select_trigger = input("Do you want to select one or multiple classes for the selection process? Y(es) or N(o): ").capitalize()
    class_filter = [cls.strip() for cls in input("Please select one or multiple classes you'd like me to choose from, separated by ',' (e.g. Warrior, Priest, Warlock): ").split(",")] if class_select_trigger == "Y" or class_select_trigger == "Yes" else None

    for idx in range(no_of_chars):
        character = random_character(faction_filter, race_filter, spec_type_filter, class_filter)
        print(f"Character {idx+1} Info:")
        print(f"Faction: {character['Faction']}")
        print(f"Race: {character['Race']}")
        print(f"Class: {character['Class']}")
        print(f"Starting Area: {character['Starting Area']}")
        print(f"Specialization: {character['Spec Type']}")
        print("=" * 20)

# RCS
if __name__ == "__main__":
    print("Welcome to RCS - the Random Character Selector for World of Warcraft Classic!\n")
    # Maybe add some more text here
    main()