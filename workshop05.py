__author__ = 'sci-lmw1'

# Code to fix - scores by person instead of by subject

# scores_file = open("scores.csv")
# scores_data = scores_file.readlines()
# print(scores_data)
# subjects = scores_data[0].strip().split(",")
# score_values = []
# for score_line in scores_data[1:]:
#     score_strings = score_line.strip().split(",")
#     score_numbers = [int(value) for value in score_strings]
#     score_values.append(score_numbers)
#
# scores_file.close()
#
# for i in range(len(subjects)):
#     print(subjects[i], "Scores:")
#     for score in score_values[i]:
#         print(score)
#     print("Max:", max(score_values[i]))
#     print()


# incomes = []
# months = int(input("How many months? "))
#
# for month in range(1, months + 1):
#     income = float(input("Enter income for month " + str(month) + ": "))
#     incomes.append(income)
#
# print()
# print("Income Report")
# print("-------------")
#
# total = 0
# for month in range(1, months + 1):
#     income = incomes[month - 1]
#     total += income
#
#     print("Month", format(month, "2d"), "- Salary: $",
#           format(income, "10.2f"),
#           "Total: $", format(total, "10.2f"))


# Word Counter
filename = input("Enter the filename: ")
inputFile = open(filename, 'r')
# initialise a dictionary of unique words
uniqueWords = {}

# Add the unique words in the file to the list
for line in inputFile:
    words = line.split()
    for word in words:
        frequency = uniqueWords.get(word, 0)
        if frequency is None:
            uniqueWords[word] = 1
        else:
            uniqueWords[word] = frequency + 1
inputFile.close()

# Print the unique words and their frequencies,
# in alphabetical order
words = list(uniqueWords.keys())
words.sort()
for word in words:
    print(word, ":", uniqueWords[word])

