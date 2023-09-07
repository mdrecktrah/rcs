# To-Dos:
- Build a proper interface (HTML?)
- Make user input (e.g. classes, races) more flexible in terms of how to write them (e.g. capitalizing)
    - Could be skipped with the interface, which can just include checkboxes and/or dropdowns
- Implement handling of empty inputs
- Check/implement error handling for ValueErrors (Numbers for strings and vice versa)
- Implement random sex (aka body type) for the character
- Add random name generator
- Add check for multiple chars to start in the same area
    - If you want to play with your friends, it would be a pain to first have to travel to another starting area just to get started together
- Avoid doubles in output
- Add option to create a new list - with same inputs or by restarting the whole process

# Version history

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