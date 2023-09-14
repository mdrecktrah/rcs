# To-Dos:
- Implement random sex (aka body type) for the character
- Implement handling of empty and/or wrong inputs (e.g. you select faction filter for Horde and race filter for Alliance races)
- Check/implement error handling for ValueErrors (Numbers for strings and vice versa)
- Add check for multiple chars to start in the same area
    - If you want to play with your friends, it would be a pain to first have to travel to another starting area just to get started together
- Avoid doubles in output
- Add option to create a new list - with same inputs or by restarting the whole process
- Build UI
    - This will also avoid errors due to misspelling or lower-/uppercase mistakes
- Add random name generator
# Version history

## Version 0.3 - TBD
- Re-arranged order of the filter selection
    - Was Faction -> Race -> Role (former Spec Type) -> Class
    - Is now Faction -> Role (former Spec Type) -> Class -> Race
- Also: Changed Spec Type to Role, as this is more fitting to how Blizzard calls it
    - Roles include: Tank, Healer, Melee (DPS), Ranged (DPS)

## Version 0.2 - 2023/09/07
- Minor changes to README.
- Added lists of viable options whenever you choose to set a filter for races, specs and classes.
- Fixed a bug that caused Specs to always be selected in order Tank > Healer > Melee > Ranged => Should now be randomized.

## Version 0.1 - 2023/08/29
First working version of the program, but still missing proper error handling. Functionality include:
- Set the number of characters you want to be created.
- Choose faction: Alliance, Horde or random choice.
- Further filtering possibilities: Race, Spec Type, Classes.
    - Race and Class combinations according to WoW Classic. You can check out all combinations on [WoWHead](https://www.wowhead.com/classic/guide/classic-wow-classes-and-talent-overview#class-race-combinations) or many other sites. Sorry, but no Night Elf Paladins here!
- After all your filters have been set (or... not set), the program will randomize every open possibility and print a list with as many characters as you set in the beginning. Enjoy your leveling experience! =)