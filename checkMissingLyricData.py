""" CP1404 workshop solution - Check lyrics files for missing ".i" information
    Lindsay Ward
    20/10/2015
"""
import os

__author__ = 'Lindsay Ward'


def file_contains_info(filename):
    """
    :param filename: name of file to check for information
    :return: true if file contains copyright information, false otherwise
    """
    in_file = open(filename, 'r', encoding='utf-8')
    for line in in_file:
        if line.startswith('.i'):
            in_file.close()
            return True
    in_file.close()
    return False

os.chdir("Lyrics")

# process every file in every directory
for dir_name, subdir_list, file_list in os.walk('.'):

    # skip '.' directory
    if dir_name != ".":
        # for each file in a directory, check file for info and report if not found
        for filename in file_list:
            full_filename = dir_name + "/" + filename
            # print("checking {}\t-\t{}".format(dir_name, filename))
            if not file_contains_info(full_filename):
                print("{}\t-\t{}".format(dir_name, filename))