"""
    Script to create a bunch of different files
    to be used with CP1404 workshop task to rename and move them
    Lindsay Ward
    20/10/2015
"""
import random, os

__author__ = 'Lindsay Ward'
LETTERS = "playing jazz vibe chords quickly excites my wife"
EXTENSIONS = ["txt", "xls", "xlsx", "doc", "docx", "jpg", "gif", "png"]


def main():
    os.chdir("FilesToSort")
    words = LETTERS.split(" ")
    # for i in range(5):
    #     print(generate_random_text())

    for extension in EXTENSIONS:
        create_file(words[random.randrange(0, len(words))] + "." + extension)


def generate_random_text():
    letters_list = random.sample(LETTERS, random.randint(10, 20))
    return "".join(letters_list)


def create_file(name):
    out_file = open(name, 'w')
    out_file.write("".join(generate_random_text()))
    out_file.close()


main()
