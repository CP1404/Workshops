"""
    CP1404 workshop solution for sorting files into subfolders by category
"""
import os, shutil
__author__ = 'Lindsay Ward'


def version1():
    """ create a folder with for each new extension and move files into these """
    categories = []

    os.chdir('FilesToSort')

    for filename in os.listdir('.'):
        # print(filename)
        extension = filename[filename.rfind('.') + 1:]
        # print(extension)
        # only make new folders for extensions we haven't seen before
        if extension not in categories:
            categories.append(extension)
            os.mkdir(extension)
        shutil.move(filename, extension)


def version2():
    """ allow user to choose categories to store different file types in
    create a folder for each category and move files into these """
    extension_categories = {}  # map extensions to category names
    categories = []  # keep track of just the category names for simplicity

    os.chdir('FilesToSort')

    for filename in os.listdir('.'):
        extension = filename[filename.rfind('.') + 1:]
        # prompt user for category if we haven't already categorised this extension
        if extension not in extension_categories:
            category = input("What category would you like to sort {} files into? ".format(extension))
            extension_categories[extension] = category

            # only make new folders for extensions we haven't seen before
            if category not in categories:
                categories.append(category)
                os.mkdir(category)
        shutil.move(filename, extension_categories[extension])

version2()
