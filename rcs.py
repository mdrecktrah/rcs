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

roles_classes = {
    "Tank":["Druid", "Paladin", "Warrior"],
    "Healer":["Druid", "Paladin", "Priest", "Shaman"],
    "Melee":["Druid", "Paladin", "Rogue", "Shaman", "Warrior"],
    "Ranged":["Druid", "Hunter", "Mage", "Priest", "Shaman", "Warlock"]
}

# Define functions
def number_of_chars():
    while True:
        try:
            no_of_chars = int(input("How many randomly selected characters do you want to create? "))
            if no_of_chars < 1 or no_of_chars > 5:
                print("Please enter a number from 1 and 5.")
                continue
            else:
                return no_of_chars
        except ValueError:
            print("Please only enter a full number.") 

def faction_selection(faction_select):
    if faction_select == "R" or faction_select == "Random":
        faction_filter = None
    elif faction_select == "A" or faction_select == "Alliance":
        faction_filter = "Alliance"
    elif faction_select == "H" or faction_select == "Horde":
        faction_filter = "Horde"
    else:
        faction_select = input("Please select a valid option - A(lliance), H(orde) or R(andom): ").capitalize()
        faction_filter = faction_selection(faction_select)
    return faction_filter

def role_selection(role_select_trigger):
    if role_select_trigger == "Y" or role_select_trigger == "Yes":
        print("Please choose one or multiple of the following roles:")
        for role in roles_classes.keys():
            print(f"- {role}")
        role_filter = [role.strip().capitalize() for role in input("If you select more than one role, please separate with a ',': ").split(",")]
        for role in role_filter:
            if role not in list(roles_classes.keys()):
                print("Please only enter valid options from the list below.")
                role_filter = role_selection(role_select_trigger)
    elif role_select_trigger == "N" or role_select_trigger == "No":
        role_filter = None
    else:
        print("Please enter a valid option.")
        role_select_trigger = input("Do you want to select one or multiple roles for the selection process? Y(es) or N(o): ").capitalize()
        role_filter = role_selection(role_select_trigger)
    return role_filter

def class_selection(class_select_trigger, faction_filter, role_filter):
    if class_select_trigger == "Y" or class_select_trigger == "Yes":
        if role_filter != None:
            for role in role_filter:
                class_list = [cls for cls in roles_classes[role]]
        else:
            class_list = [cls for classes in roles_classes.values() for cls in classes]
        class_list = list(set(class_list))
        class_list.sort()
        if faction_filter == "Alliance" and "Shaman" in class_list:
            class_list.remove("Shaman")
        elif faction_filter == "Horde" and "Paladin" in class_list:
            class_list.remove("Paladin")
        print(f"Please choose one or multiple of the following classes:")
        for cls in class_list:
            print(f"- {cls}")
        class_filter = [cls.strip().capitalize() for cls in input("If you select more than one class, please separate with a ',': ").split(",")]
        for cls in class_filter:
            if cls not in class_list:
                print("Please only enter valid options from the list below.")
                class_filter = class_selection(class_select_trigger, faction_filter, role_filter)
    elif class_select_trigger == "N" or class_select_trigger == "No":
        class_filter = None
    else:
        print("Please enter a valid option.")
        class_select_trigger = input("Do you want to select one or multiple classes for the selection process? Y(es) or N(o): ").capitalize()
        class_filter = class_selection(class_select_trigger, faction_filter, role_filter)
    return class_filter

def race_selection(race_select_trigger, faction_filter, role_filter, class_filter):
    if race_select_trigger == "Y" or race_select_trigger == "Yes":
        if class_filter != None:
            race_list = [race for race, classes in races_classes.items() for cls in class_filter if cls in classes]
        else:
            race_list = [race for race in races_classes.keys()]
        race_list = list(set(race_list))
        race_list.sort()
        if role_filter == ["Healer"] and "Gnome" in race_list:
            race_list.remove("Gnome")
        if faction_filter == "Alliance":
            for race in faction_races["Horde"]:
                try:
                    race_list.remove(race)
                except ValueError:
                    continue
        elif faction_filter == "Horde":
            for race in faction_races["Alliance"]:
                try:
                    race_list.remove(race)
                except ValueError:
                    continue            
        print(f"Please choose one or multiple of the following races:")
        for race in race_list:
            print(f"- {race}")
        race_filter = [race.strip().capitalize() for race in input("If you select more than one race, please separate with a ',': ").split(",")]
        for race in race_filter:
            if race not in race_list:
                print("Please only enter valid options from the list below.")
                race_filter = race_selection(race_select_trigger, faction_filter, role_filter, class_filter)
    elif race_select_trigger == "N" or race_select_trigger == "No":
        race_filter = None
    else:
        print("Please enter a valid option.")
        race_select_trigger = input("Do you want to select one or multiple races for the selection process? Y(es) or N(o): ").capitalize()
        race_filter = race_selection(race_select_trigger, faction_filter, role_filter, class_filter)
    return race_filter

