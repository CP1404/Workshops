""" CP1404 workshop solution - Rename lyrics files
    Lindsay Ward
    20/10/2015
"""
import os

__author__ = 'Lindsay Ward'


def get_fixed_filename(filename):
    # make new name, starting from uppercase first letter
    new_name = filename[0].upper()
    # loop through all characters from second letter to the .
    # assume no other dots in filenames, or safe to change after first dot
    for i, character in enumerate(filename[1:filename.find('.')]):
        # print(i, character)
        if character.isupper():
            # for uppercase chars, check if previous char is a space or (, add one if not
            if filename[i] == " " or filename[i] == "(":
                new_name += character
            else:
                new_name += " " + character
        else:
            # for lowercase chars, check if previous char is a space or (, add uppercase char if so
            if filename[i] == " " or filename[i] == "(":
                new_name += character.upper()
            else:
                new_name += character
    # replace all spaces with underscores
    # new_name = new_name.replace(' ', '_')
    new_name += ".txt"
    return new_name

# test get_fixed_filename function with problematic names
# for name in ["Away In A Manger.txt", "SilentNight.txt", "O little town of bethlehem.TXT", "Oceans (Where Feet May Fail).txt", "ItIsWell (oh my soul).txt"]:
#     print(get_fixed_filename(name))

os.chdir("Lyrics")

# process every file in every directory
for dir_name, subdir_list, file_list in os.walk('.'):
    # print values to see how walk works
    # print("In", dir_name)
    # print("\tcontains subdirectories:", subdir_list)
    # print("\tand files:", file_list)

    # skip '.' directory
    if dir_name != ".":
        # create directory name for renaming
        path = dir_name + '/'
        # for each file in a directory, get a fixed version of name and rename
        for filename in file_list:
            fixed_name = get_fixed_filename(filename)
            # print(fixed_name)
            os.rename(path + filename, path + fixed_name)