def random_sex():
    selected_sex = random.choice(["Male", "Female"])
    return selected_sex

def select_faction(faction_filter):
    if faction_filter is None:
        selected_faction = random.choice(list(faction_races.keys()))
    else:
        selected_faction = faction_filter
    return selected_faction

def select_role(role_filter, class_filter):
    if role_filter is None and class_filter is None:
        selected_role = random.choice(list(roles_classes.keys()))
    elif role_filter is None and class_filter != None:
        possible_roles = []
        for cls in class_filter:
            for role in roles_classes.keys():
                if cls in roles_classes[role]:
                    possible_roles.append(role)
        possible_roles = list(set(possible_roles))
        possible_roles.sort()
        selected_role = random.choice(possible_roles)         
    else:
        selected_role = random.choice(role_filter)
    return selected_role

def random_character(faction_filter, role_filter, class_filter, race_filter):
    selected_faction = select_faction(faction_filter)
    selected_role = select_role(role_filter, class_filter)
    
    possible_classes = []
    while possible_classes == []:
        if class_filter is None:
            possible_classes = roles_classes[selected_role]
        elif class_filter != None:
            for cls in class_filter:
                if cls in roles_classes[selected_role]:
                    possible_classes.append(cls)
        if selected_faction == "Alliance" and "Shaman" in possible_classes:
            possible_classes.remove("Shaman")
        elif selected_faction == "Horde" and "Paladin" in possible_classes:
            possible_classes.remove("Paladin")
        if possible_classes == []:
            selected_faction = select_faction(faction_filter)
            selected_role = select_role(role_filter, class_filter)
            continue

    selected_class = None
    while selected_class is None:
        selected_class = random.choice(possible_classes)

        possible_races = list(set([race for race, classes in races_classes.items() if selected_class in classes and race in faction_races[selected_faction]]))
        selected_race = None
        while selected_race is None:
            try:
                if race_filter is None:
                    selected_race = random.choice(possible_races)
                else:
                    selected_race = random.choice(list(set([race for race in race_filter if selected_class in races_classes[race]])))
            except IndexError:
                selected_class = random.choice(possible_classes)
                continue
 
    selected_sex = random_sex()
    
    return {
        "Faction": selected_faction,
        "Race": selected_race,
        "Class": selected_class,
        "Role": selected_role,
        "Sex": selected_sex
    }

def start_again(repeat_trigger):
    if repeat_trigger == "Y" or repeat_trigger == "Yes":
        print("====================")
        main()
    elif repeat_trigger == "N" or repeat_trigger == "No":
        exit()
    else:
        print("Please enter a valid option.")
        repeat_trigger = input("Would you like to start RCS from the beginning? Y(es) or N(o): ").capitalize()
        start_again(repeat_trigger)

def main():
    no_of_chars = number_of_chars()
    
    faction_select = input("Which faction do you want to play in? Please choose A(lliance), H(orde) or R(andom): ").capitalize()
    faction_filter = faction_selection(faction_select)

    role_select_trigger = input("Do you want to select one or multiple roles for the selection process? Y(es) or N(o): ").capitalize()
    role_filter = role_selection(role_select_trigger)

    class_select_trigger = input("Do you want to select one or multiple classes for the selection process? Y(es) or N(o): ").capitalize()
    class_filter = class_selection(class_select_trigger, faction_filter, role_filter)

    race_select_trigger = input("Do you want to select one or multiple races for the selection process? Y(es) or N(o): ").capitalize()
    race_filter = race_selection(race_select_trigger, faction_filter, role_filter, class_filter)
    
    print("=" * 20)
    for idx in range(no_of_chars):
        try:
            character = random_character(faction_filter, role_filter, class_filter, race_filter)
        except IndexError:
            print("Unfortunately, there are no valid options for your filters. Please try again.")
            break
        print(f"Character {idx+1} Info:")
        print(f"Faction: {character['Faction']}")
        print(f"Race: {character['Race']} ({character['Sex']})")
        print(f"Class: {character['Class']}")
        print(f"Role: {character['Role']}")
        print("=" * 20)

    repeat_trigger = input("Would you like to start RCS from the beginning? Y(es) or N(o): ").capitalize()
    start_again(repeat_trigger) 

# RCS
if __name__ == "__main__":
    print("Welcome to RCS - the Random Character Selector for World of Warcraft Classic!\n")    
    main()